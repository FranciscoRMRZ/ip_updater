#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python

def update_registered_ip(new_ip_address):
    with open('/Users/Francisco/Documents/ATBSWP/ip_updater/public_ip.txt', 'w') as ip:
        ip.write(new_ip_address)