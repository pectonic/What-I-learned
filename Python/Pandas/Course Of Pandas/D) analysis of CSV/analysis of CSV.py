import pandas as pd
from pandas.core.algorithms import value_counts
from pandas.core.indexes import period

#CSV dosyamizi okutalim
review = pd.read_csv('Python\Pandas\Course Of Pandas\ReviewContent.csv')
""" print(review) """

""" print(review.info()) #normalde 'Review Content' icinde 1 veri eksikti onu ctrl + f = ',,'  aramasi yaparak kolayca buldum """

# head and tail methodlarini kullanalim
""" print(review.head())
print()
print(review.tail()) 

#evet ilk 5 ve son 5i aldik  """


#x.columns attrubatei ile columnlari liste biciminde alabiliriz
""" print(review.columns) #bunu degiskene atayarak kullanabiliriz """

#memory_usage()
""" print(review.memory_usage()) #yani boyle bir sey iste :D"""

#simdi price columnunu toplamaya calicagim
"""     #amk bir saattir neden 'Price' columnu cekemiyorum diyordum, olm 'Room Price'mis ya ...
x = review.get('Room Price').sum() #bu kadar basit
print(x) """

    #simdi her allahin verisini toplayalim
""" print(review.sum()) # sayilari normal topluyor ama text degerleri birbirinin sonuna ekleyerek topluyor """

    #simdi sadece bir column degerlerine deger ekleyelim
""" print(review['Room Availability'])
print(review['Room Availability'].add(10)) # veya (review['Room Availability'] + 10) kodu da ayni islemi yapacaktir yani tum rowlara +10 ekleyecektir  """
    #ve unutmayalim ki sum/sub/mul/div ve +, -, *, / islemleri burada da gecerlidir


#value_counts ile hangi sehirler kac kere girilmis onlari saydiracagiz
""" print(review['City'])
print(review['City'].value_counts()) #135 new york mu, umarim ben de giderim :((( """

    #bunu diger seyler icin de denemek istiyorum merak ettim
""" print(review['Room Type'].value_counts()) """

    #simdi de en pahali ve ucuz odayi bulalim
""" print(review['Room Price'].sort_values().head(1)) #en ucuz
print(review['Room Price'].sort_values(ascending=False).head(1)) #1500 dolares :D  """

    #sehirleri siralayalim
""" print(review['City'].sort_values())#alfabetik siraylar bize dondurdu ama istersen ters kullan bi ascending=False """

    #simde de tum veriyi Room Price'a gore siralayacagiz
print(review.sort_values('Room Price')) #tek attim amk afsafulanneadamimyabendenkomigiyokjasbfa   

