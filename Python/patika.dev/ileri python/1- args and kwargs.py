# *ARGS degisken sayida parametre vermenin yolu. list/tuple objelerini unpack yapar ama dict yapmaz.

def sum(*args): # burada args'in adi onemli degil, onemli olan bastaki budur: '*' 
    total = 0
    for x in range(len(args)):
        total += args[x]
    return total

#print(sum(1,2,3)) # sayilari def icinde tuple olarak tutar 

# **KWARGS def'e degisken sayida keyword argument verebilmemizi saglar

def student(**students):
    print(students)
    for z in students:
        print(z)

# print(student(name = "Can", surname = "Aydin")) # degerleri dict olarak tutar 


# def icinde def deneme(*args, **kwargs): sirasinda yazilir, deger verirken hata bu sekilde deneme(1,2,3, key="deneme", key2="rteden nefret ediyorum") gibi

# birlestirme islemlerinde ardi ardina koyar

l1 = [1,2,3]
l2 = [4,5]
print(l1, l2) # OUTPUT: [1, 2, 3] [4, 5]
print(*l1, *l2) # OUTPUT: 1 2 3 4 5

dict1 = {'key':'deneme',"abo":"dict zor"}
dict2 = {"key2":"aaaw","japonya":"kurtulus"}
dictSum = {**dict1, **dict2}
print(dictSum) # BUM