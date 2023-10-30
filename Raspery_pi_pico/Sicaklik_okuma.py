from machine import ADC, Pin, I2C
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2clcd
I2C_ADDR = 0x27
I2C_NUM_ROWS =2
I2C_NUM_CLOS = 16

i2c = I2C(0,sda=sda, scl=scl,freq=400000)
lcd = I2clcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_CLOS)

sicaklik_Pini = ADC(4)

donusturme_carpani = 3.3 /(65535)

while True:
    okunan =sicaklik_Pin.read_u16() * donusturme_carpani
    sicaklik_Degeri = 27 -(okunan - 0.706)/0.001721
    
    print(sicaklik_Degeri)
    
    lcd.move_t(4, 0)
    lcd.putstr("Sicaklik")
    lcd.move_t(4, 1)
    lcd.putstr(str(sicaklik_Degeri))
    
    utime.sleep(2)
    lcd.clear()