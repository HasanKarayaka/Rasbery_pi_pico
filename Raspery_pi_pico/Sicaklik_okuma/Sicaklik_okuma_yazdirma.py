from machine import ADC,Pin,I2C
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
sicaklik_Pini = ADC(4)
donusturme_carpani = 3.3/(65635)
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(20)
scl = Pin(21)


i2c = I2C(0, sda=sda, scl=scl,freq=40000)
lcd = I2cLcd(i2c,I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)



while True:
    okunan =sicaklik_Pini.read_u16() * donusturme_carpani
    sicaklik_Degeri = 27 - (okunan - 0.706)/0.001721
    print(sicaklik_Degeri)
    
    lcd.move_to(4, 0)
    lcd.putstr("sicaklik")
    lcd.move_to(4, 1)
    lcd.putstr(str(sicaklik_Degeri))
    
    utime.sleep(2)
    lcd.clear()
