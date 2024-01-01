from machine import Pin
import utime

led_pin = Pin(2,Pin.OUT)

while True:
    led_pin.toggle()
    utime.sleep(1)