#author : Sahana Satyanarayana sasa7902@colorado.edu
#name   : Assignment 5
#purpose: Socket Programming
#date   : 2018.10.19
#version: 3.7
import sys
import socket
import argparse
import os
import time
import hashlib

def create_socket_put(option,file_name,server_name,server_port1, server_port2, server_port3, server_port4):
    if os.path.isfile(file_name):
            file_exists ="Yes"
    else:
            file_exists = "No"
    if file_exists == "Yes":
            file_size = os.path.getsize(file_name)
            size_4 = int(file_size/4);
            with open(file_name,"rb") as file_full:
                with open(file_name+".1","wb") as file1:
                    size=0
                    while(size<=size_4):
                        file1.write(file_full.read(min(size_4 - size,65000)))
                        size+=65000
                print("File 1 created")
                with open(file_name+".2","wb") as file2:
                    size=0
                    while(size<=size_4):
                        file2.write(file_full.read(min(size_4 - size,65000)))
                        size+=65000
                print("File 2 created")
                with open(file_name+".3","wb") as file3:
                    size=0
                    while(size<=size_4):
                        file3.write(file_full.read(min(size_4 - size,65000)))
                        size+=65000
                print("File 3 created")
                with open(file_name+".4","wb") as file4:
                    size=3*size_4
                    while(size<=file_size):
                        file4.write(file_full.read(min(file_size - size,65000)))
                        size+=65000
                print("File 4 created")
    else:
        print("file does not exist")
        return
    mdhash = hashlib.md5(file_name.encode())
    x = int(mdhash.hexdigest(),16)%4
    if (x == 0):
        file1=file_name+".1"
        file2=file_name+".2"
        file3=file_name+".2"
        file4=file_name+".3"
        file5=file_name+".3"
        file6=file_name+".4"
        file7=file_name+".4"
        file8=file_name+".1"
    if (x == 1):
        file1=file_name+".4"
        file2=file_name+".1"
        file3=file_name+".1"
        file4=file_name+".2"
        file5=file_name+".2"
        file6=file_name+".3"
        file7=file_name+".3"
        file8=file_name+".4"
    if (x == 2):
        file1=file_name+".3"
        file2=file_name+".4"
        file3=file_name+".4"
        file4=file_name+".1"
        file5=file_name+".1"
        file6=file_name+".2"
        file7=file_name+".2"
        file8=file_name+".3"
    if (x == 3):
        file1=file_name+".2"
        file2=file_name+".3"
        file3=file_name+".3"
        file4=file_name+".4"
        file5=file_name+".4"
        file6=file_name+".1"
        file7=file_name+".1"
        file8=file_name+".2"    
    try:
        client_socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket1.connect((server_name,server_port1))
        client_socket1.send(option.encode())
        time.sleep(.3)
        client_socket1.send(file_name.encode())
        time.sleep(.3)
        client_socket1.send(str(os.path.getsize(file1)).encode())
        time.sleep(.3)
        client_socket1.send(file1.encode())
        with open(file1,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket1.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        time.sleep(.3)
        client_socket1.send(str(os.path.getsize(file2)).encode())
        time.sleep(.3)
        client_socket1.send(file2.encode())
        with open(file2,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket1.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        print("server 1 done")
    except:
        print("Problem with Server 1")
    
    try:
        client_socket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket2.connect((server_name,server_port2))
        client_socket2.send(option.encode())
        time.sleep(.3)
        client_socket2.send(file_name.encode())
        time.sleep(.3)
        client_socket2.send(str(os.path.getsize(file3)).encode())
        time.sleep(.3)
        client_socket2.send(file3.encode())
        with open(file3,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket2.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        time.sleep(.3)
        client_socket2.send(str(os.path.getsize(file4)).encode())
        time.sleep(.3)
        client_socket2.send(file4.encode())
        with open(file4,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket2.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        print("server 2 done")
    except:
        print("Problem with Server 2")
    try:
        client_socket3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket3.connect((server_name,server_port3))
        client_socket3.send(option.encode())
        time.sleep(.3)
        client_socket3.send(file_name.encode())
        time.sleep(.3)
        client_socket3.send(str(os.path.getsize(file5)).encode())
        time.sleep(.3)
        client_socket3.send(file5.encode())
        with open(file5,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket3.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        time.sleep(.3)
        client_socket3.send(str(os.path.getsize(file6)).encode())
        time.sleep(.3)
        client_socket3.send(file6.encode())
        with open(file6,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket3.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        print("server 3 done")
    except:
        print("Problem with Server 3")
    try:
        client_socket4=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket4.connect((server_name,server_port4))
        client_socket4.send(option.encode())
        time.sleep(.3)
        client_socket4.send(file_name.encode())
        time.sleep(.3)
        client_socket4.send(str(os.path.getsize(file7)).encode())
        time.sleep(.3)
        client_socket4.send(file7.encode())
        with open(file7,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket4.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        time.sleep(.3)
        client_socket4.send(str(os.path.getsize(file8)).encode())
        time.sleep(.3)
        client_socket4.send(file8.encode())
        with open(file8,"rb") as sending_file:
            temp_file_buffer = sending_file.read(65000)
            while(temp_file_buffer):
                print("Transferring....")
                client_socket4.send(temp_file_buffer)
                time.sleep(1)
                temp_file_buffer=sending_file.read(65000)
        print("Transferring done")
        sending_file.close()
        print("server 4 done")
    except:
        print("Problem with Server 4")
    os.remove(file_name+".1")
    os.remove(file_name+".2")
    os.remove(file_name+".3")
    os.remove(file_name+".4")
    client_socket1.close()
    client_socket2.close()
    client_socket3.close()
    client_socket4.close()
    
def create_socket_get(option,file_name,server_name,server_port1, server_port2, server_port3, server_port4):
    mdhash = hashlib.md5(file_name.encode())
    x = int(mdhash.hexdigest(),16)%4
    files_received=[]
    if (x == 0):
        file1=file_name+".1"
        file2=file_name+".2"
        file3=file_name+".2"
        file4=file_name+".3"
        file5=file_name+".3"
        file6=file_name+".4"
        file7=file_name+".4"
        file8=file_name+".1"
    if (x == 1):
        file1=file_name+".4"
        file2=file_name+".1"
        file3=file_name+".1"
        file4=file_name+".2"
        file5=file_name+".2"
        file6=file_name+".3"
        file7=file_name+".3"
        file8=file_name+".4"
    if (x == 2):
        file1=file_name+".3"
        file2=file_name+".4"
        file3=file_name+".4"
        file4=file_name+".1"
        file5=file_name+".1"
        file6=file_name+".2"
        file7=file_name+".2"
        file8=file_name+".3"
    if (x == 3):
        file1=file_name+".2"
        file2=file_name+".3"
        file3=file_name+".3"
        file4=file_name+".4"
        file5=file_name+".4"
        file6=file_name+".1"
        file7=file_name+".1"
        file8=file_name+".2"    
    try:
        client_socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket1.connect((server_name,server_port1))
        client_socket1.send(option.encode())
        time.sleep(.3)
        client_socket1.send(file1.encode())
        file_exists=client_socket1.recv(2048)
        file_exists=file_exists.decode()
        if file_exists == "Yes":
            file_size=client_socket1.recv(2048)
            file_size=int(file_size.decode())
            print("File "+file1+" about to download")
            size=0
            with open(file1,"wb") as fh:
                while(size<=file_size):
                    file_content=client_socket1.recv(min(file_size - size,65000))
                    fh.write(file_content)
                    print("Receiving....")
                    size+=65000
            files_received.append(file1)
            fh.close()
            print("File "+file1+" transfer done successfully")
        client_socket1.close()
        time.sleep(2)
        client_socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket1.connect((server_name,server_port1))
        client_socket1.send(option.encode())
        time.sleep(.3)
        client_socket1.send(file2.encode())
        file_exists=client_socket1.recv(2048)
        file_exists=file_exists.decode()
        if file_exists == "Yes":
            file_size=client_socket1.recv(2048)
            file_size=int(file_size.decode())
            print("File "+file2+" about to download")
            size=0
            with open(file2,"wb") as fh:
                while(size<=file_size):
                    file_content=client_socket1.recv(min(file_size - size,65000))
                    fh.write(file_content)
                    print("Receiving....")
                    size+=65000
            files_received.append(file2)
            fh.close()
            print("File "+file2+" transfer done successfully")
        else:
            print("No file received from Server 1")
        client_socket1.close()
    except:
        print("Problem with Server1")
    try:
        if file3 not in files_received:
            client_socket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket2.connect((server_name,server_port2))
            client_socket2.send(option.encode())
            time.sleep(.3)
            client_socket2.send(file3.encode())
            file_exists=client_socket2.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket2.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file3+" about to download")
                size=0
                with open(file3,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket2.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file3)      
                fh.close()
                print("File "+file3+" transfer done successfully")
            client_socket2.close()
        if file4 not in files_received:    
            client_socket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket2.connect((server_name,server_port2))
            client_socket2.send(option.encode())
            time.sleep(.3)
            client_socket2.send(file4.encode())
            file_exists=client_socket2.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket2.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file4+" about to download")
                size=0
                with open(file4,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket2.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file4)
                fh.close()
                print("File "+file4+" transfer done successfully")
                client_socket2.close()
        else:
            print("No file received from Server 2")
    except:
        print("Problem with Server2")
    try:
        if file5 not in files_received:
            client_socket3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket3.connect((server_name,server_port3))
            client_socket3.send(option.encode())
            time.sleep(.3)
            client_socket3.send(file5.encode())
            file_exists=client_socket3.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket3.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file5+" about to download")
                size=0
                with open(file5,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket3.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file5)
                fh.close()
                print("File "+file5+" transfer done successfully")
            client_socket3.close()
        if file6 not in files_received:
            client_socket3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket3.connect((server_name,server_port3))
            client_socket3.send(option.encode())
            time.sleep(.3)
            client_socket3.send(file6.encode())
            file_exists=client_socket3.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket3.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file6+" about to download")
                size=0
                with open(file6,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket3.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file6)
                fh.close()
                print("File "+file6+" transfer done successfully")
                client_socket3.close()
        else:
            print("No file received from Server 3")
    except:
        print("Problem with Server3")    
    try:
        if file7 not in files_received:
            client_socket4=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket4.connect((server_name,server_port4))
            client_socket4.send(option.encode())
            time.sleep(.3)
            client_socket4.send(file7.encode())
            file_exists=client_socket4.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket4.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file7+" about to download")
                size=0
                with open(file7,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket4.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file7)
                fh.close()
                print("File "+file7+" transfer done successfully")
            client_socket4.close()
        if file8 not in files_received:
            client_socket4=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket4.connect((server_name,server_port4))
            client_socket4.send(option.encode())
            time.sleep(.3)
            client_socket4.send(file8.encode())
            file_exists=client_socket4.recv(2048)
            file_exists=file_exists.decode()
            if file_exists == "Yes":
                file_size=client_socket4.recv(2048)
                file_size=int(file_size.decode())
                print("File "+file8+" about to download")
                size=0
                with open(file8,"wb") as fh:
                    while(size<=file_size):
                        file_content=client_socket4.recv(min(file_size - size,65000))
                        fh.write(file_content)
                        print("Receiving....")
                        size+=65000
                files_received.append(file8)
                fh.close()
                print("File "+file8+" transfer done successfully")
                client_socket4.close()
        else:
            print("No file received from Server 4")
    except:
        print("Problem with Server 4")    
    if file_name+".1" not in files_received or file_name+".2" not in files_received or file_name+".3" not in files_received or file_name+".4" not in files_received:
        print("The files recevied are:",files_received)
        return
    with open(file_name,"wb") as file_full:
        with open(file_name+".1","rb") as f1:
            size=0
            file_size=os.path.getsize(file_name+".1")
            while(size<=file_size):
                file_full.write(f1.read(min(file_size - size,65000)))
                size+=65000
        f1.close()
        with open(file_name+".2","rb") as f2:
            size=0
            file_size=os.path.getsize(file_name+".2")
            while(size<=file_size):
                file_full.write(f2.read(min(file_size - size,65000)))
                size+=65000
        f2.close()
        with open(file_name+".3","rb") as f3:
            size=0
            file_size=os.path.getsize(file_name+".3")        
            while(size<=file_size):
                file_full.write(f3.read(min(file_size - size,65000)))
                size+=65000
        f3.close()
        with open(file_name+".4","rb") as f4:
            size=0
            file_size=os.path.getsize(file_name+".4")
            while(size<=file_size):
                file_full.write(f4.read(min(file_size - size,65000)))
                size+=65000
        f4.close()
        
def create_socket_list_or_exit(option,server_name,server_port1, server_port2, server_port3, server_port4):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((server_name,server_port1))
    if option == "list":
        client_socket.send(option.encode())
        num_of_file_names_sent=client_socket.recv(2048)
        num_of_file_names_sent=num_of_file_names_sent.decode()
        print("Number".ljust(12)+"FileName")
        for i in range (0,int(num_of_file_names_sent)):
            file_names=client_socket.recv(2048)
            file_names=file_names.decode()
            print((str(i+1)+". ").ljust(12)+str(file_names)) 
    else:
        if option == "exit":
            print("The connection will be closed")
            client_socket.close()
        else:
            print("invalid entry")
    client_socket.close()
    
    
if __name__=='__main__':
        server_name= '127.0.0.1'
        server_port1= 10001
        server_port2= 10002
        server_port3= 10003
        server_port4= 10004
        command=input("Please enter a command in one of the following formats:\nget <filename> \nput <filename>\nlist\nexit\n")
        arg_command=[]
        arg_command=command.split()
        option=arg_command[0]
        if (option == "get"):
            file_name = arg_command[1]
            file_name_contd = len(arg_command)- 2
            while(file_name_contd):
                file_name += " " + arg_command[-(file_name_contd)]
                file_name_contd -= 1
            create_socket_get(option,file_name,server_name, server_port1, server_port2, server_port3, server_port4)
        elif (option=="put"):
            file_name = arg_command[1]
            file_name_contd = len(arg_command)- 2
            while(file_name_contd):
                file_name += " " + arg_command[-(file_name_contd)]
                file_name_contd -= 1
            create_socket_put(option,file_name,server_name, server_port1, server_port2, server_port3, server_port4)
        
        elif (option == "list") or (option=="exit"):
            create_socket_list_or_exit(option,server_name, server_port1, server_port2, server_port3, server_port4)
        else:
            print("Invalid input")
quit()