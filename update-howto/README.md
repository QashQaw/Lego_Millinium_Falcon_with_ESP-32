<div align="center">
    <img src="https://github.com/QashQaw/Lego_Millinium_Falcon_with_ESP-32/blob/main/images/qashqaw.png">
</div>

# Flashing the firmware on the ESP32-S3
Requirements:

    (Python min 3.11)[https://www.python.org/downloads/]
    Editor (Thony)[https://thonny.org/]

The editor is needed for communication with the controller - and for flashing the firmware on the controller

## Firmware for the ESP32-S3 Controller
Download the latest firmware for the controller from this link (Firmware for ESP32-S3)[https://micropython.org/download/ESP32_GENERIC_S3/] <br>
After Download - move the firmware to a new folder. and then add the file for your os (Located in thes folder including the folder esptools.)

Inside that folder - run the needed script - depending on your OS. For Linux the command is: 

    python linux.py

The same command exist for Windows and Mac - for all the same is required - pyhton <script>.<br>
you'll get a lot of output while erasing the existing firmware, then uploading new firmware and then burn it to the controller. In the end, the output tells whathappens, if goes well or not.

The script for linux look like this, where you need to change the name of the firmware:

    import os
    import sys
    import time

    os.system("python3 esptool/esptool.py --chip esp32s3  erase_flash")

    os.system("python3 esptool/esptool.py --chip esp32s3 --baud 2000000 write_flash -z 0 GENERIC_S3-20250415-v1.25.0.bin")

