from machine import Pin,UART
import utime
uart = UART(0,9600)

led_k = Pin(2,Pin.OUT)
led_s = Pin(3,Pin.OUT)
led_y = Pin(4,Pin.OUT)

led_k.value(0)
led_s.value(0)
led_y.value(0)

buton1=Pin(5,Pin.IN,PULL_DOWN)
buton2=Pin(6,Pin.IN,PULL_DOWN)
buton3=Pin(7,Pin.IN,PULL_DOWN)

while True:
    try:
        if uart.any() > 0:
            data=uart.readline()
            
            if "K" in data:
                uart.write("rR255G0B0")
                led_k.toggle()
                utime.sleep(0.1)
            if "Y" in data:
                uart.write("sR255G0B0")
                led_y.toggle()
                utime.sleep(0.1)
            if "S" in data:
                uart.write("sR255G0B0")
                led_s.toggle()
                utime.sleep(0.1)
        if buton1.value() == 1:
            print("Buton 1 OK")
            uart.write("buton 1 OK! \n")
            utime.sleep(0.3)
        
        if buton2.value() == 1:
            print("Buton 2 OK")
            uart.write("buton 2 OK! \n")
            utime.sleep(0.3)
        
        if buton3.value() == 1:
            print("Buton 3 OK")
            uart.write("buton 3 OK! \n")
            utime.sleep(0.3)
    except:
        print("Başarısız")
            