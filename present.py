#!/usr/bin/python
#Insert devices addresses to be able to be detected without having needing the device to be "discoverable" 
#Queries the presence of surrounding bluetooth devices (Check if bluetooth is activated)

import bluetooth
import time

while True:
    print("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    #Saved address for specific users
    MAC_ADDRESSES = ['64:6C:B2:95:BD:3C', 'D8:1D:72:3C:B2:38', 'C8:14:79:91:33:E1']
    #Corresponding name for each mac address
    NAME = ['Nathan', 'Garrett', 'Rob']
    i = 0
    #Checks if mac address is present 
    for address in MAC_ADDRESSES:
        result = bluetooth.lookup_name(address, timeout=2)
        if (result != None):
            print(NAME[i], ": in")
        else:
            print(NAME[i], ": out")
        i += 1 
    #Pause for a minute
    time.sleep(60)

