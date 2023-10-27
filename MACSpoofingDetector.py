#!/usr/bin/env python3
from scapy.all import Dot11, sniff
import argparse
import sys
import os

__author__  = 'Regis SENET'
__email__   = 'regis.senet@bssi.fr'
__git__     = 'https://github.com/rsenet/MACSpoofingDetector'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Access Point MAC Spoofing Detector"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--bssid', help="Specify targeted Access Point MAC Address (BSSID)")
arg_parser.add_argument('--int', help="Specify Monitor Interface")
u_args = arg_parser.parse_args()

# Get variable
bssid = u_args.bssid
interface = u_args.int
access_point = ""

try:
    if bssid and interface:
        def PacketHandler(packet):
            global access_point
    
            if packet.haslayer(Dot11):
                # Beacon packets
                if packet.type == 0 and packet.subtype == 8:
                    if packet.addr3 == bssid:
                        if access_point == "":
                            print("Access Point MAC: %s with SSID %s" % (packet.addr3, packet.info))
                            access_point = packet.addr3

                        else:
                            print(packet.mac_sqn)
                        

        sniff(iface=interface, prn = PacketHandler)

    else:
        print("[x] Error! Missing attributes ('bssid' and 'int' are mandatory)")

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
