'''RESIM ANALIZI MI NELEEEER ||| POST TALEBI '''
import requests
from requests.api import post
from PIL import Image
from io import BytesIO

grafik_URL = 'https://image-charts.com/chart'
#https://image-charts.com/chart?chs=700x190&chd=t:60,40&cht=p3&chl=Hello%7CWorld&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1
keyload = {
    "chs":"700x190",
    "chd":"t:50,50",
    "cht":"p3",
    "chl":"Hello|World",
    "chan": None,
    "chf":"ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1"
}
response = requests.post(grafik_URL, data=keyload)

#print(response.status_code)
response.content #kanka bu olusacak resmin byte hali

image1 = Image.open(BytesIO(response.content)) 
#image1.show()  bize yaptigimizi gosterir 

'''neyse buraya kadar sadece anlama isiydi, simdi ANKARA MESI OR CR RONALDINHO?????'''

grafik_URL = 'https://image-charts.com/chart'
#https://image-charts.com/chart?chs=700x190&chd=t:60,40&cht=p3&chl=Hello%7CWorld&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1
keyload = {
    "chco":"3092de,027182",
    "chd":"t:81,65,50,67,59,80",
    "chdl":"Falcao",
    "chl":"hiz|sut|pas|top_surus|defans|fizik",
    "chdlp":"b",
    "chs": "480x480",
    "cht":"r",
    "chtt":"Furbolcu ozellikleri"
}

response_radar = requests.post(grafik_URL, data=keyload)

#image2 = Image.open(BytesIO(response_radar.content))
#image2.show()

class futbolcu():
    
    def __init__(self,isim,hiz,sut,pas,top_surus,defans,fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.top_surus = top_surus
        self.defans = defans
        self.fizik = fizik

    def yetenek_hazirla(self):
        return ','.join([
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_surus),
            str(self.defans),
            str(self.fizik),
            str(self.hiz)
        ])

    def futbolcu_olustur(self):
        grafik_URL = 'https://image-charts.com/chart'
        keyload = {
            "chco":"3092de",
            "chd":"t:" + self.yetenek_hazirla(),
            "chdl":self.isim,
            "chl":"hiz|sut|pas|top_surus|defans|fizik",
            "chdlp":"b",
            "chs": "480x480",
            "cht":"r",
            "chtt":"Furbolcu ozellikleri",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm":"B,AAAAAABB,0,0,0",
            "chxl":"0:|0|20|40|60|80|100"

        }

        response = requests.post(grafik_URL, data=keyload)

        image = Image.open(BytesIO(response.content))

        #image.show()

    def oyunculari_kiyasla(self,hedef_oyuncu):
        grafik_URL = 'https://image-charts.com/chart'
        keyload = {
            "chco":"3092de,027182",
            "chd":"t:" + self.yetenek_hazirla() + '|' + hedef_oyuncu.yetenek_hazirla(),
            "chdl":self.isim + '|' + hedef_oyuncu.isim,
            "chl":"hiz|sut|pas|top_surus|defans|fizik",
            "chdlp":"b", 
            "chs": "480x480",
            "cht":"r",
            "chtt":"Furbolcu ozellikleri",
            "chxt":"x",
            "chxr":"0,0.0,100.0",
            "chm":"B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0",
            "chxl":"0:|0|20|40|60|80|100"

        }

        response = requests.post(grafik_URL, data=keyload)

        image = Image.open(BytesIO(response.content))
        image.show()

messi = futbolcu('Ankara Mesi',85,92,91,95,38,65)
ronaldo = futbolcu('Ronaldo',89,94,81,89,35,77)

print(ronaldo.oyunculari_kiyasla(messi))


    