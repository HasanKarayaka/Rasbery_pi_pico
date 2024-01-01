import machine import Pin, PWM
import utime

led_k = Pin(2,Pin.OUT)
PIR = Pin(19,Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(19))
buzzer.freq(2000);

buzzer.duty_u16(0) # darbe süresi başlangıç da ses olmaması için
led_k.value(0)

while True:
    if PIR.value()==1:
        print("VARLIG Algılandı , ALARM !!!")
        for j in range(100):
            buzzer.duty_u16(40000)
            led_k.toggle()
            utime.sleep_ms(70)
            buzzer.duty_u16(0)
            
    led_k.value(0)
    buzzer.duty_u16(0)
    print("Alarm Kaldırıldı...")
    utime.sleep(0.5)