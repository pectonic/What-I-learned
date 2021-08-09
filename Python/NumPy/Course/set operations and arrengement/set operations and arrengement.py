import numpy as np
from numpy.core.fromnumeric import size

#bu derste np.intersect1d/setdiff1d/union1d/in1d/unique/sort kullanilmis ve ogrenilmistir


#genelde set operations'lari iki tane NDarray karsilistarirken kullaniriz

print('------------------1--------------------')
print()
deneme_set_op1 = np.array([2,5,6,3,9])
deneme_set_op2 = np.array([7,1,3,5,8])

deneme_set_op_test1 = np.intersect1d(deneme_set_op1,deneme_set_op2)#bu kod kesisim kumesini gosterir
print(deneme_set_op_test1)
print(type(deneme_set_op_test1))
print()

deneme_set_op_setdiff1 = np.setdiff1d(deneme_set_op1,deneme_set_op2)#op1'de olup op2'de olmayanlari gosterecek
print(deneme_set_op_setdiff1)
print()

deneme_set_op_tsetdiff2 = np.setdiff1d(deneme_set_op2,deneme_set_op1)#op2'de olup op1'de olmayanlari gosterecek
print(deneme_set_op_tsetdiff2)
print()

deneme_set_op_union = np.union1d(deneme_set_op1,deneme_set_op2)#birlesim kumesi ve ortak elemanlari iki kere yazmaz
print(deneme_set_op_union) 
print()

deneme_set_op_in = np.in1d(deneme_set_op1,deneme_set_op2)#op1'dekileri op2'de olup olmadigini kontrol ediyor
print(deneme_set_op_in)
print()

deneme_set_op3 = np.array([1,2,3,4,5,6,7,7,7,8,9,3,4,3,2,4])
print(np.unique(deneme_set_op3))#tekrarlayan elemanli yok sayarak unique bir ndarray verdi, unique itemler be PoE oynamayi ozledim amk
print()

print('------------------2--------------------')
print()

#simdi siralama sort zamani

deneme_random = np.random.randint(20 , size=(10,))
print(deneme_random)
print(np.sort(deneme_random))#np.sort siralamaya yaradi ama nonmemory olarak, bunu kayit altinta tutmak istiyorsak soyle yapabiliriz
print(deneme_random)
print()

deneme_random.sort() #bu bize siralamayi kaydetmeyi saglar
print(deneme_random)
print()

#simdi de matrisler icin bakalim

deneme_random2 = np.random.randint(10 , size= (5,5))
print(deneme_random2)
print()
print(np.sort(deneme_random2 , axis=0)) # axis = 0 sutunlara gore siralar
print()
print(np.sort(deneme_random2, axis=1)) # asix = 1 satirlara gore siralar
