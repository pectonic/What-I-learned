import os

'''current working dictionary yani mevcut konumu, calistigin konumu verir'''
#print(os.getcwd()) #

'''bulundugun yerdekileri listeler ayni zamanda parantez icine ozel konumda yazilabilir: ('C: //Bilgisayarim/') gibisinden'''
#print(os.listdir()) # 

'''bu komut ise defoult klasor yerini belirler, yazdigin diger komutlar biradan referans alir'''
#os.chdir('balblabla')# 

'''simdi bunu kodlarla nasil kullanabilecegimize bakalim'''
deneme = [*os.listdir()]

for x in deneme:
    print(x,' dosyasi babba')

'''mkdir komutu simdi klasor olurturlim '''

#os.mkdir('abo 2')

''' bak ya iki tane olurturmusum kappa neyse silmek icin de rmdir kullancagiz'''

#os.rmdir('abo 2') ayy cok guzel amk ya  ndsbvnjbdskjvbasj 

'''simdi ise dosya olurturmaya, yazmaya ve okumaya bakalim ve burada biraz yetkilerle ilgilenecegiz
## os.O_RDONLY − Read Only      - Sadece Oku
## os.O_WRONLY − Write Only     - Sadece Yaz
## os.O_RDWR   − Read and Write - Oku ve Yaz
## os.O_CREAT  - Create         - Olustur
'''

yeni_dosya = os.open('deneme_kod.txt', os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya, "kjsacfsahf".encode())
os.close(yeni_dosya) 

yeni_dosya2 = os.open('deneme_kod.txt', os.O_RDONLY)
okumalik = os.read(yeni_dosya2, 5) #bak burada uzunlugu oylesine verdim ama tam uzunluk icin os.stat ve st_size komutunu kullancagiz
os.close(yeni_dosya2)
#print(okumalik)

yeni_dosya3 = os.open('deneme_kod.txt', os.O_RDONLY)
#print(os.stat(yeni_dosya3))# bunu yazarak istatislik verilerine ve kodlarina ulasiyoruz ki st_size komutunu buradan aliyoru`
uzunluk = os.stat(yeni_dosya3).st_size #boylelikle metin ne olursa olsun uzunlugunu artik atadik
okumalik2 = os.read(yeni_dosya3 , uzunluk)
os.close(yeni_dosya3)

#print(okumalik2) # artik tum dosyayi okuyor 

'''bu kadar kullandik silmek icinde os.unlink komunutunu kullaniyoruz'''
#os.unlink('deneme_kod.txt') #komutu isimizi gorecektir

'''sildik simdi de isim degistirme isin os.rename nasil kullaniliyor ona bakalim'''
#os.mkdir('rename_babba') #burada olusturduk
print(os.listdir()) #burada gorduk
#os.rename('rename_babba', 'rename_La') # burada ismini degistirdik
print(os.listdir()) #burada tekrar gorduk



