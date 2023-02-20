#!/bin/env python3

import pyfiglet
import sys
import socket
from datetime import datetime
print("""
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│,-----.                 ,--.          ,------.                 ,--.      │
│|  |) /_  ,--,--. ,---. `--' ,---.    |  .--. ' ,---. ,--.--.,-'  '-.    │
│|  .-.  \' ,-.  |(  .-' ,--.| .--'     |  '--' || .-. ||  .--''-.  .-'    │
│|  '--' /\ '-'  |.-'  `)|  |\ `--.    |  | --' ' '-' '|  |     |  |      │
│`------'  `--`--'`----' `--' `---'    `--'      `---' `--'     `--'      │
│                                                                         │
│                                                                         │
│ ,---.                                                                   │
│'   .-'  ,---. ,--,--.,--,--, ,--,--,  ,---. ,--.--.                     │
│`.  `-. | .--'' ,-.  ||      \|      \| .-. :|  .--'                     │
│.-'    |\ `--.\ '-'  ||  ||  ||  ||  |\   --.|  |                        │
│`-----'  `---' `--`--'`--''--'`--''--' `----'`--'                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
  .........................Made By SnowyYT07..............................
""")
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: portscan.py <target>")
    sys.exit()

print("-#" * 25)
print("Target: " + target)
print("Scanned at: " +str(datetime.now()))
print("#-" * 25)

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n EXIT!!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()
