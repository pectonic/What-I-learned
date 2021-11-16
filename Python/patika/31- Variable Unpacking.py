#bir satirda birden fazla deger atama

x, y = (3,1)
print(x)
print(y)
print('============================================================================')

#x, y, z = (3,2,45,1,23,5) #hata verecektir
x, y, *z = (3,2,45,1,34,5)
print(x)
print(y)
print(z) #list
print('============================================================================')

x, _ = (4,5) #burada `_` vermemizin nedeni fazladan olarnlari kullanmayacagim bir degiskene atamak 
x, w, y, *_ = (4,7,8,3,43,55,4,654,75,47,547,5,435,24,21,421,5,3,534,6,547,2,65,7,6)
print(x)
print(w)
print(y)
print(_) #kullanilmayacak olsa da degerleri tutar
print('============================================================================')

x, y, *z, e = (3,4,5,6,2,621,5,63) # buradaki olay yildizli degiskenin bosta kalanlari almasi, yani yildizli sonda olmak zorunda degil
print(x)
print(y)
print(z)
print(e) # degiskenleri tanimlarken sonda oldugundan son veriyi aldi 

# `*` yildiz sembolu GERIYE KALAN HEPSINI AL demek. Bu yuzden iki tane kullanamazsin



