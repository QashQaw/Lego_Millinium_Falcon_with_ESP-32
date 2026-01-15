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

#######################
## Different Time between execution
def timeout():
    wait = randint(30000, 900000)   # Between 0,5 minute and up til 15minutes
    time.sleep_ms(wait)


 #######################
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

#######################
## Shots below Falcon
def below():
    # Setting the start count
    bcount = 1
    # Setting the number of shots)
    shots = randint(100, 300)
    # Choosing the weapon to be fired 
    while (bcount < shots):
        choice = randint(1,4)
        if choice == 1:
            led21.value(1)
            time.sleep_ms(10)
            led21.value(0)
            slt5 = randint(100,700)
            time.sleep_ms(slt5)
            bcount = bcount + 1
        elif choice == 2:
            led45.value(1)
            time.sleep_ms(10)
            led45.value(0)
            slt6 = randint(100,700)
            time.sleep_ms(slt6)
            bcount = bcount + 1
        elif choice == 3:
            led47.value(1)
            time.sleep_ms(10)
            led47.value(0)
            slt7 = randint(100,700)
            time.sleep_ms(slt7)
            bcount = bcount + 1
        elif choice == 4:
            led48.value(1)
            time.sleep_ms(10)
            led48.value(0)
            slt8 = randint(100,700)
            time.sleep_ms(slt8)
            bcount = bcount + 1
        else:
            print("no number was chosen" + choice)
            
    else:
        print("Finished firing below")

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

#######################
# Controlling the LED
try:
    # Setting millinium bool to TRUE
    # This could be done otherwise by clock,. I did a test with wifi - and starting wifi and use the clock to determine when the script should run.
    # But thenit'll be powered on during the day - using homeassistant it'll only be powered on during runtime.
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