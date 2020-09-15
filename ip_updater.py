#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
from func_get_public_ip import get_public_ip
from func_registered_ip import read_registered_ip
from func_update_ip import update_registered_ip
from func_mail_sender import send_mail


current_ip = get_public_ip()
registered_ip = read_registered_ip()
send_to = 'francisco.ramirez@compujal.com'
if current_ip == registered_ip:
    print('No need to update the ip address.')
else:
    update_registered_ip(current_ip)
    body = f'The ip has been updated to: {current_ip}'
    send_mail(send_to, body)
    #TODO: Add email module to send the address.


