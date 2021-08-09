round(1.4) #round sayiyi yuvarlamaya yarar

def tam_sayiya_cevirme():
    sayi = input('sayi gir: ')
    try: #dene
        sayi = float(sayi)
    except: # denedin olmadi mi, burayi calistirir
        print('kanka bu donusturelemez bir deger... = {}'.format(sayi))
    else: # bunu tam anlamadim herhalde try gerceklesirse oluyor
        print('iste yuvarlanmis sonuc: {}'.format(round(sayi)))


def tam_sayiya_cevirme1():
    sayi = input('sayi gir: ')
    status = ''
    try: #dene
        sayi = float(sayi)
        status = 'basarili'
        print('iste yuvarlanmis sonuc: {}'.format(round(sayi)))
    except: # denedin olmadi mi, burayi calistirir
        print('kanka bu donusturelemez bir deger... = {}'.format(sayi)) 
        status = 'basarisiz'
    finally: # her iki durumda da calisiyor
        print('islem durumu: {}'.format(status))
        

def tam_sayo_cevirme_dongu():
    while True:
        deger = input('sayi gir ama ondalik: ')

        try:
            deger = float(deger)
            print('donustu karsim ho: {}'.format(deger))
            break
        except:
            print('do-dostum {} donusmez amk '.format(deger))
            pass

#print(tam_sayo_cevirme_dongu())
"""
#except aslinda hata halinde calisir ve bunu daha da daraltabiliriz

try:
    5 + 'a'
except TypeError:
    print('lan slak onla o toplanir mi amk cocu')

"""
"""
#ve ve ve except'i birden fazla hata icin uyarlayabiliriz

try:
    5 + 'a'
except TypeError:
    print('lan slak onla o toplanir mi amk cocu')
except IndexError:
    print('bisiler bisiler index hakkinda bilgiler')
except: #burada genel bir hata olursa kod hayatta kalmasi icin biraktim ;))))
    print('kod duzgun calismiyor babuss')

"""