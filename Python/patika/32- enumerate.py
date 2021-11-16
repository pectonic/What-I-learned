l = [(1,2),(10,20)] # elemanlar tuple yani a,b = (1,2) olamaz mi? bal gibi olur

for i in l:
    a,b = i
    print(a)
    print(b)
    print('====================')

for a,b in l:
    print('ilk eleman = ',a)
    print('ikinci eleman = ',b)
    print('==========================')

# simdi bunu text icin yapalim

adlar = ['can', 'my boss John', 'Hardworker Can', 'Eglence bagimlisi Can']

for a,b in enumerate(adlar): # enumerate listedeki elemanlari tuple yapar ve verdigimiz degerden (0 , xxx), (1, xxx) diye cevirir
    print(a, ' indexindeki ad = ', b)
print('==========================')

ogrenciler = ['ogrenci_1', 'ogrenci_2', 'ogrenci_3']
notlar = [35,56,77]

for a,b in zip(ogrenciler,notlar):
    print(a, 'ogrencisinin notu =', b)