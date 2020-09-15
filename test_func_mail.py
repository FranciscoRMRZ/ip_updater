#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
# This program will apply the steps described in the following guide:
# Guide 2: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

# TODO: Implement JSON to use a secrets file.
# TODO: Implement body text file.
# TODO: Implement OAuth

from  func_mail_sender import send_mail



if __name__ == "__main__":
    send_mail("francisco.ramirez.valdes@gmail.com")
