#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import network_scanner
import wifi_tester

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scan", action="store_true", help="Scan all IPs on this network")
    parser.add_argument("-t", "--test_wifi", help="Test passwords on a specific Wi-Fi network")
    args = parser.parse_args()

    if args.scan:
        network_scanner.scan()

    if args.test_wifi:
        # Load passwords from a file
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
        wifi_tester.start(args.test_wifi, passwords)

if __name__ == '__main__':
    main()