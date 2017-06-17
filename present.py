#!/usr/bin/python
#Insert devices addresses to be able to be detected without needing the device to be "discoverable" 
#Queries the presence of surrounding bluetooth devices (Check if bluetooth is activated)
#Able to parse device information as long as bluetooth is enabled

import bluetooth
import time
import subprocess

while True:
    print("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    #Saved address for specific users
    MAC_ADDRESSES = ['64:6C:B2:95:BD:3C', 'D8:1D:72:3C:B2:38', 'C8:14:79:91:33:E1']
    #Corresponding name for each mac address
    NAME = ['Nathan', 'Garrett', 'Rob']
    i = 0
    print("Requesting information ...")
    print('-' * 60)
    #Checks if mac address is present 
    for address in MAC_ADDRESSES:
        result = bluetooth.lookup_name(address, timeout=2)
        print("Name:", NAME[i])
        if (result != None):
            
            output = subprocess.Popen(['sudo', 'hcitool', 'info', address], stdout=subprocess.PIPE)
            result = str(output.communicate())

            #Extract specific data fields from output
            BD_Address = result[result.find('BD Address') + 13:63]
            OUI_Company = result[result.find('OUI Company') + 13:result.find('Device Name') - 4]
            Device_Name = result[result.find('Device Name') + 13:result.find('LMP Version') -4]
            LMP_Version = result[result.find('LMP Version') + 13:result.find('Manufacturer') -4]
            Manufacturer = result[result.find('Manufacturer')+ 14:result.find('Features page 0') -4]

            print("BD Address:", BD_Address)
            print("OUI Company:", OUI_Company)
            print("Device Name:", Device_Name)
            print("LMP Version:", LMP_Version)
            print("Manufacturer:", Manufacturer)
        else:
            print(NAME[i], ": Device not connected")
        i += 1 
        if(i != len(NAME)):
            print('-' * 60)
    print('=' * 60)
    #Pause for 10 seconds to prevent flooding 
    time.sleep(10)

