#! /Users/Francisco/Documents/ATBSWP/ATBSWP_ve/bin/python
import requests
def get_public_ip():
    res = requests.get('http://ip4only.me/api/')
    public_ip = res.text.split(',')[1]
    return public_ip