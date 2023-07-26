#!/bin/python3

#scanner.py - terrible port sccanner

import sys
import socket
from datetime import datetime

#target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4

else:
    print("Wrong syntax.")
    print("To use this tool use: python3 cyberscan.py <ip>")


#banner
print("-" * 50)
print("      |___________________________________")
print("|-----|- - -|''''|''''|''''|''''|''''|'##\|__")
print("|- -  |  cc 6    5    4    3    2    1 ### __]==----------------------")
print("|-----|________________________________##/|")
print("      |        CYBERMEDIC SCANNER        ")
print("               1-1000 ports only ")
print("               HEAD DOWN, HOODIE UP         ")
print("-" * 50)
print("CYBERMEDIC is scanning the target of: "+target)
print("Time started at: "+str(datetime.now()))
print("-" * 50)

try: 
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Activity found on Port {}" .format(port))
        s.close()

except KeyboardInterrupt:
    print("Stopping your scan.")
    sys.exit()

except socket.gaierror:
    print("no host found for CYBERMEDIC to scan.")
    sys.exit()

except socket.error:
    print("CYBERMEDIC found no server.")