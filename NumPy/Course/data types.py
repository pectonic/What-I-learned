import numpy as np

#numpy bircok veri tipini destekler ama bunlardan 5'i en cok kullanilanlardir: boolen, int, float, complex, unsigned integers(sanirim str'den bahsediyor)

x = np.array([1,2,3], dtype=np.int32) #disarida dtype ayarlayabiliyoruz ki istemedigimiz veriyi almayalim 
print(x)
print(x.dtype)

print('-----------------------')

y = np.array([1,2,3], dtype=np.float64)
print(y)
print(y.dtype)

print('-----------------------')

z = np.array([1,2,3], dtype=np.complex128)
print(z)
print(z.dtype)

print('-----------------------')

k = np.array([1.3,2.5,3.9], dtype=np.int32) #dtype int olmasina ragmen float degerler verdik ama hepsini int yapti without yuvarlama islemi
print(k)
print(k.dtype) #yaptigimiz bu isleme DOWNCAST islemi deniliyor

print('-----------------------')

#simdi de ayni array'i farkli veri tipine convert edelim

g = np.array([1,2,3,4], dtype=np.float64)
print(g)
print(g.dtype)


print()
#simdi burada iki yontem var, birisi ayni sekilde yazarak 'g = np.array(g, dtype=complex)' seklinde yazabiliriz veya .astype kullaniriz

g = g.astype(np.complex128)
print(g)
print(g.dtype)


print('-----------------------')

#sirada arrayler kendi arasindaki islemlerde nasil davrandigi

x1 = np.array([1,2,3,4], dtype=np.int32)
x2 = np.array([3.2,4.5,6.7,1.3], dtype=np.float64)

print(x1 + x2)
print((x1 + x2).dtype) #int ve float arasidan float daha kapsamli oldugu icin floata cevirdi, unutma KAPSAMLAMLI OLANA cevrilir


print('-----------------------')
#veri tipimiz yaptigimiz isleme uygun olmak zorundadir!

o = np.sqrt(np.array([-1,9,4], dtype=np.float64)) #burada -1 kok icinde complex sayi oldugundan bize 'nan' degerini dondu ama biz bunu bize uygun veri tipine cevirirsek islem sorunsuz isleyecektir
print(o)
print(o.dtype)

print()

o = np.sqrt(np.array([-1,9,4], dtype=np.complex128))
print(o)
print(o.dtype) #basarili ama istersen bu sonucun real ve imagine kismini alabiliriz

print(o.real)#sadece real kismini aldik
print(o.imag)#burada da sadece imag kismini yani sanal kismini aldik


