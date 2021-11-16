# f-string de yaptığımız tek şey aslında değişkenlerin değerlerini veya hesaplamaların sonucunu stringin içine gömmek.

x = 3

print("x in değeri" + " " + str(x)) # uzuuun uzun yerine 

print(f"X in degeri {x}") # OYYYYYYYYYYYYY 

print(f"X in degeri {x+2}") # isleme bile sokabiliyoruz POG

# sadece int icin degil her amk cocugunu ekleyebiliriz

isim = 'Can'
l = [1,2,3,4]
d = {1:2,31:5,552:5}

print(f'Isminiz : {isim}')
print(f'Liste : {l}')
print(f'Dic : {d}')

def kare(x):
    return x*x

print(f'{x} in karesi: {kare(x)}') 