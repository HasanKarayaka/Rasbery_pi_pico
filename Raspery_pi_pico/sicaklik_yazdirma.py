from machine import ADC,Pin
import utime

sicaklil_Pini = ADC(4)
donusturme_carpani = 3.3 / (65535)

olcumAraligi = 15

while True:
    okunan = sicaklik_Pini.read_u16() * donusturme_carpani
    sicaklik_Degeri = 27 - (okunan - 0.706)/0.001721
    
    zaman =utime.gmtime()
    
    tarihSaat= str(zaman[2]) + "/" + str(zaman[1]) + "/" + str(zaman[0]) + " - " + str(zaman[3]) + ":" + str(zaman[4]) + "." + str(zaman[5])
    with open("sicaklik.txt","a+") as dosya
       dosya.write("{0} ------ : {1}\n".format(tarihSaat , sicaklik_Degeri))
        
        utime.sleep(olcumAraligi)
    
    