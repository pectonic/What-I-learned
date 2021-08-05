import numpy as np

#np.zeros ve np.ones 

deneme_zeros = np.zeros(4) #bize 0lar verdi ve float
print(deneme_zeros)
print(deneme_zeros.dtype)

print('---------------------------')

deneme_ones = np.ones(4) #bize 1ler verdi ve float
print(deneme_ones)
print(deneme_ones.dtype)

print('---------------------------')

#bunlarin biraz parametreleri ile oynayarak farkli array'ler elde edebiliriz
deneme_zeros_multi = np.zeros((3, 6, 6), dtype=np.int32) #guzel gozuktu UwU bu 3 boyutlu array oldu
print(deneme_zeros_multi)

print()

deneme_ones_multi = np.ones((4,5)) # 4 satir 5 sutunlu array 
print(deneme_ones_multi)