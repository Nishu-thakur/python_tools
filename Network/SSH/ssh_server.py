import paramiko
import os
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD,'text_rsa.key'))

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
    
    def check_channel_request(self,kind,chanid):
        if(kind=='session'):
            return paramiko.OPEN_SUCCEEDED
        
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self,username,password):
        if(username=='Nimesh' and password == 'lalu'):
            return paramiko.AUTH_SUCCESSFUL

if __name__=="__main__":
    server_ip,server_port = sys.argv[1],sys.argv[2]
    server = server_ip
    port = int(server_port)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind((server,port))
        sock.listen(5)
        print('[+] Listening for connection...')
        client,addr = sock.accept()
    except Exception as e:
        print('[+] Listen failed:',str(e))
        sys.exit()
    else:
        print('[+] Got a connection:',client,addr)
    
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)

    chan = bhSession.accept(20)
    if chan is None:
        print('***no channel')
        sys.exit(1)
    
    print('[+] Authenicated')
    print(chan.recv(1024))
    chan.send('Welcome to bh__ssh')
    try:
        while True:
            command = input("Enter comamnd:")
            if command != "exit":
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('existing')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()


    
