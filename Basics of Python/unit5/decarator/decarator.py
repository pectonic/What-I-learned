'''uzun zaman oldu kasar, benden kacabilecegini mi sandin yarram... Calisma vakti'''

'''ilk olarak bir degisgene func atayabilgimizi gorecegiz, evet valla oluyor'''

def degisgene_atanacak():
    print('valla atadik')

degisgen = degisgene_atanacak
#print(degisgen()) #bak atadik aslan parcasi bu kadar

'''simdi de func ici func'a bakalim'''

def func_ici():
    print("ustteki func")

    def func_ici_ici():
        print("lan icerideyim")

    print(func_ici_ici())

#print(func_ici()) #noldu kasar, adres belli amk, gel amk, neyse amk boyle iste 

'''bak simdi ne yapacagim, func icinde baska funcu calistiracagim'''

def baskasina_gidecek():
    return 'hooop geldim ilk'

def baskasini_alacak(f):
    print('ikinci')
    print(f())

#print(baskasini_alacak(baskasina_gidecek)) #yukarida olan funcu alttakinin elemani olarak cagirabildik

'''burada bir sey yapacagim izle'''

def deco(f):
    def wrapper():

        print("baslangic")
        f() #buradaki amac asil fonksiyon oncesi ve sonrasi yapilacaklarin olmasi, wrapper ambalaj anlamina geliyor onun gibi iste, yemek istiyorsan once ambalaji acarsin degil mi, ayni ayni iste
        print("bitis")

    return wrapper

def sadece_yazdir():
    print("tek isim bunu yazdirmak")

sadece_yazdir = deco(sadece_yazdir) #aslinda burada sadece_yazdir funcunu ambalajliyoruz OBAAAAAA ADAM YA 
#print(sadece_yazdir()) #anladin mi aslan parcasi

def sadece_yazdir2():
    print("tek isim bunu yazdirmak 2")

sadece_yazdir2 = deco(sadece_yazdir2) #gordugun gibi ambalaj tek kullanimlik degil :)))
#print(sadece_yazdir2()) 

@deco
def sadece_yazdir3():
    print("tek isim bunu yazdirmak 3")

#print(sadece_yazdir3()) #gordun mu kolayligi, @deco yazarsak o amele atamaya gerek kalmadan tek satirda funcumuzu ambalajladik

'''burada problem arguman kismi dolu olanlarda hata verecek olmasi yani:'''
@deco
def toplama(a,b):
    print(a+b)

#print(toplama(4,3)) #olmayacak cunku bizim wrapper arguman beklemiyor ama bunu duzeltebiliriz 

def deco(f):
    def wrapper(*args): #Sınırsız sayıda parametreli fonksiyon oluşturmak 

        print("baslangic")
        f(*args) 
        print("bitis")

    return wrapper

#boylelikle duzelmis olmasi gerekiyor 
@deco
def toplama(a,b):
    print(a+b)
#print(toplama(4,3)) #evet, duzelmis.

'''arguman alan decarator'''

def deco(msg1,msg2):
    def ara_katman(f): #asil funcun oncesi sonrasina arguman vermek icin yaptik 
        def wrapper(*args):

            print(msg1)
            f(*args) 
            print(msg2)

        return wrapper
    return ara_katman

@deco("ilk","son") #boyle argumanlari verdik
def toplama(a,b):
    print(a+b)
#print(toplama(4,3)) 


import time

def deco_time(f):

    def wrapper(*args):
        baslangic = time.time()
        print("baslanhic:\t{}".format(baslangic))
        f(*args)
        bitis = time.time()
        print("bitis:\t{}".format(bitis))

        print("gecen zaman: {}".format(bitis - baslangic))
    return wrapper

@deco_time
def factoriyel(sayi):
    toplam = 1
    while sayi > 1:
        toplam = toplam * sayi
        sayi = sayi - 1
    print(toplam)

print(factoriyel(1000))


