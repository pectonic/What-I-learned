#funclarin ic ice kullanimi

def buyuk_sayiyi_dondur(a,b):
    if a > b:
        return a
    elif b > a:
        return b


def buyuk_sayi_metni(a,b):
    buyukSayi = buyuk_sayiyi_dondur(a,b)
    metin = '{} daha buyuktur'.format(buyukSayi)
    print(metin)

#buyuk_sayi_metni(40,13421)

#funclar birden fazla sonuc dondurebilir

def isim_soyisim(tamIsim):
    isim=tamIsim.split()[0]
    soyisim = tamIsim.split()[1]

    return isim, soyisim 

isim1, soyisim1 = isim_soyisim("can ahmet")

#print(isim1, soyisim1)

#args argumani 

def isim_soyisim_birlestir(isim, soyisim):
    return " ".join([isim, soyisim])

print(isim_soyisim_birlestir("can" , "ahmett")) # bak kanka burada iki isim var uc ve daha fazla icin args!

def isim_soyisim_birlestir(*args):
    return " ".join(args) #args burada ne girersen onu listler

print(isim_soyisim_birlestir("Can", "Ahmet", 'Aydin'))

def gobekadi_bulucu(**kwargs): #kwargs ise kutuphane mantigi
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print('yok yerak')

print(gobekadi_bulucu(isim = 'can', gobekadi = "pecto", soyisim = 'aydin'))