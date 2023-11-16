#!/usr/bin/env python3

import cgi
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(name, email, subject, message):
    receiving_email_address = 'guru2611199@gmail.com'

    # Set up the email server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'guru2611199@gmail.com'
    smtp_password = 'rqoq wfef mqbc ewmj'

    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiving_email_address
    msg['Subject'] = subject

    # Attach the message to the email
    body = f"From: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email, receiving_email_address, msg.as_string())

    print("Content-type: text/html\n")
    print("<html><body>")
    print("<h1>Email sent successfully!</h1>")
    print("</body></html>")

def main():
    form = cgi.FieldStorage()

    if "name" in form and "email" in form and "subject" in form and "message" in form:
        name = form.getvalue("name")
        email = form.getvalue("email")
        subject = form.getvalue("subject")
        message = form.getvalue("message")

        send_email(name, email, subject, message)
    else:
        print("Content-type: text/html\n")
        print("<html><body>")
        print("<h1>Error: Missing form fields</h1>")
        print("</body></html>")

if __name__ == '__main__':
    main()
