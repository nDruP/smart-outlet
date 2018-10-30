# Smart Outlet Micropython code.
Micropython code for esp8266.
Follow this guide for the hardware of this project: http://www.circuitbasics.com/build-an-arduino-controlled-power-outlet/

Creates a simple webpage to turn the outlet on/off. The webpage is accessed through the arduino's localhost:8080

## Installation
1. Flash your arduino to run Micropython
2. Add boot.py, main.py, and passwords.txt\* to it. This can be done using https://github.com/micropython/webrepl
3. Connect your arduino according to the circuitbasics.com guide above.

\*passwords.txt is a text file containing ssid/password pairs separated by `:*:` you can change the separator in boot.py

E.g. `NetworkSSID:\*:P@ssword1`

## Usage
1. Access the arduino's localhost:8080 in a standard web browser.
2. Click the switch.

Sidenote: Make sure your arduino stays plugged in... I recommend getting Female to Female Dupont wires instead of using a breadboard.

## Motivation
I have a loft bed and a lamp underneath. If I want to turn it on/off I have to crawl out of bed.
Now I don't have to crawl out of bed to turn it on/off. wooooo.
