import numpy as np
from numpy.core.fromnumeric import reshape

#sa, bu derste element.mean()/srd()  ve np.median

print('-------------1--------------')
deneme_random1 = np.random.randint(1,10, size=(8,))
print(deneme_random1)
print()
print(deneme_random1.mean()) #aritmatik ort
print()
print(np.median(deneme_random1)) # medyani verir
print()
print(deneme_random1.std())#standart sapma 
print('----------2----------')

#bunlari matris icin de yapalim

deneme_random2 = np.random.randint(1,10, size=(4,3))
print(deneme_random2)
print()
print(deneme_random2.mean(axis=0))
print()
print(np.median(deneme_random2,axis=1))
print()
print(deneme_random2.std(axis=0)) 
print('----------------3----------------')

#simdi broadcasting hakkinda bir seyler gorelim. Anladigim kadariyla broadcasting sekilleri birbirne ugmayan ndarrayleri sekillerini uygun hale getirmeye yariyor

deneme_random3 = np.random.randint(1,10, size=(1,))
print(deneme_random3)
print()

deneme_random4 = np.random.randint(1,20, size=(5,3))
print(deneme_random4)
print()

print(deneme_random3 + deneme_random4) #olay tam olarak bu, 1x1 matrisi 5x3 matrisle toplayabilmek ama bunun olabilitesi olmasi gerekiyor, demek istedigim her iki matris birbiri ile uyumlu degil, ornek olarak:
print('***************')
""" deneme_random3 = np.random.randint(1,10, size=(3,)) 
print(deneme_random3)
print()

deneme_random4 = np.random.randint(1,20, size=(5,2)) 
print(deneme_random4)
print()

print(deneme_random3 + deneme_random4) #burada hata aliriz cunku random3 matrisi random4 matrisi ile uyumlu degil, broadcast yapilamaz!

"""

#bunun yaninda guzel bir ornek daha BUM

deneme_random5 = np.random.randint(1,10, size=(3,1)) 
print(deneme_random5)
print()

deneme_random6 = np.random.randint(1,20, size=(1,3))
print(deneme_random6)
print()

print(deneme_random5 + deneme_random6)# 3x1 matris ile 1x3 matris uyumlu hale gelerek 3x3 matris oluyor ve huzur icinde bu kod icinde uzun yillaaaaaaaaaaaaaar boyunca github'da yasiyor olacak...
