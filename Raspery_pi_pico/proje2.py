import machine
import utime

# GPIO pin tanımlamaları
RX_PIN = 12  # Değiştirebilirsiniz
TX_PIN = 11  # Değiştirebilirsiniz
DHT11_PIN = 2  # Değiştirebilirsiniz

# UART tanımlamaları
uart = machine.UART(0, baudrate=115200, tx=TX_PIN, rx=RX_PIN, timeout=1000)

def send_at_command(command):
    uart.write(command + '\r\n')
    utime.sleep(1)
    response = uart.read(100)
    return response

def connect_to_wifi():
    send_at_command('AT')
    while not b'OK' in send_at_command('AT'):
        print("ESP8266 not found.")

    send_at_command('AT+CWMODE=1')
    while not b'OK' in send_at_command('AT+CWMODE=1'):
        print("Setting mode...")

    print("Set as client mode")
    print("Connecting to WiFi...")

    wifi_command = 'AT+CWJAP="{}", "{}"'.format(agAdi, agSifresi)
    send_at_command(wifi_command)

    while not b'OK' in send_at_command('AT+CWJAP?'):
        print("Failed to connect to WiFi.")

    print("Connected to WiFi.")

def send_data_to_thingspeak():
    global sicaklik, nem

    send_at_command('AT+CIPSTART="TCP","'+ip+'",80')
    if b'Error' in uart.read(100):
        print("Failed to start TCP connection.")

    dht = machine.DHT(DHT11_PIN)
    sicaklik = dht.temperature()
    nem = dht.humidity()

    data = "GET /update?api_key=93R5NP8Q4XTPI1WV&field1={:.2f}&field2={:.2f}\r\n\r\n".format(sicaklik, nem)

    send_at_command('AT+CIPSEND={}'.format(len(data)))
    utime.sleep(2)

    if b'>' in uart.read(100):
        uart.write(data)
        print(data)
        print("Data sent successfully.")
        utime.sleep(1)

    print("Connection closed.")
    send_at_command('AT+CIPCLOSE')
    utime.sleep(1)

def main():
    connect_to_wifi()

    while True:
        send_data_to_thingspeak()
        utime.sleep(60)  # 1 dakika bekleyin

if __name__ == "__main__":
    main()
