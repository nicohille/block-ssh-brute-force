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
            counter+=1

    if counter>=3:
        print("Het Ip addres", a ,"komt", counter ,"keer voor, het wordt nu geblokkeerd")
        fwblock.block_ip(a)       
        
