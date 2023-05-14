'''
Author1: Alexandru Constantin
Author2: <Insert Name Here>

Date: May 2023

REQUIREMENTS: 
* Adafruit_CircuitPython_HID: https://github.com/adafruit/Adafruit_CircuitPython_HID

The following program runs on the Raspberry Pi Pico and allows the mapping of keyboard shortcuts to a single button on the Maker Pi Pico.
'''

import time
import board
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Saving the PINS of the 3 buttons
btn1_pin = board.GP20
btn2_pin = board.GP21
btn3_pin = board.GP22

# Setting up the buttons
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT

# Setting up the keyboard
keyboard = Keyboard(usb_hid.devices)


while True:
    if not btn1.value:
        print("Select All")
        keyboard.press(Keycode.CONTROL, Keycode.A) # Press the SELECT ALL shortcut
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.A) # Release the press
    if not btn2.value:
        print("Copy")
        keyboard.press(Keycode.CONTROL, Keycode.C) # Press the COPY shortcut
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.C) # Release the press
    if not btn3.value:
        print("Paste")
        keyboard.press(Keycode.CONTROL, Keycode.V) # Press the PASTE shortcut
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.V) # Release the press
        
    time.sleep(0.1)