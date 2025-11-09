<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/qashqaw.png">
</div>

# Lego Millinium Falcon with ESP-32
Building The Legostarwars Ultimate Collection - Millinium Falcon with ESP32 Controller adding lights to the Collectio. (Hopefully this isn't last LEGO project i do)
<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/build/squreview.jpg">
</div>

A long time ago, I found and bought the package: Lego StarWars Ultimate Collection Millinium Falcon V.2 - and found it again, decided to build the Falcon, and along the way the idea of installing ligth.<br>
The Actual build time for the Millinum Falcon was 36hours and the hours in planning , configuring and setting up the ESP32-S3 Wroom controller was a longer process - and in this case - using a Pythonscript for switching the lights on and off. My Idea is making a glass shelf hanging this is a corner in a bedroom.

<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/build/Lego_Boxset.png">
</div>

The package contains 4 boxes, containing several bags with the numbers 1-18, which is the different levels you need to go through while building the Millinium Falcon. I did not lock any of the top plates, so I could create the light within tha Falcon. I had some lovely times spent with my boy, collecting the Falcon, and starting the little idea of building this massive Starship. The Process are documated wth fotos within [images/build](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main/images/build) the folder.

When its on - it'll switch between 5scenes created in the python scripts

    1. Turning the light on in cockpitt
    2. Fire the lasercanon above
    3. Fire the lasercanon below
    4. Turning the light on in the Docking bridge
    5. Flying

Between each scenes, is a random process, and the sleep time is a function called timeout that choose a number between 30secs to 15minutes. So starting the the script will do: 

    * Choose a number between 1-5 (Choosing which scene to run.)
    * Start the scene
    * Call Timeout - wait the seconds
    * Stop the scene
    * Call Timeout - wait before starting the next scene

The firing scenes also choose a number between 100-300 for the number of shot to fire - and call a random int between 100-700, which is tyhe time before the next shot in millisecs.

<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/lights/Firing_above.gif">
</div>

# Starting With Pythom (or Micro-python)
I know python from work, so needed to find out what the ESP32-S3 Wroon Connector can do. Lets take a look at the python file created for this Falcon. 

```
# !/usr/bin/python
# This python script is for
# create light in the
# Millinium Falcon in Lego
##########################
# Importing our libraries
# used in this script
from random import randint
from machine import Pin
import time
import network
from neopixel import NeoPixel

# Initialize Pins
#######################
## Cockpitt - 3 lights
led1=Pin(1,Pin.OUT)
## Above - 4 lights
led6=Pin(6,Pin.OUT)
led7=Pin(7,Pin.OUT)
led15=Pin(15,Pin.OUT)
led16=Pin(16,Pin.OUT)
## Below - 4 lights
led21=Pin(21,Pin.OUT)
led45=Pin(45,Pin.OUT)
led47=Pin(47,Pin.OUT)
led48=Pin(48,Pin.OUT)
# Flying - 6 lights
nppin=Pin(48)
num_pixels=32
np = NeoPixel(nppin, num_pixels)

# Open bridge - 3
led8=Pin(8,Pin.OUT)

# Done setting Pins
#######################
# Setting the boolean
millinium = bool()
#######################
```