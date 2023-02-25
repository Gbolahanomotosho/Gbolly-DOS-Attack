#!/usr/bin/env python3
import os
import time
import sys
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



Gbolly =""" 
         \033[1;96m _____   ____   _____            _   _             _                 
         \033[1;96m|  __ \ / __ \ / ____|          | | | |           | |             
         \033[1;96m| |  | | |  | | (___ ______ __ _| |_| |_ __ _  ___| | __           
         \033[1;96m| |  | | |  | |\___ |______/ _` | __| __/ _` |/ __| |/ /           
         \033[1;96m| |__| | |__| |____) |    | (_| | |_| || (_| | (__|   <            
         \033[1;96m|_____/ \____/|_____/      \__,_|\__|\__\__,_|\___|_|\_\           
                                                                              
         \033[1;91mCoded by Omotosho Gbolahan Hammed                                
         \033[1;92mFacebook: Omotosho Gbolahan                                   
         \033[1;93mInstagram: _lord_of_hacker                                   
         \033[1;94mWhatsapp: 08022648626                                       
         \033[1;95mGithub: https://github.com/Gbolahanomotosho                 
         \033[1;96mI wont be resposible for illegal use                       
                                                                              
                                                                             
         \033[1;91mThis is a simple but powerful Dos script which shut down your      
         \033[1;91mvictim website, Device (mobile phone, pc, printer, smart tv) and   
         \033[1;91myour victim wifi network.........                                 
                                                                              
                                                                              
          \033[1;97mThis script uses UDP attack method to shut down your victim      
          \033[1;97mwebsite, Device and wifi network.......                           
                                                                              
                                                                              
                                                                             
         \033[1;96mPls use wisely, i wont be responsible for illegal use              
         \033[1;96mDont use it for revenge                                           
         \033[1;96mRemember DoS someone website or device is a very big crime         
         \033[1;96mwhich land you in jail or make you pay a big fine                  
         \033[1;96mfor educational purpose only....................                   
                                                                             
                                                                             
         \033[1;93mThis tools is very simple and easy to use                          
         \033[1;93mEven your grandmother can use this tools...............            
                                                                              
                                                                              
         \033[1;92mTo use this tools first scan for your victim website or device     
         \033[1;92mip address.............................                            


                                                                             
         \033[1;96m[1] DOS Attack 
         \033[1;93m[2] DDOS Attack Detection
         \033[1;97m[3] Get website ip address
         \033[1;94m[4] Get device ip address
                                              
         \033[1;95m[5] Report a bug or contact the developer                                                          

"""






for i in Gbolly:
        time.sleep(0.01)
        print(i, end='',flush=True)





try:
        menu = int(input("\033[1;91mEnter an option: "))
except ValueError:
        print("\033[1;92mEnter the correct number")
        time.sleep(3)
        loop()
if menu == 1:


    if os.path.exists('Gbolly-dos.py'):


        os.system("python3 Gbolly-dos.py")



elif menu == 2:


    if os.path.exists('DDos-detection.py'):


        os.system("python3 DDos-detection.py")





elif menu == 3:


    if os.path.exists('get-web-ip.py'):


        os.system("python3 get-web-ip.py")






elif menu == 4:


    if os.path.exists('grab-device-ip-address.py'):


        os.system("python3 grab-device-ip-address.py")






elif menu == 5:


    os.system("xdg-open https://facebook.com/gbolahan.omotosho.73")
    time.sleep(2)
    os.system("xdg-open https://wa.me/08022648626")
    time.sleep(2)
    os.system("xdg-open https://github.com/Gbolahanomotosho")














