#!/usr/bin/python3

import fwblock
import sys,getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   verbose=False
   try:
      opts, args = getopt.getopt(argv,"h:nv",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('Error gelieve een optie te kiezen tussen -h -v of -n')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("Dit is een help functie van getopt, gelieve Nico Hillé te contacteren op 0488821104")
         sys.exit()
      elif opt in "-v":
         with open("sshdlog","r") as lf:
            logfile=lf.readlines()
            for line in logfile:
                if "invalid user" in line: outputUsers.append(line)

            for line in outputUsers:
                listLines=line.split(" ")
                ip=listLines[-4]
                ipaddresses.append(ip)

            lf.close()
            UniqueIps=set(ipaddresses)

            for a in UniqueIps:
                counter=0
                for b in ipaddresses:
                    if a==b:
                        counter+=1

                if counter>=3:
                    print("Het Ip addres", a ,"komt", counter ,"keer voor, het wordt nu geblokkeerd")
                    fwblock.block_ip(a)       
      elif opt in ("-n", "--ofile"):
         with open("sshdlog","r") as lf:
            logfile=lf.readlines()
            for line in logfile:
                if "invalid user" in line: outputUsers.append(line)

            for line in outputUsers:
                listLines=line.split(" ")
                ip=listLines[-4]
                ipaddresses.append(ip)

            lf.close()
            UniqueIps=set(ipaddresses)

            for a in UniqueIps:
                counter=0
                for b in ipaddresses:
                    if a==b:
                        counter+=1

                if counter>=3:
                    print("Het Ip addres", a ,"komt", counter ,"keer voor, het wordt nu geblokkeerd")
                    

outputUsers = []
ipaddresses = []


if __name__ == "__main__":
   main(sys.argv[1:])

outputUsers = []
ipaddresses = []

with open("sshdlog","r") as lf:
    logfile=lf.readlines()
for line in logfile:
    if "invalid user" in line: outputUsers.append(line)

for line in outputUsers:
    listLines=line.split(" ")
    ip=listLines[-4]
    ipaddresses.append(ip)

lf.close()
UniqueIps=set(ipaddresses)

for a in UniqueIps:
    counter=0
    for b in ipaddresses:
        if a==b:
            counter+=1

    if counter>=3:
        print("Het Ip addres", a ,"komt", counter ,"keer voor, het wordt nu geblokkeerd")
        fwblock.block_ip(a)       
        
       


        

