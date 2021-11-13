from ftplib import FTP 
import os
import fileinput
from pathlib import Path
from typing_extensions import TypedDict


def get_file_from_ftp(file_path, file_name):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('192.168.0.1', 21) 
    ftp.login('Usb','Andz1k')
    ftp.cwd('/SharedFolder')
    localfile = open(file_name, 'wb')
    ftp.retrbinary('RETR {}'.format(file_path), localfile.write, 1024)
    localfile.close()
    ftp.close()

def get_server_ip_address(log_path):
    data_folder = Path(log_path)
    file_to_open = data_folder
    f = open(file_to_open)
    data = []
    for row in f:
        if 'in a browser' in row:
            data.append(row)
    
    data = data[-1].split(' ')
    ip_address = ''
    for row in data:
        if 'http' in row:
            ip_address = row
            break
    return ip_address
    # test
