from machine import Pin
import utime
import _thread

led_k = Pin(2, Pin.OUT)
led_y = Pin(4, Pin.OUT)

led_k.value(0)
led_y.value(0)

def second_thread():
    x=1
    while True:
        #baton.acquire()
        led_y.toggle()
        utime.sleep(2)
        print("2. _thread {0}. kez çalıştı." .format(x))
        x+=1

_thread.start_new_thread(second_thread, ())

while True:
    baton.acquire()
    led_k.toggle()
    utime.sleep(1)
    baton.release()