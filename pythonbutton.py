#!/usr/bin/python2

#-------------------------------------------------------------------------------
# Name:         Controlling Hue Lights With Raspberry Pi & a Button
#
# Details &
# instructions: forthcoming
#
# Author:       shatteredhaven
# Inspired by:  O'Reilly Raspberry Pi example with a push button switch
#               found here: http://razzpisampler.oreilly.com/ch07.html
#
# Created:      March 2015
# 
#-------------------------------------------------------------------------------

import sys; sys.path.append("/home/pi/phue-master")
import RPi.GPIO as GPIO
import time
import urllib2
from xml.dom import minidom

from phue import Bridge

# IP of Hue Bridge. IP address should be changed to your Brige's IP address
b = Bridge('192.168.0.161')

GPIO.setmode(GPIO.BCM)

# use pin 18 on GPIO of Raspberry Pi
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        #check if the light is on. If on, turn off.
        #note - you will need to change the light # to correspond to your bulb #
        if b.get_light(1,'on') == True:                                    
            b.set_light(1,'on', False)

        #if it is off, turn the light on
        else:                               
            b.set_light(1,'on', True)
            b.set_light(1, 'bri', 20)
        time.sleep(0.2)
