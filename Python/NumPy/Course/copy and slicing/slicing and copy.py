import numpy as np

#bu derste slicing yontemini ve memory share mantigi incelenmis ve ogrenilmis olarak dusunulmustur :D ayrica np.copy de gorduk


# ndarray[start:end]/[start:]/[:end] 

deneme_arange = np.arange(10)
print(deneme_arange)
print()
print(deneme_arange[3:8])#3. indexten basla 8. indexe kadar
print()
print(deneme_arange[5:])#5. indexten basla sona kadar
print()
print(deneme_arange[:6])#en bastan basla belirttigimiz indexe yani 6. indexe kadar dewam et 
print()
#matrisler icin bakalim

deneme_arange2 = np.arange(25).reshape(5,5)
print(deneme_arange2)
print()
print(deneme_arange2[0:3,1:4])
print()
print(deneme_arange2[::])
print()
print(deneme_arange2[2:])
print()
print(deneme_arange2[:,3:])
print('--------------------------------------------')

#bu islemler slicing islemi oluyor ama simdi KRITIK BIR YERE GELDIK HEM DE COK CRIT

deneme_memory = np.arange(9).reshape(3,3)
print(deneme_memory)
print()
deneme_memory2 = deneme_memory[1:2,0:2]
print(deneme_memory2)
print()
#BAK DIKKATLI INCELE
deneme_memory2[0,0] = 100 
print(deneme_memory2) #eee normal diyorsun ama simdi sana bir sey gosterem agam benim, biz deneme_memory2 degistirdik ama farkli seylerde degisti bak
print()
print(deneme_memory)#olum kodlamada ilk defa boyle birsey gordum la, bunun nedeni ise bu iki degiskenin birbiri ile baglantili olmasi, birbiri ile baglantili olmasini da np.share_memory(x,y) kodu ile ogrenebiliriz
print()
print(np.shares_memory(deneme_memory,deneme_memory2))#true donerse senindir donmezse hicbir zaman senin olmamistir yani true ise baglantilidir :))))))))))))))))))))))) yeni seviye bebegiiiiimm
#yani biz slicing islemi yapip farkli degiskene atarken aslinda ana array'yimizin bir goruntusunu atmis oluyoruz, gercek bir degisken degil de array'in imagine allahim neleeeeer!!! cok iyi amk
print('---------------------------------------------------')


#ama dersen iliskisi olmasin kardesim, o zaman np.copy kullanacagiz

deneme_copy = np.arange(16).reshape(4,4)
print(deneme_copy)
print()
deneme_copy2 = np.copy(deneme_copy[1:3,1:3])#evet kopyalama islemi tamamdir simdi baglantili olup olmadigina iki yontemle de bakalim
print(deneme_copy2) 
print()
deneme_copy2[0,0]=99
print(deneme_copy2)
print()
print(deneme_copy) #evet degismemis
print()
print(np.shares_memory(deneme_copy,deneme_copy2))#false yani baglanti yok
print()
#copy yapmanin farkli biz yazimina da bakalim

deneme_copy3 = deneme_copy[:,2:3].copy() #bu da farkli bir yazim sekli
print(deneme_copy3) 