import os
import smtplib
from email.message import EmailMessage
from django.conf import settings

#This function automatically sends emails to customers attached with the corresponding invoice and documents



#Email credentials stored in local file
email_user_dir = settings.EMAIL_USER_DIR
with open(email_user_dir) as f:
    email_address = f.readline()
        

email_pass_dir = settings.EMAIL_PASS_DIR

with open(email_pass_dir) as f:
    email_password = f.readline()



class Email:

    #Add all files in a given directory to a dictionary as a key and store file-type as value
    #Allows for proper attachment when calling add_attachment method of the EmailMessage Class

    def get_files(self, files_dir):
        file_dict = {}
        for dir, folders, files in os.walk(files_dir):
            for file in files:
                file_path = dir + file #generate separate file path in dictionary for each individual file to be attached
                file_type = os.path.splitext(file)[1]
                file_dict[file_path] = file_type
        print(file_dict)
        return file_dict

    #send_email generates the complete email with from, to, subject line, and attachments, and sends it
    def send_email(self, file_dict, load_ref):
        
        msg = EmailMessage()
        msg ['Subject'] = "Invoice and POD for Load " + load_ref
        msg['From'] = email_address
        msg['To'] = 'motlani.saqib@gmail.com'

        for file, path in file_dict.items():
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name

                if path == ".jpg":
                    msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=load_ref + "POD")
                if path == '.xlsx':
                    msg.add_attachment(file_data, maintype='application', subtype='xlsx', filename=load_ref + "_Invoice.xlsx")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)


