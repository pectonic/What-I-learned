import numpy as np
from numpy.core.fromnumeric import size

#bu derste np.add/subtract/multiply/divide/array_equal/sqrt/power/exp ve element.sum/min/max/argmin/argmax kullanilmis ve ogrendilgi dusunuluyor

#element-wise(aritmatik islemler) ve array-wise
#element-wise tek tek elementlere etki eden islemler
#array-wise ise diret array uzerine etki eden islemler


print('------------------1--------------------')

deneme_random_1 = np.random.randint(1,10, size=(5,))
print(deneme_random_1)

deneme_random_2 = np.random.randint(1,10, size=(5,))
print(deneme_random_2)
print()
#ONEMLI NOT: element-wise islemlerde ya shapeleri ayni olacak ya da broadcast olayi olacakmis, broadcast terimi icin ayri bir ders olacakmis hmmm
print(deneme_random_1 + deneme_random_2)
print(np.add(deneme_random_1,deneme_random_2)) #ikisin de type'i ndarray yani ikisi de tamamen ayni islem ama yine de kanit gosterelim
print()
print(type(deneme_random_1 + deneme_random_2))
print(type(np.add(deneme_random_1,deneme_random_2))) 
print()

#bunlar tum dort islemler icin gecerli

print(deneme_random_1 - deneme_random_2)
print(np.subtract(deneme_random_1,deneme_random_2))
print()

print(deneme_random_1 * deneme_random_2)
print(np.multiply(deneme_random_1,deneme_random_2))
print()

print(deneme_random_1 / deneme_random_2)
print(np.divide(deneme_random_1,deneme_random_2))
print()

#ve bir ndarray'i bir tam sayi ile isleme sokabiliriz

print(deneme_random_1 + 3)
print(deneme_random_1 - 3)
print(deneme_random_1 * 3)
print(deneme_random_1 / 3) #sikintisiz devam 
print()
#arraylerin birbirine esit olup olmadigini np.array_equal ile kontrol edecegiz

print(np.array_equal(deneme_random_1,deneme_random_2)) 

deneme_array1 = np.array([1,2,3])
deneme_array2 = np.array([1,2,3])

print(np.array_equal(deneme_array1,deneme_array2))
print()

#simdi farkli mat islemlerine bakalim

deneme_random_3 = np.random.randint(10, size=(6,))
print(deneme_random_3)
print(np.sqrt(deneme_random_3))
print(np.power(deneme_random_3, 3))
print(np.exp(deneme_random_3))
print()

#simdi bir seyler yapacagiz 

deneme_random_4 = np.random.randint(1,10, size=(9)).reshape(3,3)
print(deneme_random_4)
print(np.sum(deneme_random_4))
print(deneme_random_4.sum(axis = 0))#sutunlari topla
print(deneme_random_4.sum(axis = 1))#satirlari topla
print(deneme_random_4.min())
print(deneme_random_4.max())
print(deneme_random_4.argmin())#bu ndarray'de min degerli sayinin indexini veriyor
print(deneme_random_4.argmax())#bu ndarray'de max degerli sayinin indexini veriyor 


