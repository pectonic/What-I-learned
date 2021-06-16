def bes_bastir():
    print('hey!')



#funclarda print ve return farki

def bes_dondur():
    return (3)

#bes_dondur()

#a = bes_bastir()
#b = bes_dondur()

#print(a)
#print(b)

#funclarda argumanlar

def sayi_dondur(sayi):
    print(sayi)

#sayi_dondur(333)

def sayi_dondur(sayi2=200): #buna pasif deger deniliyor yani deger vermezsen default 200 verir ama degistiribilirsin
    print(sayi2)

#sayi_dondur()

#funclarin kendi arasinda iliskileri

def buyuk_sayiyi_dondur(a,b):
    if a > b:
        return a
    elif b > a:
        return b

print(buyuk_sayiyi_dondur(5,10))