from fileinput import filename
import imghdr
import os
from os import path
import smtplib
from email.message import EmailMessage
import imghdr


with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_address.txt') as f:
        email_address = f.readline()
        

with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/email_password.txt') as f:
        email_password = f.readline()
    
class Email:
    def __init__(self) -> None:
        pass

    def get_files(self):

        path_dict = {}
        my_dir = "/Users/sm/Desktop/Symport/agt/248975/"
        for dir, folders, files in os.walk(my_dir):
            for file in files:
                file_path = dir + file
                file_type = os.path.splitext(file)[1]
                path_dict[file_path] = file_type
        
        return path_dict

    def send_email(self, path_dict):
        
        msg = EmailMessage()
        msg ['Subject'] = "Test Email 1"
        msg['From'] = email_address
        msg['To'] = 'motlani.saqib@gmail.com'

        path_dict = path_dict

        for file, path in path_dict.items():
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name

                if path == ".jpg":
                    fileType = imghdr.what(f.name)
                    msg.add_attachment(file_data, maintype='image', subtype=fileType, filename=file_name)
                if path == '.xlsx':
                    msg.add_attachment(file_data, maintype='application', subtype='xlsx', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)


