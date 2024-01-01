from machine import ADC,Pin,I2C
import utime

pot =ADC(27)
donusturme_carpani = 3.3/(65635)

from lcd_api import LcdApi

from pico_i2c_lcd import I2cLcd
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(20)
scl = Pin(21)


i2c = I2C(0, sda=sda, scl=scl,freq=40000)
lcd = I2cLcd(i2c,I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def convert(x, in_min,in_max,out_min,out_max):
    return(x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    voltage = pot.read_u16() * donusturme_carpani
    print("voltaj=", voltage)
    print("yüzde:", convert(pot.read_u16(), 1000,65535,0,100))
    print("-------------------")
    
    lcd.move_to(5, 0)
    lcd.putstr("voltaj")
    lcd.move_to(4, 1)
    lcd.putstr(str(voltage))
    
    utime.sleep(2)
    lcd.clear()