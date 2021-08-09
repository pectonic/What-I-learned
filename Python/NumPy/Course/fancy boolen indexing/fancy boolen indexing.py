import numpy as np
from numpy.core.fromnumeric import size

deneme_index1 = np.linspace(1,21,11)
print(deneme_index1)
print()
deneme_index2 = np.array([1,4,10])
print(deneme_index2)
print()
print(deneme_index1[deneme_index2]) #deneme_index1'i farkli bir array ile indexledik

print('------------------------------------')


#matrislerde de yapalim ve burada onemli olan sey bir arrayi farkli bir arrayle indexlememiz, bunun normal indexlemeden farkli memory_sharenin false donmesi. Bunun ismi Fancy Indexing oluyor.
deneme_index3 = np.arange(25).reshape([5,5])
print(deneme_index3)
print()
deneme_index3_1 = np.array([1,2])
print(deneme_index3_1)
print()
print(deneme_index3[deneme_index3_1,:])
print()
print(deneme_index3[:,deneme_index3_1])
print()

deneme_fancy_index = np.array([1,2])
deneme_index3_2 = deneme_index3[deneme_fancy_index,:]
print(deneme_index3_2)
print()
deneme_index3_2[0,0] = 99 
print(deneme_index3_2)
print()
print(deneme_index3)
print()

#ya da
print(np.shares_memory(deneme_index3,deneme_index3_2))
print('---------------------------------------------------')



#boolen indexing
#aslinda bizim yukarida yapigimiz indexleminin pek bir anlami yok cunku yapay zekada biz arraylerin degerlerini falan bilmeyecegiz, bu nedenle AI'de boolen indexing yapilir diye duydum :P
deneme_boolen1 = np.arange(10)# soyle ornek vereyim, dusunun 10a kadar deger verdik ama bu 1000x1000 bir matrix olabilir o yuzden mantiksal bir indexlemeye ihtiyaci var
print(deneme_boolen1)
print()
deneme_boolen1_2 = deneme_boolen1[(deneme_boolen1 % 2 == 0)] #biz de mantikli sekilde indexlememizi yapiyoruz 
print(deneme_boolen1_2)
print()
#ve booeln indexing de fancy indexingte oldugu gibi non memory share'dir
deneme_boolen1_2[0] = 99
print(deneme_boolen1_2)
print()
print(deneme_boolen1) 
print()

#ya da 
print(np.shares_memory(deneme_boolen1,deneme_boolen1_2))
print('--------------')

#farkli bir ornek

deneme_random1 = np.random.randint(10, size = 10)
deneme_random2 = np.random.randint(10, size = 10)
print(deneme_random1)
print(deneme_random2)

deneme_boolen2 = deneme_random1>deneme_random2
print(deneme_boolen2)
print(type(deneme_boolen2))
print((deneme_boolen2).dtype)
print()

#mantiksal demisken if else aklima geldi, zaten derste de orada kullandigimiz || ya da && kosullarina benzer numpy komutlari var

print(np.all(deneme_random1>deneme_random2))#hepsi 
print(np.any(deneme_random1>deneme_random2))#bi dane olsa bile yeter

print('------------')

#maskeleme mi? bakalim neymis, ne icin kullanilirmis

deneme_linspace = np.linspace(1,21,11)
print(deneme_linspace)
print()
deneme_mask = (deneme_linspace % 3 == 0)
print(deneme_mask)
print(type(deneme_mask))
print(deneme_linspace[deneme_mask]) #iste bu maskeleme bebegim
print()

deneme_linspace[deneme_mask] = -(3+1) #sj? evet dostum s ve kadim dostu j
print(deneme_linspace)









print()


