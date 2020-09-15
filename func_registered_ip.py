#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python

def read_registered_ip():
    with open('/Users/Francisco/Documents/ATBSWP/ip_updater/public_ip.txt') as ip:
        registered_ip = ip.read()
        return registered_ip