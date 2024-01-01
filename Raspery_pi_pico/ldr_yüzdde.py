#programın içinde sürekli tekralanacak işlem varsa bu işlem fonk olarak yazılabilir
# ışık değerini okumak gibi sürekli yapılması gereken işlem

from machine import ADC,Pin
from time import sleep

LDR_Pin = 26
def readlight(photoGP):
    photoRes = ADC(Pin(26))
    light=photoRes.read_u16()
    light=round(light/65535*100,2) # ışık degerini 65534 tane deger geldiği için o değere böldük ve 100 ile çarptık yüzdelik ksımı bulalım , 2 e virgülden sonra sı içindir
    return light
while True:
    print("ışık:"+ str(readlight(LDR_Pin)) + "%")
    sleep(1)