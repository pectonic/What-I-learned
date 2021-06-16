#break islemi bitirir

harfler = ['a','b','c','d','e']*100

for index,harf in enumerate(harfler):
    if harf == 'c':
        print("{} harfi {}. indexte".format(harf, index))
        break #break yazmaksak 500 tane itemi de gezecekti, gereksiz veri kullanimi

print("###################################################")
###################################################
#continue devamke anlamina gelir yani donguyu basa sarar

#problem: tek sayileri bul
for sayi in range(1,6):
    if sayi%2==0:
        continue #eger sayi cift ise basa sarar
    print(sayi)

print("###################################################")
###################################################
#pass ise olan kisim false ise gecmeyi yarar, izle simde keke

for sayi in range(1,6):
    if sayi%2==0:
        pass #eger sayi cift degilse bir sonraki adima gec
    else:
        print(sayi)