# distributed_file_system

This distributed file system consists of 4 distributed file servers and a single client. The file system command line can support multiple functionalities like PUT, GET, LIST and EXIT. It supports redundancy and uses Socket Programming in Python. Since the socket is TCP, the system is reliable.

PUT : The client divides the file into 4 quaters and stores it in a redundant fashion on 2 servers. The choice of 2 servers is made based on the hash value obtained by hashing the file name. This lets the file system to be available even if one or more servers are not up.

Efficient GET : The client knows that the DFS has redundancy and does not contact all the servers if it can get the 4 different quarters of the file by contacting less than 4 servers. The combination logic happens in the client to reproduce the complete file.

LIST: This outputs the list of files stored on distributed file servers including the redundant ones.

EXIT : This exits the cli and closes the socket connection with all the servers.
