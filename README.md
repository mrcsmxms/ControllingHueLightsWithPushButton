Controlling Hue Lights With a Push Button, Raspberry Pi & Python
==============
Use a Raspberry Pi, GPIO and a push switch to turn on and off a light connected to the Hue bridge. This will work with Philips Hue lights as well as any other lights that are compatible with the Hue bridge (ex. GE Link white LED bulbs).

Inspired by O'Reilly's Connecting a Push Switch tutorial (http://razzpisampler.oreilly.com/ch07.html)

**Overview:** 
Turn on and off a Hue-connected light remotely with a push switch wired to GPIO pin 18. 

The program can be run directly from the command line. If you would like to have the program run as a background process so you can disconnect SSH, you can do two things: 

Option 1 - Daemon Process Shell Script

The pythonbutton.sh file should be placed in /etc/init.d folder. The file indicates where the python script is located. In this example, the python script is located in directory /usr/local/bin/pythonbutton. This is a daemon script that can be stopped/started at the command line. 

Be sure to use dos2unix or something similar if you edit the file in Windows and you have difficulty running the script (Windows text editor may have added characters the Pi can't interpret). 

Template taken from (good directions here as well): http://blog.scphillips.com/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/

Option 2 - Cron Job & Shell Script
run a shell script on startup with cronjob.

Tutorial and templates taken from here: http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

**Contents:**
- pythonbutton.py - python script

Option 1
- pythonbutton.sh - shell script file for daemon process

Option 2
- crontab.txt - example cronjob text
-launcher.sh

**Requirements/Libraries Used:**
- GPIO Library (https://pypi.python.org/pypi/RPi.GPIO)
- Phue Library (https://github.com/studioimaginaire/phue)

**Materials Used**
- Rasberry Pi (model B)
- Miniature WiFi dongle (http://www.adafruit.com/products/814)
- one (1) push switch
- one (1) miniature breadboard
- two (2) jumper wires

