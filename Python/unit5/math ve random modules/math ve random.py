import random

#print(help(random)) # komutlari tatli dille anlatiyor __dir__ yerine kullanilabilen bir kod

print(random.random()) #bu 0 ile 1 arasinda random
print(random.uniform(5,10)) # bu da istedigimiz defer arasinda ama float
print(random.randint(5,10)) # bu da usttekinin aynisinin int versionu
print(random.choice(range(10))) # choise secmek ama liste koymali icine range ozellik tasiyor
print(random.sample(range(10), k=4)) # bu ise yukaridakinin aynisi ama k verisi kac tane sececegini belirtiyor

liste = [*range(10)]
print(liste)

random.shuffle(liste) #rasgele siraliyor

import math

#print(help(math)) #math yardim aman amk cikamiyoruz sonr

print(math.ceil(8.1)) # tavana ve
print(math.floor(9.99)) # zemine yuvarlar
print(math.factorial(6)) # FaCtOrIyEL bAbU
print(math.pow(5,2)) # ust alma (5in ustu 2)
