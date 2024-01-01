from machine import Pin,PWM
import time

motorPin=machine.PWM(machine.Pin(10));

while True:
    for outputValue in range(0,65535,100):
        motorPin.duty_u16(outputValue)
        time.sleep_ms(5)
        
    time.sleep(3)
    
    for outputValue in range(65535,0,-100):
        motorPin.duty_u16(outputValue)
        time.sleep_ms(5)
        
    time.sleep(3)
        
        
   
    