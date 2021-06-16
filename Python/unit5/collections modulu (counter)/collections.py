from collections import Counter # OYYYY HAREKETI GORDUN MU LNA, neyse buyuk baslik altinda alt basligi cektik, performance upgrade
import random 

liste1 = random.sample(range(10), k=4)
liste2 = random.sample(range(10), k=4)
liste3 = random.sample(range(10), k=4)
liste4 = random.sample(range(10), k=4)

liste_listesi = [liste1,liste2,liste3,liste4]

liste_toplam = liste1 + liste2 + liste3 + liste4

print(liste_listesi)
print(Counter(liste_toplam))