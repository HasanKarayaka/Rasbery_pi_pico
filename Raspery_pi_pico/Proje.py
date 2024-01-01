from machine import UART
import time

# UART iletişimi başlat
uart = UART(0, 115200)

# UART'tan gelen verileri dinlemek için bir fonksiyon
def uartSerialRxMonitor(command):
    recv = bytes()
    while uart.any() > 0:
        recv += uart.read(1)
    res = recv.decode('utf-8')
    erase_len = len(command) + 5
    res = res[erase_len:]
    return res

# ESP8266'yi SoftAP+Station modunda yapılandır
send = 'AT+CWMODE=3'
uart.write(send + '\r\n')
time.sleep(1)

# SoftAP adını ve şifresini ayarla
send = 'AT+CWSAP="pos_softap","",11,0,3'
uart.write(send + '\r\n')
time.sleep(1)
res = uartSerialRxMonitor(send)
print(res)

# Çoklu bağlantı modunu etkinleştir
send = 'AT+CIPMUX=1'
uart.write(send + '\r\n')
time.sleep(1)
res = uartSerialRxMonitor(send)
print("Configured as Dual mode ->" + res)

# TCP sunucusunu 80 numaralı port üzerinden başlat
send = 'AT+CIPSERVER=1,80'
uart.write(send + '\r\n')
time.sleep(2)
res = uartSerialRxMonitor(send)
print("Server configured successfully -> " + res)

# Sıcaklık sensörünü başlat
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

# Ana döngü
while True:
    # Sıcaklık okuma
    reading_temp = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading_temp - 0.706) / 0.001721

    # HTML sayfasını oluştur
    val = '<head><title>Pi Pico Server</title></head><body><p>Temperature: ' + str(int(temperature)) + ' deg' + '</p></body>'
    print(val)
    length = str(len(val))

    # HTTP GET isteği ile Thingspeak'e veri gönder
    send = 'AT+CIPSEND=0,' + str(len(val) + len('GET /update?api_key=93R5NP8Q4XTPI1WV&field1=')) + '\r\n'
    uart.write(send + '\r\n')
    time.sleep(2)
    res = uartSerialRxMonitor(send)
    print("Data sent -> " + res)

    send = 'GET /update?api_key=93R5NP8Q4XTPI1WV&field1=' + str(int(temperature)) + '\r\n'
    uart.write(send + '\r\n')
    time.sleep(2)
    res = uartSerialRxMonitor(send)
    print("Data sent -> " + res)

    # Bekleme süresi
    time.sleep(1)
