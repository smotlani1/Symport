import os
import smtplib
from email.message import EmailMessage
from django.conf import settings
import boto3

#Establish client with s3 bucket
s3 = boto3.client('s3',  aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name='us-east-1')

#This function automatically sends emails to customers attached with the corresponding invoice and documents

class Email:

    def send_email(self, file_dir, load_ref, attachments):
        
        msg = EmailMessage()
        msg ['Subject'] = "Invoice and POD for Load " + load_ref
        msg['From'] = settings.EMAIL_USER
        msg['To'] = 'motlani.saqib@gmail.com'

        for item in attachments:
            s3_data = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=f'{item}')
            contents = s3_data['Body'].read()
            msg.add_attachment(contents, maintype='image', subtype='jpg', filename=load_ref + "POD")


        #Iterates items in a given file of the bucket, determines filetype (i.e xlsx, jpg, etc) and attaches all files to email message

        for item in s3.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Prefix=file_dir)['Contents']:
            key = item['Key']
            s3_data = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
            contents = s3_data['Body'].read()
            
            if key.endswith('.xlsx'):
                msg.add_attachment(contents, maintype='application', subtype='xlsx', filename=load_ref + "_Invoice.xlsx")
            elif key.endswith('.jpg') or key.endswith('.png'):
                msg.add_attachment(contents, maintype='image', subtype='jpg', filename=load_ref + "POD")


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_USER, settings.EMAIL_PASS)
            smtp.send_message(msg)






#     #Add all files in a given directory to a dictionary as a key and store file-type as value
#     #Allows for proper attachment when calling add_attachment method of the EmailMessage Class

    # def get_files(self, files_dir):
    #     file_dict = {}
    #     for dir, folders, files in os.walk(files_dir):
    #         for file in files:
    #             file_path = dir + file #generate separate file path in dictionary for each individual file to be attached
    #             file_type = os.path.splitext(file)[1]
    #             file_dict[file_path] = file_type
    #     print(file_dict)
    #     return file_dict

#     #send_email generates the complete email with from, to, subject line, and attachments, and sends it




        # for file, path in file_dict.items():
        #     with open(file, 'rb') as f:
        #         file_data = f.read()
        #         file_name = f.name

        #         if path == ".jpg":
        #             msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=load_ref + "POD")
        #         if path == '.xlsx':
        #             msg.add_attachment(file_data, maintype='application', subtype='xlsx', filename=load_ref + "_Invoice.xlsx")