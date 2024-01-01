from machine import UART
import machine
import _thread
import time

uart = UART(0,115200)
print("UART seri Haberleşme")
print(">", end="")
def uartSerialRxMonitor(command):
    recv=bytes()
    while uart.any()>0:
        recv+=uart.read(1)
    res=recv.decode('utf-8')
    erase_len=len(command) +5
    res=res[erase_len:]
    return res
send='AT+CWMODE=3'
uart.write(send+"\r\n")
time.sleep(1)
send='AT+CWSAP="pos_softap","",11,0,3'
uart.write(send+'\r\n')
time.sleep(1)
res=uartSerialRxMonitor(send)
print(res)
send="AT+CIPMUX=1"
uart.write(send+"\r\n")
time.sleep(1)
res=uartSerialRxMonitor(send)
print("configured as Dual mode ->" + res)
send ="AT-CIPSERVER = 1,80"
uart.write(send+"\r\n")
time.sleep(2)
res=uartSerialRxMonitor(send)
print("server configured secessfully-> " + res)
sensor_temp =machine.ADC(4)
conversion_factor = 3.3/(65535)

while True:
    reading_temp=sensor_temp.read_u16()* conversion_factor
    temperature= 27-(reading_temp - 0.706)/0.001721
    val="<head><title>Pi Pico Server</<title></head><body><p>temperature:"+str(int(temperature))+"deg"+"</p></body>"
    print(val)
    length=str(len(val))
    send ="AT+CIPSEND=1," +length
    uart.write(send+"\r\n")
    time.sleep(2)
    res=uartSerialRxMonitor(send)
    print("Data sent-> "+res)
    send=val
    uart.write(send+"\r\n")
    time.sleep(10)