#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
# This program will apply the steps described in the following guide:
# Guide 2: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

# TODO: Implement JSON to use a secrets file.
# TODO: Implement body text file.
# TODO: Implement OAuth

import smtplib
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

def send_mail(sent_to, body):
    # Credentials.
    mail_user = <email_user>
    mail_password = <password>

    # Mail formatting.
    sent_from = <sender>    
    subject = <subject>
    # body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. '

    email_text = f'from: {sent_from}\nTo: {sent_to}\nSubject: {subject}\n{body}'

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_password)
        # send the mails
        server.sendmail(sent_from, sent_to, email_text)
        logging.debug(f'sent_from: {sent_from}, sent_to: {sent_to}')
        logging.debug(f'email_text: {email_text}')
        server.close()
        logging.debug('Email sent.')
        
    except:
        logging.debug("Something went wrong.")

