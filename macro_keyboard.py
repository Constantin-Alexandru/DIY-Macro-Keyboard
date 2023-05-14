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
        print("Select All")
        keyboard.press(Keycode.CONTROL, Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.A)
    if not btn2.value:
        print("Copy")
        keyboard.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.C)
    if not btn3.value:
        print("Paste")
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.V)

    time.sleep(0.1)