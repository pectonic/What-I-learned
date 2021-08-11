import pandas as pd
#bu derste loc/iloc/len/list/dict/sorted/max/drop/min, pandas Series indexing olayi islendi



""" series elemanlarina nasil ulasiriz ve degistiririz """
print('---1-------------------------------------------------------------------')

student = pd.Series(data=['Can Ahmet','Aydin',20,'Agriculture'], index=['name','surname','age','department'])
student = pd.Series(['Can Ahmet','Aydin',20,'Agriculture'],['name','surname','age','department']) #evet ustteki ile bu ayni 

print(student)
print()

print(student['name']) #bu sekilde ulasabiliyoruz
print(type(student['name']))
print()

print(student[['name', 'department']])#bu sekilde de coklu cagirim yapabiliyoruz
print(type(student[['name', 'department']]))# bu bu sekilde cagirim Series oluyor ama yukarida teklide olmadi
print()

print(student[1])#evet her ne kadar indexlerini kendimiz yazsak da hala 0,1... diye indexleri duruyor ki guzel amk 
print()
print(student[[0,1]])
print()
print(student[0:3])
print()
print(student[-2])
print()
print(student[0:])
print()
print(student[-2:])
print()
print(student['name':'department']) #bunun ile [0:4] ayni mi? yoo biris yariacik aralik digeri kapali aralik 
print()

print('---2-------------------------------------------------------------------')

# loc --> location, iloc --> index location

print(student.loc['department'])
print()
print(student.iloc[1])# iloc kullanirken kesinlikle index numarasi kullanilir
print()

print(student)
print()
student['name'] = 'Kelek'
student.iloc[2] = 21
print(student) 
print()
#yani buradan anlayacagimiz Pandas Series --> Mutable (tekrar degistirilebilir), peki silebilir miyiz?


print(student)
student.drop('name')#evet dropladik
print(student) #AAAAAAAaaa olmadi la, olmaz tabii. Bir veri bu kadar kolay bozulamaz. Ama soyle bir sey yapilabilir
student2 = student.drop('name')
print(student2)#evet bu sekilde boyle oldu ama istersen ben sadece silmek istiyorum onunda caresi var.
""" student.drop('name', inplace=True) """#evet bu komut direkt siliyor 
print()

print('---3-------------------------------------------------------------------')
print(student)
print()
print(len(student)) #e uzunluk babba
print(list(student)) # datalari list seklinde veriyor
print(dict(student)) #dict seklinde veriyor yani key ve valueler belli oluyor
print()


""" print(sorted(student)) """ #bu hata veriyor cunku int ile texti nasil siralasin
student3 = pd.Series(data=['Can Ahmet','Aydin','Agriculture'], index=['name','surname','department'])

print(sorted(student3)) #alfabeye gore siraladi
print(max(student3))#bu da siralamanin en sonundakini veriyor 
print(min(student3))# e bu da ilki gosterir

