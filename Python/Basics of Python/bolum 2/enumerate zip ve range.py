range(10) #bak bu range 0dan 10a kadar range iste amk 
print(range(10))
[*range(10)] #bu da rangeyi list yapar elemanları iceri atar
print([*range(10)])

for x in range(10):
    if x <4:
        print(x)  #boyle if for ile kullanilabilir

print("###################################################")
###################################################
harfler = ['a','b','c','d','e']

for index, harf in enumerate(harfler): #bak enumerate listedekileri indexlemeye yaradi 
    print("{}. harf = {}".format(index+1, harf))

print("###################################################")
###################################################

ulkeler = ['TR','FR','DE']
siralama = range(1,4)

for ulke in zip(ulkeler,siralama):# zip ayni elemana sahip olan iterable'i baglar 
    print(ulke)