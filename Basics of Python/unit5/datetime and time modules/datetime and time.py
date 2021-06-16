from datetime import date
import datetime

bugun = date.today()
print(bugun)

oylesine_tarih = date(2020,3,31)
print(oylesine_tarih)

print(bugun - oylesine_tarih) #yaa tarihler arasinda islemler yapiliyor, yas hesaplama yapilabilr

yarin = bugun + datetime.timedelta(days = 1) # ya bu normalde olan gune 1 ekliyor da hoca ne yaptin amk, neyse oldu :D
print(yarin) 

print(bugun.year) #direkt yil ay gun alabiliriz

print(date.isocalendar(bugun)) # (yil,hafta,hafta gunu) #hafta gunu indexi 1den basliyor mal amk >:(

print(date.weekday(bugun)) # index 0dn basliyor

from datetime import time

zaman = time(20,22,31)#saat verdim
print(zaman) 
print(zaman.hour)#ve tabii spesifik noktalara ulasabiliriz min ve sec givi 

simdi = datetime.datetime(2001,3,31,9,5,31)
print(simdi) 

import time
 
baslangic = time.time() #su anki zamani atiyor ama degisik bir gosterge ile: 60 bolunce saat, 60 bolunce dakika...
print('baslangic zamani: \t{}'.format(baslangic))
time.sleep(5)
bitis = time.time() #ya bu cooook guzelmis lan, sisteme delay atiyor
print('bitis: \t{}'.format(bitis))
print('gecen zman: \t{}'.format(bitis - baslangic))