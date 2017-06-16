#!/usr/bin/python

import bluetooth
import time

while True:
    print("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))

    result = bluetooth.lookup_name('63:FF:AA:A3:08:BC', timeout=5)
    if (result != None):
        print("John: in")
    else:
        print("John: out")

    result = bluetooth.lookup_name('00:1D:D9:F9:79:43', timeout=5)
    if (result != None):
        print("Paul: in")
    else:
        print("Paul: out")

    time.sleep(60)

