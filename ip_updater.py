#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
import ip_tools
from func_mail_sender import send_mail


current_ip = ip_tools.get_public_ip()
registered_ip = ip_tools.read_registered_ip()
send_to = 'francisco.ramirez@compujal.com'
if current_ip == registered_ip:
    print('No need to update the ip address.')
else:
    ip_tools.update_registered_ip(current_ip)
    body = f'The ip has been updated to: {current_ip}'
    # Mail module to send the address.
    send_mail(send_to, body)
    


