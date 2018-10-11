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
    
    for i in range(6):
        if i%3 == 0:
            sta_if.connect(station, password)
        if sta_if.isconnected():
            break
        time.sleep(3)
        print(sta_if.isconnected())
        
    if sta_if.isconnected():
        print("localhost address is: {}".format(sta_if.ifconfig()[0]))
        break
    else:
        print("Connection could not be made.\n")            
