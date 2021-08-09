import numpy as np

#bu derste np.hstack/vstack/insert/append/delete kodlari incelenmis ve ogrenilmistir diye dusunulmustur :D 


deneme_index_alma = np.arange(5,10)
print(deneme_index_alma)
print(deneme_index_alma[0])
print(deneme_index_alma[5-1])#5 elemanli bi array oldugundan bize son indexteki elemani verecek
print('---------------------------------------------------')
#simdi de negatif indexlere bakalim
print(deneme_index_alma[-1])#burada sondan 1. index -1 olarak basliyor ne de olsa normalde 0 1. indexi temsil ediyor
print(deneme_index_alma[-2])
print(deneme_index_alma[-5])#yukaridaki nedenden dolayi kac elemanliysa -x verdigimiz zaman bize sondan sonuncu elamni yani aslinda normalin 1. indexini dondurecektir
print('---------------------------------------------------')

#nasil degisiklik yapacagimiza bakalim

deneme_index_alma[2] = 221 #2. indexteki degeri degistirdik
print(deneme_index_alma)
print(deneme_index_alma[2])
print('---------------------------------------------------')

#2d zamani

deneme_2d_index_alma = np.arange(12).reshape(3,4)
print(deneme_2d_index_alma)
print(deneme_2d_index_alma[0,2])#0 indexteki satirin 2. indexini istedik yani x[row, column]
print('---------------------------------------------------')
#degisilik yapim?
deneme_2d_index_alma[2,3] = 666
print(deneme_2d_index_alma)
print(deneme_2d_index_alma[2,3])
print('---------------------------------------------------')

#np.delete

deneme_delete1 = np.arange(10)
print(deneme_delete1)
deneme_delete2 = np.delete(deneme_delete1, [0,10-1])#ya burada son elemanin 9. indexte oldugunu biliyorum ama amk bu nasil yoldur son elemani bulmak icin olm son eleman - 1 nedir, baska yol mu yok
print(deneme_delete1)
print(deneme_delete2)
print('----')
#np.delete ama 2d burada axis=0 row satir, axis = 1 column satir

deneme_delete3 = np.arange(16).reshape(4,4)
print(deneme_delete3)
print()
deneme_delete3 = np.delete(deneme_delete3, 2, axis=0)#direkt satiri sildi
print(deneme_delete3)
print()

deneme_delete3 = np.delete(deneme_delete3, [0,3], axis=1)
print(deneme_delete3)
print('---------------------------------------------------')

#np.append

deneme_append = np.arange(8)
print(deneme_append)
deneme_append = np.append(deneme_append, [40,925])#sona eklemeye yaradi
print(deneme_append)
print('-------')
#simdi de 2d arraylerde nasil isliyor ona bakalim

deneme_append2 = np.arange(9).reshape(3,3)
print(deneme_append)
print()
deneme_append2 = np.append(deneme_append2 , [[333,444,555]], axis=0)#son satira bir 3lu ekledik 
print(deneme_append2)
print()
#simdi column ekleyecegiz bu da uyumlu olmasi acisindan 4 elemanli olmali
deneme_append2 = np.append(deneme_append2, [[232],[6665],[4124],[6346]], axis = 1)#her satira ozel koseli parantez cunku ayrilar baba
print(deneme_append2)
print('---------------------------------------------------')

#np.insert => np.insert(ndarray, index, element, axis)

deneme_insert = np.arange(5)
print(deneme_insert)
deneme_insert = np.insert(deneme_insert, 1, 99)#1. indexe 99 ekle dedim, ekledi...
print(deneme_insert)
print()
#simdi 2d 
deneme_insert2 = np.arange(4).reshape(2,2)
print(deneme_insert2)
print()
deneme_insert2 = np.insert(deneme_insert2, 1, [79,64], axis=0 ) #boylelikle 1. indexteki satira yeni bir array ekledik veya stuna da ekleyebiliriz
print(deneme_insert2)
print('---------------------------------------------------')

#UNUTMA EGER EKLEDIGIN ELEMENTLER DUZENI BOZARSA HATA ALIRSIN, YANI KELEGINE VURDUGUM 3X3 MATRISE 2X2 ELEMANI EKLERSEN HATA ALIRSIN 😉✌

#np.stack arrayleri birbirine baglama buyusu olabilir sj

deneme_stack1 = np.arange(3)
print(deneme_stack1)
print()
deneme_stack2 = np.arange(9).reshape(3,3)
print(deneme_stack2)
print()
deneme_stack3 = np.vstack([deneme_stack1,deneme_stack2])#1.yi al 2.nin ustune koy, vstack= vertical stack oluyor, bir de bunun horizontal stack versitonu var
print(deneme_stack3)
print('--------')

deneme_stack4 = np.arange(4).reshape(4,1)
print(deneme_stack4)
print()
deneme_stack5 = np.hstack([deneme_stack4, deneme_stack3])# horizontal stack 
print(deneme_stack5)
