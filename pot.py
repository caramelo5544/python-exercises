from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
red = Pin(2, Pin.OUT)

while True:
    value = pot.read()
    print(value)
    if value > 2000:
        red.on()
    else:
        red.off()
    sleep(0.3)