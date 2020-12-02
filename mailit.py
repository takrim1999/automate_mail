#!/usr/bin/python3
import os.path
from email.message import EmailMessage
import smtplib
import mimetypes
from getpass import getpass
sender = input("your mail: ")
mail_pass = getpass("password: ")
receiver = input("To whom send mail: ")
subject = input("subject: ")
body = input("body:\n>")
message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject #"""my automated mails to several mail id"""
#body = "sending a photo attachment and a string message via script to 7 different mail id"
message.set_content(body)
attachment_path = os.path.abspath("robot.png")
mime_types, _ = mimetypes.guess_type(attachment_path)
mime_type,mime_subtype = mime_types.split("/", 1)
with open(attachment_path , "rb") as ap:
    message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype , filename = os.path.basename(attachment_path))
mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
mail_server.set_debuglevel(1)
mail_server.login(sender , mail_pass)
mail_server.send_message(message)
