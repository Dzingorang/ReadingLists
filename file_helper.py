from ftplib import FTP 
import os
import fileinput

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