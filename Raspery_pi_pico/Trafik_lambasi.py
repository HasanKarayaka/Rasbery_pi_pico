from machine import Pin
import utime
import _thread

button_1 = Pin(5,Pin.IN,Pin.PULL_DOWN)

led_k = Pin(2,Pin.OUT)
led_s = Pin(3,Pin.OUT)
led_y = Pin(4,Pin.OUT)

yayaRGB_green = Pin(17,Pin.OUT)
yayaRGB_red = Pin(16,Pin.OUT)

aracGecisSure = 15
aracBeklemeSure = 0

led_k.value(0)
led_s.value(0)
led_y.value(0)
yayaRGB_red.value(0)
yayaRGB_green.value(0)

buttonDurum = False

def button_okuma_thread():
    global buttonDurum
    while True:
        if button_1.value() == 1:
            print("Butona basıldı, yaya geçiyor")
            buttonDurum=True
        utime.sleep(0.1)

_thread.start_new_thread(button_okuma_thread,())

while True:
    
    if buttonDurum == False:
        led_y.toggle()
        yayaRGB_red.value(1)
        print("Araçlar geçiyor, yaya bekliyor")
        utime.sleep(aracGecisSure)
        
    else:
        print("yavaşla kırmızı yanacak")
        for i in range(10):
            led_y.toggle()
            utime.sleep(0.5)
            
        led_y.value(0)
        utime.sleep(0.5)
        
        led_s.value(1)
        print("Dikkat kırmızı yanacak")
        utime.sleep(2)
        led_s.value(0)
        led_k.value(1)
        
        utime.sleep(2)
        yayaRGB_red.value(0)
        yayaRGB_green.value(1)
        print("Araçlar bekliyor... yayalar geçecek")
        
        utime.sleep(aracBeklemeSure)
        yayaRGB_green.value(0)
        yayaRGB_red.value(1)
        utime.sleep(3)
        led_s.value(1)
        print("Araçlar hazırlanıyor, araçlar geçecek")
        utime.sleep(4)
        led_k.value(0)
        led_s.value(0)
        
        buttonDurum = False
        
