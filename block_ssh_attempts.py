#!/usr/bin/python3

import fwblock

logfile=open("sshdlog","r")

outputUsers = []
ipaddresses = []

for line in logfile.readlines():
    if "invalid user" in line: outputUsers.append(line)

for line in outputUsers:
    listLines=line.split(" ")
    ip=listLines[-4]
    ipaddresses.append(ip)

UniqueIps=set(ipaddresses)

for a in UniqueIps:
    counter=0
    for b in ipaddresses:
        if a==b:
            counter+=0

    if counter>=3:
        fwblock.block.ip(a)
        print("Het ip address" + a + "kwam" + counter + "keer voor en wordt geblokeerd")
