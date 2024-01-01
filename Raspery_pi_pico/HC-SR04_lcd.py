from machine import Pin, I2C
import utime

trigger = Pin(8,Pin.OUT)
echo = Pin(9,Pin.IN)

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


sda=Pin(20)
scl=Pin(21)

i2c = I2C(0, sda=sda, scl=scl,freq=40000)
lcd = I2cLcd(i2c,I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def mesafe():
    trigger.low()
    utime.sleep(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        sinyalKapali = utime.ticks_us()
    while echo.value() == 1:
        sinyalAcik = utime.ticks_us() # belli bir zamana baglı utime içinde fonksiyondur(ticks),ms olarak sayaç kurar
    gecenZaman = sinyalAcik - sinyalKapali
    uzaklik = (gecenZaman * 0.0343) / 2 # ses hızı 343m/s ses 1 sn 343m yol alır , 2 ile bölme sebebi hem gidiyor hem geliyor ses o yüden
    print("Uzaklık", uzaklik,"cm")
    
    lcd.move_to(4, 0)
    lcd.putstr("uzaklik")
    lcd.move_to(4, 1)
    lcd.putstr(str(uzaklik))
    lcd.move_to(14,1)
    lcd.putstr("cm")
    
while True:
    mesafe()
    utime.sleep(1)
    lcd.clear()
        
        