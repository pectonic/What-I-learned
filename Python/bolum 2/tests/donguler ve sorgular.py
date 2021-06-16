# Soru 1: Ferhat Ibrik Kullanicisinin uzmanlik alanlarini döndür

kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End','yazilim', 'yazilim']
}

for k,v in kullanici1.items():
    if k == "uzmanlik":
        print("Ferhat uzmanlik: {}".format(v))
        break


print("######################################################################################################")

# Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür

kullanici_listesi = [kullanici1, kullanici2, kullanici3] 
kisino = 0
#print(kullanici_listesi[1].items())
for kisi in kullanici_listesi:
    for k,v in kisi.items():
        if v == ['Front-End']:
            print(kullanici_listesi[kisino]['ad'])
    kisino += 1

print("######################################################################################################")

# Soru 3: Mesut kullanicisi Yazilim ögrendi, bilgileri güncelle! 



# Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)

#print(len(kullanici_listesi[1]['uzmanlik']))

kisino2 = 0

for kisi2 in kullanici_listesi:
    for va in kisi2.values():
        if len(kullanici_listesi[kisino2]['uzmanlik']) > 1: 
            print(kisi2)
            break
    kisino2 += 1

print("######################################################################################################")

# Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?
kullanici_yaslari_listesi = [22, 34, 32]

yas_kont = 0
for kullanicilar, yaslar in zip(kullanici_listesi, kullanici_yaslari_listesi):
    if yaslar < 30:
        print(kullanicilar)

print("######################################################################################################")

# Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!

deger = 8
asal_tester = deger - 1


while asal_tester > 1:
    if deger % asal_tester == 0:
        print("asal degil")
        break
    else:
        asal_tester -= 1
else:
    print("asal")
        



