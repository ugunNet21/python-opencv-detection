#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import srp, Ether, ARP, conf

def scan(interface='wlan0', ips='192.168.1.0/24'):
    """Scan the network for devices using ARP."""
    try:
        print('[*] Starting network scan...')
        conf.verb = 0  # Hide Scapy verbose output
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(pdst=ips)
        answer, _ = srp(ether/arp, timeout=2, iface=interface, inter=0.1)

        print('[*] Devices found:')
        for sent, received in answer:
            print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

    except KeyboardInterrupt:
        print('[*] Scan interrupted by user.')
        sys.exit(1)