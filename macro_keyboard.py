import time
import board
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP20
btn2_pin = board.GP21
btn3_pin = board.GP22

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT

keyboard = Keyboard(usb_hid.devices)


while True:
    if not btn1.value:
        # Add code for mapping the 1st button
    if not btn2.value:
        # Add code for mapping the 2nd button
    if not btn3.value:
        # Add code for mapping the 3rd button
        
    time.sleep(0.1)