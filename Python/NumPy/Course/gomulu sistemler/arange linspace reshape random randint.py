import numpy as np

#bu kod satirlarinda np.arange/linspace/reshape ve random.random/randint ogrenilmistir



#np.arange() not: arange yari kapali aralik kullanir yani [x,y) gibi

deneme_arange = np.arange(10)#tek satir 0dan 10a kadar dondurdu
print(deneme_arange)

deneme_arange2 = np.arange(2,8)#2den basla 8e kadar emrini verdik, o da calistirdi bea
print(deneme_arange2)

deneme_arange3 = np.arange(2,8,2)#2den basla 8e kadar 2 atlayarak let's fucking gooo 
print(deneme_arange3)

print('---------------------------')

#np.linspace not: linspace ise kapali araliktir yani [x,y] ama eger parametreler kismina endpoint=False eklersek yari kapali aralga donecektir

deneme_linspace = np.linspace(0,20,40)#0dan 20ye kadar bana 40 tane deger ver emri verdik. NOT: eger biz almak istedigimiz degeri vermezsek default 50 eleman alacaktir 
print(deneme_linspace)

print('---------------------------')

#np.reshape ile simdi array'lerin ayarlariyla oynayacagiz, CEKIYN MI BABBA

deneme_arange4 = np.arange(32) #32 elemanlik tek satirlik array olusturduk

deneme_reshape = np.reshape(deneme_arange4, [2,4,4]) #tek satir olan seyi 3 boyutlu 4x4(16+16=32 bu da arange degerimizle uyumlu) matris olusturduk
print(deneme_reshape) 
print()

#tabii bunu istedigimiz sekli verebiliriz  

deneme_linspace2 = np.linspace(0,50,15)
deneme_reshape2 = np.reshape(deneme_linspace2, [3,5]) #gorebildigimiz gibi bu sefer sadece 2 boyutlu yaptik ve yine degerler birbiri ile uyumlu
print(deneme_reshape2)
print()

#veya bunu tek satirda halledebiliriz ama sanki bos isler yapiyoruz gibi geliyor, neyse sabrin sonu selamettir arkadaslar

deneme_reshape3 = np.linspace(0,50,15).reshape([3,5])#tek satirda yaptik 
print(deneme_reshape3)

print('---------------------------')


#random.random

deneme_random_array = np.random.random([3,4,6])#bu sekilde shape belirledikten sonra degerlerin random olacak sekilde array olusturabiliyoruz
print(deneme_random_array)

print('---------------------------')

#random.randint

deneme_randint_array = np.random.randint(4,20, [2,5])#4 ile 20 arasinda random degerlerle 2x5 array babba ve de int degerler 
print(deneme_randint_array)
