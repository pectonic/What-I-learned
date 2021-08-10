import numpy as np
from numpy.core.fromnumeric import size

"""1) 5 elemanli 0 ve 1 lerden olusan ndarrayleri olusturunuz  """
print('---------------Soru 1-----------------')
dnm_soru1 = np.zeros(5)
dnm_soru1_1 = np.ones(5)
print(dnm_soru1)
print(dnm_soru1_1)
print()



'''2) 7 ve 41 dahil olmak uzere aralarindaki tek sayilari gosteren ndarrayleri olusturunuz'''
print('---------------Soru 2-----------------')

dnm_soru2 = np.arange(7,42)
dnm_soru2_1 = dnm_soru2[(dnm_soru2 % 2 == 1)] 
print(dnm_soru2_1)
print()



'''3) 1 ile 10 arasinda rastgele 16 elemanli olusan 4x4 matris olusturunuz'''
print('---------------Soru 3-----------------')

dnm_soru3 = np.random.randint(1,10,size=(16,)).reshape(4,4)
print(dnm_soru3)
print()



'''4) 0.1 ile 1 arasinda esit farkli 10 elemanli bir ndarray olusturunuz'''
print('---------------Soru 4-----------------')
dnm_soru4 = np.linspace(0.1,1,num=10)
print(dnm_soru4)
print()


"""[[ 0  1  2  3  4]
    [ 5  6  7  8  9]
    [10 11 12 13 14]
    [15 16 17 18 19]
    [20 21 22 23 24]] x matrisinden [[ 7  8]
                                  [12 13]] y matrisini olusturunuz """

print('---------------Soru 5-----------------')

dnm_soru5 = np.arange(25).reshape(5,5)
dnm_soru5_1 = dnm_soru5[1:3,2:4]
print(dnm_soru5_1)
print()


'''6) elemanlari 1 ile 17 arasindaki  sayilardan olusan 4x4 x matrisindeki cift sayilarin Boolean index ile alarak 2x4luk y matrisini olusturalim'''
print('---------------Soru 6-----------------')

dnm_soru6 = np.arange(1,17).reshape(4,4)
dnm_soru6_1 = dnm_soru6[(dnm_soru6 % 2 ==0)].reshape(2,4)
print(dnm_soru6_1)
print()


'''7) Sinamaya giris ucreti ogrenciler icin 5TL olmayanlar icin 10TL, 100 kisi icin 700TL topladigina gore ogrenci sayisi kactir? x+y=100, 5x + 10y =700 '''
print('---------------Soru 7-----------------')

dnm_soru7 = np.array([[1,1],[5,10]])
print(dnm_soru7)
dnm_soru7_1 = np.array([100,700])
print(dnm_soru7_1)

dnm_soru7_x = np.linalg.solve(dnm_soru7,dnm_soru7_1)
print(dnm_soru7_x)

print()



'''8) tek boyutlu ve cift boyutlu ndarrayler icin skaler carpim ornekleri gosteriniz'''
print('---------------Soru 8-----------------')

dnm_soru8 = np.random.randint(1,10, size=(10,))
dnm_soru8_1 = np.random.randint(1,10, size=(10,))
print(dnm_soru8)
print()
print(dnm_soru8_1)
print()
print(np.dot(dnm_soru8,dnm_soru8_1))
print()

dnm_soru8_2 = np.random.randint(1,10, size=(10,)).reshape(5,2)
dnm_soru8_3 = np.random.randint(1,10, size=(10,)).reshape(2,5)
print(dnm_soru8_2)
print()

print(dnm_soru8_3)
print()

print(np.dot(dnm_soru8_2,dnm_soru8_3))

