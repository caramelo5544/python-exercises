from machine import Pin
from time import sleep

red = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    if button.value() == 0:
        red.on()
    else:
        red.off()
    sleep(0.2)