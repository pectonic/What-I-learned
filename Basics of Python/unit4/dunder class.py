class seyahat():

    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis

    def anons(self):
        return '{}-{} yolculugumza hg'.format(self.kalkis , self.varis)

class Otobus(seyahat):
    def __init__(self, mola_duraklari, ):
        seyahat.__init__(self, 'ANK', 'IST')
        self.mola_duraklari = mola_duraklari
    

class araba(seyahat):
    def __init__(self, kalkis, varis, petrol_duraklari):
        super().__init__(kalkis, varis)
        self.petrol_duraklari = petrol_duraklari

    


bilet1 = seyahat('Bod', 'Bay')
bilet2 = Otobus(['fet', 'alanya'])
bilet3 = araba('adana','ankara',['konya', 'hooop ananain ami'])
print(bilet1.kalkis)
print(bilet2.mola_duraklari)
print(bilet3.petrol_duraklari)
