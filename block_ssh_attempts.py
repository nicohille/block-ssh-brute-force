#!/usr/bin/python3

import fwblock
import sys,getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   verbose=False
   try:
      opts, args = getopt.getopt(argv,"hnv",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('Error gelieve een optie te kiezen tussen -h -v of -n')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("Welkom bij de helpfunctie. Dit is een script die IP adressen van invalid users gaat blokkeren indien ze meermals voorkomen. Gebruik command line optie -n  om elke geblokeerde ip adres te zien. Optie -n zal de script inlezen zonder block_ip op te roepen." ")
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

            
                    

outputUsers = []
ipaddresses = []


if __name__ == "__main__":
   main(sys.argv[1:])

outputUsers = []
ipaddresses = []


        
       


        

