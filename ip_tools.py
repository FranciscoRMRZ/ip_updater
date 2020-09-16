#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
import requests

# Refactor to use relative paths instead of absolute ones.

def get_public_ip():
    res = requests.get("http://ip4only.me/api/")
    public_ip = res.text.split(',')[1]
    return public_ip

def read_registered_ip():
    with open('public_ip.txt') as ip:
        registered_ip = ip.read()
        return registered_ip

def update_registered_ip(new_ip_address):
    with open('public_ip.txt', 'w') as ip:
        ip.write(new_ip_address)