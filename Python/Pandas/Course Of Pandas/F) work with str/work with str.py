from numpy import ogrid
import pandas as pd
from pandas.io.parsers import read_csv

review = pd.read_csv('Python\Pandas\Course Of Pandas\ReviewContent.csv')

""" print(review) """

print(review['Country']) # bunun uzerinde biraz calisalim 
print()

# str.upper(), str.lower(), str.len(), str.title()

""" print(review['Country'].str.upper()) # hepsini buyuk yapti 
print(review['Country'].str.lower()) # hepsi kucuk
print(review['Country'].str.title()) # sadece bas harfleri buyuk  """
    # bunlar gecici degisiklikler. kalici olmasini istiyorsak farkli bir degiskene atamali veya inplace=True ozelligini kullanmaliyiz 

    # bu komutlari zincirleme yontemi ile ard arda kullanabiliriz
""" print(review['Country'].str.upper().str.lower()) """

    # str.len()
""" print(len(review['Country'])) # bu bize satir sayisini verir """
""" print(review['Country'].str.len()) # ama str.len() bize satirlardaki strlerin karakter sayisini dondurur """

# str.replace()
""" print('Abicim gunun kodunu soyler misin?'.replace('i','X')) #tek satirda replace ne ise yaradigini gorduk: i yerine X yazdi, simdi de pandasda ne yapilir bakalim """
""" print(review['Room Type'])
print(review['Room Type'].str.replace('room','Room')) # bize kucuk harflerle yazilmiz 'room'u bas harfi buyul 'Room' hale getirdik """


# str.contains(), str.startswith(), str.endswith()

""" print(review['City'])  """# simdi burada icinde 'york' gecenleri dondurmesini isteyecegiz

""" print(review['City'].str.upper().str.contains('YORK')) # boolen deger donduruyor o zaman maskeleme yapalim
print()
mask= review['City'].str.upper().str.contains('YORK')# upper yapmamizin nedeni 'YORK'lari alirken hata olmasin diye :D 
print(review[mask]) # evet ise yaradi sadece City columnunun icinde York olanlari bize dondurdu """

    # str.startswith()
""" mask= review['City'].str.upper().str.startswith('LOS') # simdi 'LOS' ile baslayan sehirlerin verilerini dondurecek
print(review[mask]) """

    # str.endswith() ise usttekinin tam tersi
""" mask= review['City'].str.lower().str.endswith('don') # simdi 'don' ile biten sehirlerin verilerini dondurecek
print(review[mask]) """


# str.strip() bastaki ve sondaki boslugu siler
""" print('                                       sil lan boslugu                                       ')
print('                                       sil lan boslugu                                       '.strip())
print(review['City'].str.strip()) # varsa silmistir :D """

    #lstip(left) ve rstrip(right) sol ve sag bosluklari siler

#split() 

print('benim-admin-can'.split('-')) # tirelerden ayirip liste yapti '' icine ne koyarsan oradan ayirir

print(review['City'].str.split(' ')) # satirlardaki veriyi List olarak dondurdu
print(review['City'].str.split(' ', expand=True))  #bu bize DataFrame olarak dondurmeye yarar
print(review['City'].str.split(' ').str.get(0)) # sifirinci indextekileri dondurdu