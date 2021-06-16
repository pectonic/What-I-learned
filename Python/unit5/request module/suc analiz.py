'''SUC ANALIZ YAPIYORUZ LAN '''

from typing import Counter #HASSIKTIR LAN  olm altta kullandigim komutu kendi import etmis vay amk
import requests

class suc_analiz():

    def __init__(self,bolge,tarih,suc_turu = "all-crime"):
        self.bolge = bolge
        self.tarih = tarih
        self.suc_turu = suc_turu
        self.suclar = self.suclari_bul()


    def suclari_bul(self): #suclari almak icin func yazalim
        suc_URL = 'https://data.police.uk/api/crimes-no-location' #APIyi cekiyoruz

        payload = { #keyleri yaziyoruz
            'category' : self.suc_turu,
            'force' : self.bolge,
            'date' : self.tarih
        }
        response = requests.get(suc_URL, params=payload)#geri bildrimi aliyoruz

        if response.status_code == 200: #basarili cekip cekmedigini soruyoruz
            return response.json() #basariliysa aktariyoruz
        else:
            return None #basarisiz olursa none gondersin ki hata vermesin

    def suclari_say(self): #hangi suc kac kere islenmis acep

        suclar_listesi = [] #suclari listlemek icin bos bir liste

        if self.suclar is not None: #none degilde insin ki yine patlamayalim
            for suc in self.suclar: #suclar icinde gez ve
                suclar_listesi.append(suc['category']) #suclar_listesi'ne yolla
            
            return Counter(suclar_listesi)#counter hangi sonucun kac kere dondugunu bize gosteriyor 

bolge = 'city-of-london'
tarih_asil = '2021-02' 
sr = suc_analiz('{}'.format(bolge), '{}'.format(tarih_asil)) #verilerimizi giriyoruz
print(len(sr.suclari_say())) #ve OBAAAA 
deneme = sr.suclari_say()
print(len(deneme))


#print('{}'.format(bolge), '{}'.format(tarih_asil))





