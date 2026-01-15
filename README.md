<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/qashqaw.png">
</div>

# Table of Contents
1. [Lego Millinium Falcon with ESP-32](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#lego-millinium-falcon-with-esp-32)
2. [Assemble the the Millinium Falcon](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#assemble-the-millinium-falcon)
3. [The masterplan for the lights](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#the-masterplan-for-the-lights)
4. [Starting With Pythom (or Micro-python)](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#starting-with-pythom-or-micro-python)
    1. [timeout()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#timeout)
    2. [cockpit()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#cockpitt)
    3. [above() or below()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#above-and-below)
    4. [flying()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#flyin)
    5. [landing()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#landing)
    6. [main function()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main?tab=readme-ov-file#main-function)

## Lego Millinium Falcon with ESP-32
Building The Legostarwars Ultimate Collection - Millinium Falcon with ESP32 Controller adding lights to the Collectio. (Hopefully this isn't last LEGO project i do)

<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/build/Lego_Boxset.png">
</div>

A long time ago, I found and bought the package: Lego StarWars Ultimate Collection Millinium Falcon V.2 #75192- and found it again, decided to build the Falcon, and along the way the idea of installing ligth.<br>
The package contains 4 boxes, containing several bags with the numbers 1-18, which is the different levels you need to go through while building the Millinium Falcon. 
<br>
Then find a Micro-Controller to handle the light, and start planning on how to make my idea work, with different scenes to run each night in a corner. My Idea is making a glass shelf hanging this is a corner in a bedroom or livingroom to avoid the dust - having my HomeAssistent to power on the controller and then run using a Pythonscript for switching the lights on and off. 

## Assemble the Millinium Falcon 
The Actual build time for the Millinum Falcon was 36hours and the hours in planning, so while assembling the Falcon, the ideas of how to create the effects startet, and started to order the different parts needed for making my idea work in the end.


 I did not lock any of the top plates, so I could create the light within tha Falcon. I had some lovely times spent with my boy, collecting the Falcon, and starting the little idea of building this massive Starship. 
 <br>
 The building process are documated wth fotos within [images/build](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main/images/build) the folder. And also the different light setup in the [images/lights](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main/images/build). 

 <div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/build/squreview.jpg">
</div>

 ## The masterplan for the lights
 After looking around - I've ended up with the ESP32-S3-Wroom - as the controller for my project, so found one on Temu - and then here we go :-)
My different tries for this controller I've ended up through the process, with the solution of having a HomeAssistent Plugin to control when the lights is on and off. In HomeAssistent you can create an automation based on Sunset, for power on the ESP-controller and then autostart the python script. That way we can also set a fixed time to turn off the light again,

<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/HA_Automation.png">
</div>

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


Seperate
## Starting With Pythom (or Micro-python)
---
<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/lights/lights004.jpg">
</div>
For starting out with a new Controller, you'll properly need to flash the firmware, and prepare the ESP-Controller to autostart the pythonscript. This procedure is described in a seperate README.md here - https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main/update-howto.<br>
So why not use the HomeAssistent to create the different functions, which I'd looked at - but had some issues all along making t almost impossible to create the same functions on the same level as I can in a python code.

I know python from work, so needed to find out what the ESP32-S3 Wroon Connector can do. Lets take a look at the python file created for this Falcon. Starting the script with setting our parameters and  initialze the PINS etc 

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

First we'll import some different libraries, for setting all this up 

| Commands             | Usage |
| :------------------- | :-----------------|
| from random import randint| Use for create rondon int|
| from machine import Pin | Use for easy accessing Pins |
| import time | Use for sleep |
| from neopixel import NeoPixel| Use for using LED strips|

Next up is enabling the different PIN output we need, for having the lights/Pins turn on or off, and setting up NeoPixels, the number of LEDs there is on the strips.<br>
And finally setting the Millinium boolean as true. and the we are ready for starting the script. The first thing is our function timeout(), which is called between each functions called.

### timeout()
---
This function is a value, we'll use several times within the script. This function is called after each sccenes, providing a int - that it'll use for sleep. The value are sleep between 30secs to 15minutes, creating the natural pause between each scenes, and also used to a timer between light on and off in the functions. By creating a seperate functions, we can instead of setting the sleep again - we can just call out timeout(), and the execution is on hold while sleep.
```
#######################
## Different Time between execution
def timeout():
    wait = randint(30000, 900000)   
    time.sleep_ms(wait)

```

### cockpitt()
---
<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/lights/lights002.jpg">
</div>
This is a simple PIN light on and off, but having 3pins wired to the PIN1.out, giving the light inside the cockpitt. This is the same as the light inside the cargo room, connecting more light to the same PIN.out on the controller, which make this possible with the lights installed inside the Falcon.

1. Setting the light on in the cockpitt using PIN1 for lightning up 3white lights inside the cockpitt.
2. Then calling the timeout() 
3. before turning the light off again

```
## Cockpitt ligth turing
    # on the light 1 Pins
def cockpitt():
    # Turn on Pin
    led1.value(1)
    # Choosing the wait pause
    timeout()
    # Turn off Pin
    led1.value(0)
    print("Finished Cockpitt light")

```

### above() and below()
---
<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/lights/Firing_above.gif">
</div>

The 2 functions are the same, only difference is where the lasercanon are place and explained it'll do  the following: <br>
1. Setting the acount as 1 (the first shot)
2. Settings the amount of shots as a randint between 100 and 300.
3. Then if $acount is less that $shots - the firing sequenze continues.
4. if continuing, choosing a randint - for which PIN to light up as an shot from the lasercanon.
5. After each shot it'll sleep in 10millisec - then choosing a new randit between 100 and 700 millisecs for sleeping between shots
6. Then finally for each shots, it'll add one to the $acount - and then start checking if $acount is less than $shots

So this function is for creating the shooting scenes, from above or below the Falcon. For simulation the shot, we'll power on the LED and wait for 10 milliseconds before turning the LED off
```
#######################
## Shots above falcon
def above():
    # Setting the start count
    acount = 1
    # Setting the number of shots)
    shots = randint(100, 300)
    # Choosing the weapon to be fired 
    while (acount < shots):
        choice = randint(1,4)
        # Switch created for each Weapon(Pins)
        if choice == 1:
            led6.value(1)
            time.sleep_ms(10)
            led6.value(0)
            slt1 = randint(100,700)
            time.sleep_ms(slt1)
            acount = acount + 1
        elif choice == 2:
            led7.value(1)
            time.sleep_ms(10)
            led7.value(0)
            slt2 = randint(100,700)
            time.sleep_ms(slt2)
            acount = acount + 1
        elif choice == 3:
            led15.value(1)
            time.sleep_ms(10)
            led15.value(0)
            slt3 = randint(100,700)
            time.sleep_ms(slt3)
            acount = acount + 1
        elif choice == 4:
            led16.value(1)
            time.sleep_ms(10)
            led16.value(0)
            slt4 = randint(100,700)
            time.sleep_ms(slt4)
            acount = acount + 1
        else:
            print("no number was chosen" + choice)
            
    else:
        print("Finished firing above")

```

### flyin()
---
<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/lights/lights001.jpg">
</div>


For creating the flying effect - I found some small strips, small enough to be inside the tubes, that simulates the Falcon engine. <br>
The LED strips is 3mm width, and therefor I'd using these for simulating the blue light when the falcon flies. <br>

EDIT:  I'm thinking about developing some more effects when flying, the brightness should flicker, starting from withe light to flying in lightspeed in blue and perhaps some sound - but more to come about that!
The script will do when flying:
1. setting the color of the strips
2. write to activate the color on the strips
3. taking the [timeout()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#timeout)
4. then turing off the lights in LED strips. 

```
#######################
## Method for flying
def flying():
    # Starting the motors for flying - turns on LED
    for i in range(num_pixels):
        np[i] = (0, 0, 255)  # Blue
    np.write()
    # Choosing the wait pause
    timeout()
    # Turn off the LED
    for i in range(num_pixels):
        np[i] = (0, 0, 0)  # White
    np.write()
    print("Finished flying")

```

### landing()
---

The final function for now is ligtning up the lanfing bridge, which is open with personal on the ground in front.
```
#######################
##  Our Landing bridge
def landing():
    # Setting the Pins for ON
    led8.value(1)
    # Choosing the wait pause
    timeout()
    # Turns of Pins
    led8.value(0)
    print("Finished landingbridge")
```

### main function()
---

This main functions is a simple try-catch, where we controlling which function to call.
1. setting boolean as True
2. when valid(allways) we'll taking and randint between 1-5 which are the 5 different functions.
3. using a switch to choose between the functions
4. taking a [timeout()](https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/tree/main#timeout) before starting all over again 
```
#######################
# Controlling the LED
try:
    # Setting millinium bool to TRUE
    millinium = True
    
    # Then run the loop
    while millinium:
        # Setting a number and match against sequences
        num = randint(1,5)
        # Number 1 == Cockpitlight
        if num == 1:
            cockpitt()
            timeout()
        # Number 2 == Shots firing from above
        elif num == 2:
            above()
            timeout()
        # Number 3 == Shots firing from below
        elif num == 3:
            below()
            timeout()
        # Number 4 == Flying engine
        elif num == 4:
            flying()
            timeout()
        # Number 5 == Light in the landingbridge 
        elif num == 5:
            landing()
            timeout()
        else:
            print("No number is selected")            
except:
    print("Failure is total")
# EOF
```
This will make a choice depending on the random number - thats been drawn with the interger "num". and when finished executing the choice - it'll redrawing "num" and gets the next function to run.  