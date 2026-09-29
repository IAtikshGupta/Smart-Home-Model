from gpiozero import PWMOutputDevice, LED
import time

ena_pin = 18
in1_pin = 27
in2_pin = 22

speed = PWMOutputDevice(ena_pin, initial_value=0)  # Start at 0 speed
in1 = LED(in1_pin)
in2 = LED(in2_pin)

def open_window():
    in1.on()      
    in2.off()
    speed.value = 1.0  
    time.sleep(5)
    stop()

def close_window():
    in1.off()     
    in2.on()
    speed.value = 1.0  
    time.sleep(5)
    stop()

def stop():
    speed.value = 0  
    in1.off()
    in2.off()
