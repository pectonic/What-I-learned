#input kullanicidan deger almaya yarar babba

def durum():
    sayi = input('sayi gir: ')

    if int(sayi) % 2 == 0:
        print('sayi cifttir')
    else: 
        print('tek')

print(durum()) 
