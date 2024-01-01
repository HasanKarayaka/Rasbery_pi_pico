from machine import Pin
import utime

buton1_flag= 0
buton2_flag = 0

buton1=Pin(5,Pin.IN,Pin.PULL_UP)
buton2=Pin(6,Pin.IN,Pin.PULL_UP)

bt1_count = 0
bt2_count = 0

led=Pin(7,Pin.OUT)

def callback1(pin):
    global bt1_count
    bt1_count +=1
    print("Buton 1 e basıldı", bt1_count)
    
    if bt1_count == 5:
        led.toggle()

def callback2(pin):
    global bt2_count
    bt2_count +=1
    print("buton 2 ye bu kadar basıldı" ,bt2_count)
    
    if bt2_count == 3:
        for i in range(3):
            led.value(1)
            utime.sleep(0.5)
            led.value(0)
            utime.sleep(0.5)
try:
    while True:
        if buton1.value(1)  and buton2_value(1):
            led.toggle()
        

