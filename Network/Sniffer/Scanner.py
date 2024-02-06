from IP_decoder import IP
from Icmp_decoder import ICMP
import os
import socket
import ipaddress
import sys
import threading

#subnet to target
SUBNET = '192.168.0.0/24'
#magic string we cheak for ICMP response for
MESSAGE = "="

def udp_sender():
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE,'utf8'),(str(ip),65212))

class Scanner:
    def __init__(self,HOST):
        self.host = HOST
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP
        
        self.sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
        self.sniffer.bind((HOST,0))
        self.sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

        if os.name == 'nt':
            self.sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
        
    
    def sniff(self):
        host_up = set([f'{str(self.host)}*'])
        try:
            while True:
                #read a packet
                raw_buffer = self.sniffer.recvfrom(65535)[0]
                ip_header = IP(raw_buffer[0:20])
                print(ip_header.src_address)
                print((raw_buffer[len(raw_buffer)-len(MESSAGE):]))
                if(ip_header.protocol=='ICMP'):
                    offset = ip_header.hlen*4
                    buff = raw_buffer[offset:offset+8]
                    icmp_header = ICMP(buff)
                    if(icmp_header.type==3 and icmp_header.code==3):
                        if(ipaddress.ip_address(ip_header.src_address) in ipaddress.IPv4Network(SUBNET)):
                            #make sure it has our magic keyword
                            if(raw_buffer[len(raw_buffer)-len(MESSAGE):] == bytes(MESSAGE,'utf8')):
                                tgt = str(ip_header.src_address)
                                if tgt != self.host and tgt not in host_up:
                                    host_up.add(str(ip_header.src_address))
                                    print(f'Host_up:{str(tgt)}')
        # handle ctrl+C
        except KeyboardInterrupt:
            if os.name=='nt':
                self.sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
            print('User Interrupted\n')
            if host_up:
                print(f'\n\n Summary hosts up on  {SUBNET}')
            if self.host in host_up:
                print(f'{self.host}')
            print('')
            sys.exit()


if __name__=="__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '192.168.0.115'
    s = Scanner(host)
    t  = threading.Thread(target=udp_sender)
    t.start()

    s.sniff()

    






