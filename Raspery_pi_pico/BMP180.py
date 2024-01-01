from machine import Pin, SoftI2C
from bmp180 import BMP180
from time import sleep

# I2C pin tanımlamaları
i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=100000)  # I2C frekansını 100kHz olarak ayarlayın

# BMP180 sensörünü başlat
bmp = BMP180(i2c)

while True:
    try:
        # Sıcaklık ve basınç ölçümlerini al
        temperature = bmp.temperature
        pressure = bmp.pressure

        # Alınan değerleri ekrana yazdır
        print("Sıcaklık: {:.2f} °C, Basınç: {:.2f} hPa".format(temperature, pressure / 100.0))

    except Exception as e:
        print("Hata:", e)

    # 2 saniye bekleyin (isteğe bağlı olarak ayarlayabilirsiniz)
    sleep(1)
