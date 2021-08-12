import pandas as pd
from pandas.core.series import Series
#hi pandas ^-^

print('-1--------------------------------------------------')

student = ['Can Ahmet', 20, 'Agriculture']
print(student)
print(type(student))

print()

ps_student = pd.Series(student)
print(ps_student)#listten Series olusturdu, indexleri de 0'dan baslayip gidiyor
print(type(ps_student))
print()

print('-2--------------------------------------------------')

student2 = {
    'name' : 'Can Ahmet',
    'age' : 20,
    'department' : 'Agriculture'
}

print(student2)
print(type(student2))

print()

ps_student2 = pd.Series(student2)
print(ps_student2) #bu sefer indexleri dict'in keylerini alarak Series olusturdu
print(type(ps_student2))
print()

print('-3--------------------------------------------------')

#tabii direkt olarak da Series olusturabiliriz 
student3 = pd.Series(['Can Ahmet',20,'Agriculture'])
print(student3)
print(type(student3)) #dtype: object
print()

numbers = pd.Series([32,142,54])
print(numbers)
print(type(numbers))# dtype: int64
print()

booleans = pd.Series([True,False,False])
print(booleans)
print(type(booleans))#dtype: bool
print()



print('-4--------------------------------------------------')

#istersek datayi ve indexi kendimiz yazariz

student4 = pd.Series(data=['Can Ahmet', 20, 'Agriculture'], index=['name','age','department'])
print(student4)
print(type(student4)) 
print()

#attribute : nitelik, ozellik alnamina gelir. Ve biz de Series'in attributelerini inceleyecegiz

print(student4.values)
print()
print(student4.index)
print()
print(student4.shape) # sekli
print()
print(student4.ndim)# boyut
print()
print(student4.size)# size
print()
print(student4.name) #isim ama daha atanmadigindan none
print()
print(student4.dtype)
print()
student4.name = 'Yarraaaaa'
print(student4.name) #simdi ismi dondurdu 
print()



print('-5--------------------------------------------------')

#bir degeri veya indexi o Series icinde olup olmadigin kontrol edelim

x = 'name' in student4#bu sekilde yazilirsa indexler arasinda arama yapar
print(x)
print()

y = 'job' in student4
print(y)
print()

x2 = 'Can Ahmet' in student4.values #degerler icin de .values attributeyi kullanmamiz gerekiyor
print(x2)
print()

y2 = 'Annen' in student4.values
print(y2)
print()

print('-6--------------------------------------------------')

numbers2 = pd.Series([4 , 2.5, 5])
print(numbers2)
print(numbers2.sum()) #toplama
print(numbers2.mean()) #ortalama
print(numbers2.product()) # verilerin carpimi
