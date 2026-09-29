from gpiozero import LED
import time

pin_number = 5
fan = LED(pin_number)

def fan_on():
    fan.on()

def fan_off():
    fan.off()
