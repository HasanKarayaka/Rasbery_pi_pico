from machine import Pin
import utime

RGB_red = Pin(18,Pin.OUT)
RGB_blue = Pin(16, Pin.OUT)

RGB_red.value(0)
RGB_blue.value(0)

LED_time = 0.09
LED_count = 1

while True:
    for i in range(LED_count):
        RGB_red.value(1)
        utime.sleep(LED_time)
        RGB_red.value(0)
        utime.sleep(LED_time)
        RGB_red.value(1)
        utime.sleep(LED_time)
        RGB_red.value(0)
        utime.sleep(LED_time)
        
    for i in range(LED_count):
        RGB_blue.value(1)
        utime.sleep(LED_time)
        RGB_blue.value(0)
        utime.sleep(LED_time)
        RGB_blue.value(1)
        utime.sleep(LED_time)
        RGB_blue.value(0)
        utime.sleep(LED_time)
        