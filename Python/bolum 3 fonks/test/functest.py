#soru 1 Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde doldurun
def ust_alma(x,y):
    sonuc = x**y
    return sonuc

#print(ust_alma(5,2))

#soru 2 Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde ve ** yerine for döngüsü ile hesaplayacak bicimde olusturun
def ust_alma(x,y):
    ust = [*range(y-1)]
    kontrol = y
    for y in ust:
        if kontrol == 0:
            break
        else:
            x *= x
            kontrol -= 1
    return x

#print(ust_alma(5,1))

#soru 3 Asagidaki fonskiyonu 1 parametre alacak (sadece sayilardan olusan liste tipinde) ve en büyük iki sayiyi döndürecek bicimde olusturun

liste = [1,5,10,2,6]

def sirala_ve_son_ikiyi_ver(l):
    l.sort()
    l.reverse()
    return l[0:2]

#print(sirala_ve_son_ikiyi_ver(liste))

#Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde) ve sadece str tipindeki degerleri filter ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun¶

liste4 = [1,2,3,5,'abc','a',True]

def str_filtrele(l4):
    """
    parametre: rastgele tipte elemanlar iceren
    tip:       liste
    örnek:     [1,2,3,5,'abc','a',True]
    
    r-return:  sadece string tipindeki degerleri iceren
    r-tip:     liste
    r-örnek:   ['abc', 'a']
    """
    
    if type(l4) == str:
        return l4
    else:
        pass        

#print([*filter(str_filtrele,liste4)])
#print([*filter(lambda x: type(x) == str, liste4)])

#Asagidaki fonskiyonu 1 parametre alacak (sadece sayi iceren liste tipinde) ve map ve lambda ifadelerini kullanarak 6 sifir atacak bicimde olusturun
"""
    parametre: sayi tipinde elemanlar iceren
    tip:       liste
    örnek:     [1000000, 90000000, 15000000]
    
    r-return:  liste elemanlarinin 6 sifir atilmis halinde
    r-tip:     liste
    r-örnek:   [1, 90, 15]
    """
paralar = [1000000, 90000000, 15000000]
def paradan_alti_sifir_at(x):
    x = int(x/1000000)
    return x

#print([*map(paradan_alti_sifir_at, paralar)])
#print([*map(lambda p: int(p/1000000), paralar)])

#Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat ve dakika alacak bicimde olusuturun.

def zaman_verisi_al():
    saat = input('saat kac: ')
    dakika = input('dakika: ')
    while True:
        if (saat.isdigit() == True) and (dakika.isdigit() == True):
            break
        else:
            print('lutfen sayi giriniz')
            saat = input('saat kac: ')
            dakika = input('dakika: ')

    return 'Saat {}, dakika {}'.format(saat,dakika)

#print(zaman_verisi_al())
