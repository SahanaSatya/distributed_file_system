#author : Sahana Satyanarayana sasa7902@colorado.edu
#name   : Assignment 5
#purpose: Socket Programming
#date   : 2018.10.19
#version: 3.7
import sys
import os
import time
import socket
import argparse
from socket import errno
from ctypes import WinError

def create_socket(server_name,server_port):
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((server_name,server_port))
    server_socket.listen(5)
    print("Server is ready to receive")
    while True:
        client_socket,client_addr = server_socket.accept()
        option=client_socket.recv(2048)
        option=option.decode()
        if option == "get":
            file_name = client_socket.recv(2048)
            file_name=file_name.decode()
            if os.path.isfile(file_name):
                file_exists ="Yes"
            else:
                file_exists = "No" 
            client_socket.send(file_exists.encode())
            if file_exists == "Yes":
                file_size = os.path.getsize(file_name)
                client_socket.send(str(file_size).encode())
                with open(file_name,"rb") as sending_file:
                    temp_file_buffer = sending_file.read(65000)
                    while(temp_file_buffer):
                        print("Transferring....")
                        client_socket.send(temp_file_buffer)
                        time.sleep(1)
                        temp_file_buffer=sending_file.read(65000)
                print("Transferring done")
                sending_file.close()
            else:
                print("The file was not found") 
        if option == "put":
            file_name=client_socket.recv(2048)
            file_name=file_name.decode()
            file_size=client_socket.recv(2048)
            file_size=int(file_size.decode())
            file1=client_socket.recv(2048)
            file1=file1.decode()
            print("File about start to download the file "+file_name)
            size=0 
            while(size<=file_size):
                file_content=client_socket.recv(min(file_size - size,65000))
                fh=open(file1,"ab")
                fh.write(file_content)
                print("Receiving....")
                size+=65000
            fh.close()
            print("File "+file1+" received")
            file_size=client_socket.recv(2048)
            file_size=int(file_size.decode())
            file2=client_socket.recv(2048)
            file2=file2.decode()
            size=0
            while(size<=file_size):
                file_content=client_socket.recv(min(file_size - size,65000))
                fh=open(file2,"ab")
                fh.write(file_content)
                print("Receiving....")
                size+=65000
            fh.close()
            print("File "+file2+" received")
        if option == "list":
            list_of_files=os.listdir()
            num_of_file_names_sent=len(list_of_files) - 1
            client_socket.send(str(num_of_file_names_sent).encode())
            for i in range (0,len(list_of_files)):
                if list_of_files[i] != "server.py":
                    client_socket.send(str(list_of_files[i]).encode())
            print("List of files sent successfully")
            
if __name__=="__main__":
    server_name= '127.0.0.1'
    server_port= 10004
    create_socket(server_name,server_port)
quit()