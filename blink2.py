from machine import Pin
from time import sleep

red = Pin(2, Pin.OUT)
green = Pin(4, Pin.OUT)

while True:
    red.on()
    green.off()
    sleep(0.5)
    red.off()
    green.on()
    sleep(0.5)