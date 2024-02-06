import os
import socket
import sys
import struct
from IP_decoder import IP


class ICMP:
    def __init__(self,buff=None):
        header = struct.unpack("<BBHHH",buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]
    
    def sniffs(host):
        
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol  = socket.IPPROTO_ICMP
        
        sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
        sniffer.bind((host,0))
        sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

        if(os.name == 'nt'):
            sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
        
        try:
            while True:
                recv_buff = sniffer.recvfrom(65535)[0]
                ip_header = IP(recv_buff[0:20])
                print('[*]Protocol: %s  %s -> %s' %(ip_header.protocol,ip_header.src_address,ip_header.dst_address))
                #if its icmp we want
                if ip_header.protocol == "ICMP":
                    print('[*]ver:%s  hlen:%s ttl:%s' %(ip_header.ver,ip_header.hlen,ip_header.ttl))
                    print("************ICMP Header*************")
                    offset = ip_header.hlen*4
                    buff = recv_buff[offset:offset+8]
                    #create icmp structure
                    icmp_header = ICMP(buff)
                    print('[*] code: %s  type: %s\n' %(icmp_header.code,icmp_header.type))
        except KeyboardInterrupt:
            if os.name=='nt':
                sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
            sys.exit()


if __name__=="__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = "10.0.2.15"
    ICMP.sniffs(host)
