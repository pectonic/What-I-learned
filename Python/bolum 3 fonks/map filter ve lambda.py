def karesini_al(x):
    return x**2

sayilar = [*range(1,6)]
#print(sayilar)

for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])
    
#print(sayilar)

#ust taraf yerine map ile her liste elemanina funcu uygulamaya yarar

sayilar = [*range(1,6)]
print(sayilar)

print([*map(karesini_al, sayilar)])

def cift_sayilari_topla(x):
    return x if x % 2 == 0 else None

sayilar = [*range(1,6)]

print([*filter(cift_sayilari_topla, sayilar)]) # vardir devletin bi bildigi :p ya iste filtrelemeye yariyor kelek. Not: for olayini kendi yapiyor 

sayilar = [*range(1,6)]
print([*map(lambda x: x**2, sayilar)]) #kanka lambda satirda func yazmani sagliyor guzel


