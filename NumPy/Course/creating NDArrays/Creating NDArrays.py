import numpy as np
from numpy.core.fromnumeric import shape

#buradaki array ile pythondaki list arasindaki en buyuk fark np.array ayni data tipindekileri tutar

x = np.array([10,11,12,13])
print(x)

print(type(x))#class'ini veriyor bize('numpy.ndarray')

print(x.shape)#eksendeki eleman sayilarini gosteriyor ve bu tek eksenli oldugunda sonuc '(4,)' seklindedir
print(x.size)#toplam eleman sayisi
print(x.ndim)#boyut sayisini veriyor
print(x.nbytes)#verinin boyutunu byte olarak gosterir
print(x.dtype)#veri tipini gosterir

#simdi de iki boyutlu array'in ozelliklerine bakalim
print('###########################################################################################') #kodlar karmasik gozukmesin diye yapiyorum ama bos kod bosa performans harcar, yapilmamasi gereken bir sey

y = np.array([[1,2,3],[4,5,6]])

print(y)

print(type(y))
print(y.shape) # (2,3) dedigi 2 rolls(satirlari), 3 ise satirlardaki eleman sayisi
print(y.size)
print(y.ndim)# hoop 2 boyutlu be aslan be
print(y.nbytes)
print(y.dtype)

#sirada uc boyutlu array olusturmakta B)
print('###########################################################################################')

z = np.array([[1,2],[3,4],[5,6]])

print(z)

print(type(z))
print(z.shape)#bize gercekten arraylerin seklini veriyor babba, 3 satir 2 sutun muuu abooo
print(z.size)
print(z.ndim)# lan ben 3 boyutlu oldu sandim ama bu yanlis amk, heeeeee hizli kosan atin boku seyrek duser gibi bir laf vardi :DDDD neyse asagida dogrusunu yapalim
print(z.nbytes)
print(z.dtype)


print('###########################################################################################')

f = np.array([[[1,2],[2,3]],[[3,4],[4,5]]])

#simdilik digereri onemli degil asil bunlarla ilgilenelim
print(f.shape) #simdi bize (x, y, z) diye sonuc veriyor bunu da soyle aklimizda tutabiliriz: x tane y*z matris 
print(f.ndim) # bu da bize 3 boyutlu array verir


#sirada np.arrayler icinde veriler nasil oluyor ona bakalim
print('###########################################################################################')


np_normal = np.array([1,2,3])
print(np_normal.dtype) # burada bildigimiz array'imiz var
print(np_normal)


np_str = np.array([1,'2',3])
print(np_str.dtype)# hani tek tip idi lan... burada icine yabanci girerse hepsini ona cevirdigini gorecegiz
print(np_str)


np_float = np.array([1,2.0,3])# uzum uzume baka baka karardi maan 
print(np_float.dtype)
print(np_float)
