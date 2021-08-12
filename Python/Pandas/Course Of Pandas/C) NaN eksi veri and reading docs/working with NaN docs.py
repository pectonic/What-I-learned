import pandas as pd

students = {'Can':pd.Series(data=[20,  'Agriculture','aydin', 172], index=['age', 'department','surname', 'height']),
            'Miku':pd.Series(data=[21, 'F','japon', 55], index=['age','gender','surname', 'weight']),
            'Umit':pd.Series(data=[19,  'Streamer','demirkaya', 176], index=['age', 'department','surname', 'height'])
            }

df_students = pd.DataFrame(students)
print(df_students)
print()

#burada neyin NaN oldugunu gozumuzle secebiliriz ama buyuk bir veride bunu yapmak pek akillica olmaz o yuzden bununla ilgilenelim

#isnull()
""" x = df_students.isnull() #veri olmayan yerde True dondurerek bize bir DataFrame verdi ve bu boolean degerler bize 0 1ler olarak dondugunden kac tane 0 kac tane 1 oldugunu ogrenbilirz
print(x) """

    #simdi indexlerde kactane NaN deger var ona bakalim
""" y = df_students.isnull().sum()
print(y)
print(type(y)) """

    #indexlerde toplam kac tane NaN var
""" z = df_students.isnull().sum().sum()
print(z)
print(type(z))
 """

#notnull() ise isnull() metodunun tam tersi 
""" x = df_students.notnull() #veri olmayan yerde False dondurerek bize bir DataFrame verdi ve bu boolean degerler bize 0 1ler olarak dondugunden kac tane 0 kac tane 1 oldugunu ogrenbilirz
print(x)
print()
 """
    #simdi indexlerde kac tane dolu deger var ona bakalim
""" y = df_students.notnull().sum()
print(y)
print(type(y))
print() """

    #indexlerde toplam kac tane dolu var
""" z = df_students.notnull().sum().sum()
print(z)
print(type(z))
print()
 """

#count() dolu bos farketmez tum verileri 1 sayar
""" x = df_students.count() # indexlerde kac tane veri var onu sayar
print(x)
print() """

    #simdi  kac tane deger var ona bakalim
""" y = df_students.count().sum()
print(y)
print(type(y))
print() """

#dropna() ile icerisinde herhangi bir NaN ifadesi bulunan indexi yok edebiliriz
""" x = df_students.dropna() #bir degiskene atayabiliriz veya inplace= parametresini kullanabiliriz
print(x)
print(type(x)) """

    #how='all' parametresi tum row NaN ile doluysa o row'u siler
""" df_students['Miku']['weight'] = None
print(df_students)
print()

x = df_students.dropna( how='all') 
print(x)
print(type(x)) """

    #thresh=x parametresi x'e kac verirsen row'da o kadar NaN varsa o row'u siler. Not: x'e kadar degil x tane varsa o satiri siler
""" x = df_students.dropna( thresh=2) 
print(x)
print(type(x)) """

    #axis parametreleri kullanimi
""" x = df_students.dropna(axis=0) #NaN deger olan tum rowlari siler
print(x)
print(type(x))
print()

y = df_students.dropna(axis=1) #NaN deger olan tum columnlari siler ve bizde column kalmadi :D
print(y)
print(type(y)) """


#fillna()
""" x = df_students.fillna(method='ffill', axis=0) #ust rowdan alip doldurdu
print(x) """

x = df_students.fillna(method='ffill', axis=1) #sol columndan alip dolduruyor ama bak ilk column NaN kaldi cunku alabilecegi deger yok ama eger 'ffill'i 'backfill' yaparsak ilk column deger alir ama bu sefer sondaki almaz 
print(x)
print()

y = df_students.fillna(method='ffill', axis=1).fillna(method='backfill', axis=1)# bu da sagdan soldan aldigindan bos kalan deger kalmaz, hepsine deger 
print(y)