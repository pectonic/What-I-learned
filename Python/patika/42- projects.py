'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]



2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]


'''

#1 =================================================================================================================================================== 
l1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] #proje icin verilen ornek

def flatten(x):

    flat = []
    
    while x: #x'in ici bosalana kadar dongude kalacak
        z = x.pop() #x'in icindekilerinden son sirada olani z'ye atiyoruz ki tek tek kontrol edelim

        if type(z) == list: #z'ye atadigimizi 'list' olup olmadigini kontrol ediyoruz
            x.extend(z) #eger z bize 'list' olarak donerse 'list' tipinden degisine kadar icine girecegiz, simdilik geri atama yapiyoruz 

        else:
            flat.append(z) # z'ye atadigimiziz veri tipi 'list' degilse 'flat' degerimize aktarir
    
    return flat

print(flatten(l1))

#  ===================================================================================================================================================
#2 ===================================================================================================================================================

l2 = [[1, 2], [3, 4], [5, 6, 7]] #proje icin verilen ornek
l3 = [4 ,2 ,1,6,37] #bu test icin olusturdugum liste
l4 = [[[1,2]],[2,6,7,3],[12,[34,[65]]]] #hahaha bu tarz bir seyde hata veriliyor ama benden istenen bu degil, bu istenirse bunun cozumu icin ugrasirim :P

def reverselist(r):

    
    for x in r: #elemanlari da kontrol etmek icin for dongusu aciyorum
        if type(x) == list: #elemanlari liste tipindeyse iceri giriyorum
            x.sort(reverse=True) #elemanlari liste olanlari tersine duzenliyorum
        else: None #eger elemanlar liste degilse saliyorum cayira 
        
    r.sort(reverse=True)#burada genel tersine sifirliyorum
    return r

print(reverselist(l4))

#  ===================================================================================================================================================
