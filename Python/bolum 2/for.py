kullanicilar = ["CAN sdfs","Burak asfasf","memet qwrqwr","kelek vsvsdv","yarraaa adaDa"]

sira = 0
modasayi=0
moderator = "memet qwrqwr"
    
for isimler in kullanicilar:
    
    ad, soyad = isimler.split()[0],isimler.split()[1]
    if(isimler == moderator):
        modasayi += 1
        print("{0}. mod ismi {1} ve soyismi {2}".format(modasayi,ad,soyad))
    else:
        sira += 1
        print("{0}. kullanicinin adi {1} ve soyadi {2}".format(sira,ad,soyad))
    


degismeyenler = (4,5,6,7)

for x in degismeyenler:
    print(x)

kutup = {
    "ad" : "Can",
    "soyad" : "Aydin",
    "yasadigi yer" : "Sakarya"
}


for k,v in kutup.items():
    if (k == 0 and v == 0):
        print("{0} : {1}".format(k,v))
    elif (k == 1 and v == 1):
        print("{0} : {1}".format(k,v))
    else:
        print("{0} : {1}".format(k,v))


coklu = [[1,2],[3,4],[5,6]]

for x,y in coklu:
    print(x)
    print(y)