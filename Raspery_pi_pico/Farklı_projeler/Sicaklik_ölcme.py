from machine import Pin, ADC
from time import sleep
led = Pin(25,Pin.OUT)
sensor_temp = ADC(4) # 4 numaralı pine baglı olan sıcaklık sensöründen gelen adc verisini tanımladığımız değere atadık
conversion_factor = 3.3 / (65535) # 3.3 v elektirği 5535 e böldük sıcaklık değerini anlamlı hala getirmek için

while True:
    reading = sensor_temp.read_u16() * conversion_factor # sensörden gelen veriyi dönüştürdük sıcaklığı C cinsiden ölçebilmek için
    temperature = 27 - (reading - 0.706)/0.001712 # bu denklem rp20 işlemcisinde özgü bir denklem 
    if temperature > 25:
        led.toggle()
        print("COK SİCAK",temperature)
        sleep(1)
    else:
        led.value(1)
        print("sicaklık normal" , temperature)
        sleep(1)
        
    