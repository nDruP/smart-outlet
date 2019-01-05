#This file is executed on every boot (including wake boot from deepsleep)

import gc
import webrepl
import network
import time

webrepl.start()
gc.collect()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
"""
Load passwords.txt into a list
"""
try:
    with open("passwords.txt") as f:
        connections = f.readlines()
except OSError:
    print("No passwords.txt file!")
    connections = []

"""
Parse through list from passwords.txt, then connect to network
"""
for connection in connections:
    station, password = connection.strip('\n').split(':*:')
    
    print('Connecting to {}:*:{}'.format(station, password))
    for i in range(6):
        if i%3 == 0:
            sta_if.connect(station, password)
        if sta_if.isconnected():
            break
        time.sleep(2.5)
        print(sta_if.isconnected())

    """
    Set a static ip for device.
    """
    if sta_if.isconnected():
        ip, subnet, gateway, dns = sta_if.ifconfig()
        index = [pos for pos, char in enumerate(ip) if char == '.'][-1]
        sta_if.ifconfig((ip[0:(index+1)]+'52', subnet, gateway, dns))
        print("localhost address is: {}".format(sta_if.ifconfig()[0]))
        break
    else:
        print("Connection could not be made to {}\n").format(station)

print("Access the webrepl for this device at: {}:8266".format(sta_if.ifconfig()[0]))
