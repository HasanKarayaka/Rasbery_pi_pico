from machine import ADC,Pin
import utime
led_pin = Pin(2,Pin.OUT)
pot = ADC(27)

while True:
    print("Potansiyometre Değeri =", pot.read_u16())
    
    utime.sleep(1)
    
    