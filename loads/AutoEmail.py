from fileinput import filename
import imghdr
import os
from os import path
import smtplib
from email.message import EmailMessage



with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_address.txt') as f:
    email_address = f.readline()
        

with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_password.txt') as f:
    email_password = f.readline()
    
class Email:
    # def __init__(self):
    #     self.email_address = email_address

    def get_files(self, files_dir):

        file_dict = {}
        for dir, folders, files in os.walk(files_dir):
            for file in files:
                file_path = dir + file
                file_type = os.path.splitext(file)[1]
                file_dict[file_path] = file_type
        print(file_dict)
        return file_dict

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


