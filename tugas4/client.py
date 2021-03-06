import sys
import socket
import os
from client_download import c_download
from client_upload import c_upload
from client_list import c_list


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    print("command menu : \n\tdownload\n\tupload\n\tlist\n\texit")
    command = input("enter command : ")
    if (command=='download'):
        filename = input("enter namefile : ")
        c_download(sock,command,filename)
        sock.close()
    elif (command=='upload'):
        filename = input("enter namefile : ")
        c_upload(sock,command,filename)
        sock.close()
    elif (command=='list'):
        c_list(sock,command)
        sock.close()
    elif (command == 'exit'):
        exit()
    else: 
        print("ERRCMD")
        