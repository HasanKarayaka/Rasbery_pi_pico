from machine import Pin, PWM
import utime
PIR = Pin(19,Pin.IN,Pin.PULL_DOWN)

buzzer = PWM(Pin(10))
buzzer.freq(2000);
buzzer.duty_u16(0)

while True:
    if PIR.value() == 1:
        print("PIR calısıor...")
        buzzer.duty_u16(40000)
        utime.sleep(1)
        buzzer.duty_u16(0)
    else:
        print("Haraket bekelniyor...")
        
    utime.sleep(0.5)