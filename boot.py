#This file is executed on every boot (including wake boot from deepsleep)


import gc
import webrepl

webrepl.start()
gc.collect()

import network
import time

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

try:
    with open("passwords.txt") as f:
        connections = f.readlines()
except OSError:
    print("No passwords.txt file!")
    connections = []

for connection in connections:
    station, password = connection.strip('\n').split(':*:')
    print('Connecting to {}:*:{}'.format(station, password))
    
    for i in range(10):
        if i%3 == 0:
            sta_if.connect(station, password)
        print(sta_if.isconnected())
        if sta_if.isconnected():
            break
        time.sleep(3)
        
    if sta_if.isconnected():
        break
    else:
        print("Connection could not be made.\n")            
            
if sta_if.isconnected():
    ap_if.active(False)
    print("Connected as: {}".format(sta_if.ifconfig()[0]))
