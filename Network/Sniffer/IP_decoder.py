import socket
import os
import struct
import sys
import ipaddress

class IP:
    def __init__(self,buff=None):
        header = struct.unpack("<BBHHHBBH4s4s",buff)
        self.ver = header[0] >> 4
        self.hlen = header[0] & 0xF
        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        self.protocol_dict = {1:"ICMP",6:"TCP",17:"UDP"}
        try:
            self.protocol = self.protocol_dict[self.protocol_num]
        except Exception as e:
            print("%s NO PROTOCOL FOR %s" %(e,self.protocol_num))

    def sniff(host):
        if os.name =='nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP
        
        sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
        sniffer.bind((host,0))
        #capture a ip packet
        sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
        
        try:
            while True:
                #read a packet
                raw_buffer = sniffer.recvfrom(65535)[0]
                #create a ip buffer form first 20 bytes of rawbuffer
                IP_header = IP(raw_buffer[0:20])
                #print detected ip and protocol
                print('[*] Protocol: %s  %s -> %s' %(IP_header.protocol,IP_header.src_address,IP_header.dst_address))
        except KeyboardInterrupt:
            if os.name=='nt':
                sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
            sys.exit()

if __name__=="__main__":
    if(len(sys.argv)==2):
        host = sys.argv[1]
    else:
        host = '10.0.2.15'
    IP.sniff(host)
