class Ucus():
    hava_yolu = 'THY'

ucus1 = Ucus.hava_yolu

#print(ucus1)

class Ucus2():
    hava_yolu = 'THY'

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def __repr__(self) -> str: #repr bu classin ana aciklamasini yapmaya yarar. print(bilet3)
        return '{} nolu ucustur.'.format(self.kod)

    def anons_yap(self):
        return '{} nolu ucusumuz {}-{} arasinda yapilmak uzere {} saat surecektir'.format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure
        )
    def kalan_koltuk_sayisi(self):
        return self.kapasite - self.yolcu

    def satilan_biletler(self, bilet=1):
        if bilet + self.yolcu <= self.kapasite:
            self.yolcu += bilet
            self.kalan_koltuk_sayisi()
            return '{} bilet satilmistir ve {} kadar koltuk bos. Toplam yolcu {}'.format(bilet,self.kalan_koltuk_sayisi(), self.yolcu)
        else:
            return 'ya yarram o kadar bilet mi var amcik, once koltuk sayisina bak'
    
    def bilet_iptal(self, iptaller=0):
        if self.yolcu - iptaller >= 0:
            self.yolcu -= iptaller
            self.kalan_koltuk_sayisi()
            return '{} bilet iptal edilmistir, kalan koltuk sayisi {}. Toplam yolcu {}'.format(iptaller, self.kalan_koltuk_sayisi(), self.yolcu)
        else:
            return 'ya amcik o kdar bilet mi var iptal ediyorsun'
bilet2 = Ucus2('AB123', '08.00AM IST', '10.00AM ANK', 2, 300, 80)
bilet3 = Ucus2('AB223', '09.00AM Bodrum', '10.00AM ANT', 1, 200, 180)

#print(bilet3.satilan_biletler(10))
#print(bilet3.bilet_iptal(190))

#print(bilet2.hava_yolu, bilet2.kod,'\n',bilet3.hava_yolu, bilet3.kod)
#print(bilet3.anons_yap())
#print(bilet2.anons_yap())

#print(bilet3)

print(bilet3.__dir__()) # dir classin sahip oldugu ozellikleri gosterir diyebilir miyiz? olur gibi
        