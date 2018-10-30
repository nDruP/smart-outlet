# smart-outlet

Micropython code for esp8266. 
Following this guide: http://www.circuitbasics.com/build-an-arduino-controlled-power-outlet/

Creates a simple webpage to turn the outlet on/off. The webpage is accessed through the arduino's localhost:8080

This assumes you have an arduino that runs Micropython and a way to add boot.py, main.py, and passwords.txt\* to it.

\*passwords.txt is a text file containing ssid/password pairs separated by ":\*:" you can change the separator in boot.py

E.g. NetworkSSID:\*:P@ssword1

Motivation for making this: I have a loft bed and a lamp underneath. If I want to turn it on/off I have to crawl out of bed.
Now I don't have to crawl out of bed to turn it on/off. wooooo.
