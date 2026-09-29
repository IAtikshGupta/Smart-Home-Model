from gpiozero import LED
import time

pin_number = 6
heizung = LED(pin_number)

def heater_on():
    heizung.on()

def heater_off():
    heizung.off()