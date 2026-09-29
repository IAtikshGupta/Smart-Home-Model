from gpiozero import LED
import time

pin_number = 25
licht = LED(pin_number)

def light_on():
    licht.on()

def light_off():
    licht.off()

