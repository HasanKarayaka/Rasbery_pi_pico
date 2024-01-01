from machine import Pin,UART

uart=UART(0,9600)
led = Pin(13,Pin.OUT)

while True:
    if uart.any() >0:
        data=uart.read()
        print(data)
        if "on" in data:
            led.value(1)
            print("Led On \n")
            uart.write("Led On \n")
        else "off" in data:
            led.value(0)
            print(" Led off \n")
            uart.write("Led Off \n ")
                
                