from machine import Pin, time_pulse_us
from time import sleep, sleep_us

trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)
led = Pin(2, Pin.OUT)

def distance_cm():
    trig.off()
    sleep_us(2)
    trig.on()
    sleep_us(10)
    trig.off()
    t = time_pulse_us(echo, 1, 30000)
    return t * 0.0343 / 2

while True:
    d = distance_cm()
    print("Distance:", round(d, 1), "cm")
    if d < 20:
        led.on()
    else:
        led.off()
    sleep(0.5)