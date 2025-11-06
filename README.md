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