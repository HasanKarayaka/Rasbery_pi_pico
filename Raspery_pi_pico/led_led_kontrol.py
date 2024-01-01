import machine
import time

led_pin=machine.Pin(2,machine.Pin.OUT)
LIGHT_Pin =machine.Pin(3,machine.Pin.OUT)

LDR_pin =machine.ADC(26)
while True:
    led_pin.value(1)
    time.sleep(0.1)
    led_pin.value(0)
    time.sleep(0.1)
    
    vol=LDR_pin.read_u16()
    print(vol)
    time.sleep(0.2)
    if vol < 650:
        LIGHT_Pin.value(1)
    else:
        LIGHT_Pin.value(0)
    time.sleep(0.5)
        