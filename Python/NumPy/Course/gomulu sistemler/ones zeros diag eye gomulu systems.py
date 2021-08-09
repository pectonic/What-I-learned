import numpy as np
from numpy.core.numeric import ones

#bu kod satirlarinda np.ones/zeros/full/empty/fill/eye/diag ogrenilmistir 


#np.zeros ve np.ones 

deneme_zeros = np.zeros(4) #bize 0lar verdi ve float
print(deneme_zeros)
print(deneme_zeros.dtype)

print('---------------------------')

deneme_ones = np.ones(4) #bize 1ler verdi ve float
print(deneme_ones)
print(deneme_ones.dtype)

print('---------------------------')

#bunlarin biraz parametreleri ile oynayarak farkli array'ler elde edebiliriz
deneme_zeros_multi = np.zeros((3, 6, 6), dtype=np.int32) #guzel gozuktu UwU bu 3 boyutlu array oldu
print(deneme_zeros_multi)

print()

deneme_ones_multi = np.ones((4,5)) # 4 satir 5 sutunlu array 
print(deneme_ones_multi)

print('---------------------------')


#np.full 
deneme_full = np.full((2,3),10.0)# veri tipi sonda verdigimiz parametreye gore oluyor yani bu float
print(deneme_full)#10.0 verdik full 10.0 dolu matris verdi 
#np.full'u farkli sekilde de olusturabiliriz

zeros_to_full = 10.0 + np.zeros([2,3])
ones_to_full = 10.0 * np.ones([2,3])

print(zeros_to_full)
print(ones_to_full)#gordugumuz gibi aritmetik islemler kullanarak np.full komutunu taklit ettik 

print('---------------------------')

#np.empty ve np.fill 

deneme_empty = np.empty((2,2))#videoda random veriler verdi bende ise kodda kullandigim verileri dondurdu ALLAH ALLAH YAW, neyse bu bos array yani simdi doldurma vakti
print(deneme_empty)

deneme_empty.fill(31)#sjsjsjssjs
print(deneme_empty)#komediyim ya 😎😎

print('---------------------------')


#np.eye 

deneme_eye = np.eye(6) #bize 6x6lik birim matris verdi, diagonal(bu nasil yaziliyor bilmiyorum ve su an bunu yazarken internetim olmadigindan da bakamiyorum ) kismi 1 diger kisimlar 0 
print(deneme_eye)
print()
#tabii biraz oynamadan olmaz babus, diagonal kismini kaydirabiliriz

deneme_eye2= np.eye(6, k=1)#diagonal kismini 1 arttirdik
print(deneme_eye2)
print()

deneme_eye3= np.eye(6, k=-2)#diagonal kismini 2 azalttik 
print(deneme_eye3) 
print()

#np.eye disinda np.idendity ile de matris olusturabiliyoruz ama farki ne bilmiyorum... heee sanirim parametreler farkli ve np.eye direkt birim matris icin cunku aciklamasi oyle :D

deneme_idendity = np.identity(6)
print(deneme_idendity)

print('---------------------------')

#np.diag ise verdigimiz degerleri diagonal kisma yerlestiriyor

deneme_diag= np.diag([2,4,14,55])
print(deneme_diag)
