l1 = [[1, 2], [3, 4], [5, 6, 7]] #proje icin verilen ornek
l3 = [4 ,2 ,1,6,37] #bu test icin olusturdugum liste
l4 = [[1,2,3],[[4,5,6]],[[[7,8,9,[10,12,13]]]]]
def flatten(x):

    flat = []
    
    while x: #x'in ici bosalana kadar dongude kalacak
        z = x.pop() #x'in icindekilerinden son sirada olani z'ye atiyoruz ki tek tek kontrol edelim

        if type(z) == list: #z'ye atadigimizi 'list' olup olmadigini kontrol ediyoruz
            
            z.sort(reverse=True)
            flat.append(z)
        else:
            z.sort(reverse=True)
            flat.append(z)
    flat.sort(reverse=True)
    return flat

print(flatten(l3))