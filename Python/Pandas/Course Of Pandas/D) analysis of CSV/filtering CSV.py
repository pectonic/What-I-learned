from typing import Tuple
import pandas as pd

review = pd.read_csv('Python\Pandas\Course Of Pandas\ReviewContent.csv')
""" print(review)
print() """

#biz sadece bir column bilgisini nasil aliyorduk
""" print(review['City'])  """
    #bunu hatirladiktan sonra simdi sadece 'London' olanlari alabiliriz
""" print(review['City'] == 'London') """ #evet bize True ve False degerleri dondurdu simdi bunu tam anlamiyla isleyelim
""" print(review[review['City'] == 'London']) """ #bize sadece London olan sehirlerin bilgisini verdi ama bunun daha guzel yazim sekli var

""" mask = review['City'] == 'London' 
print(review[mask]) #bu sekilde daha UwU  """

    #farkli ornekler yapalim
""" mask = review['Room Type'] == 'Private room' 
print(review[mask]) """
""" mask = review['Room Type'] != 'Private room' #bu da 'Private room' olmayanlari bulur
print(review[mask]) """

    #100 ile 60 price arasini goster
""" mask = (review['Room Price'] <= 100) & (review['Room Price'] >= 60 )
print(review[mask]) """

    #room price 200den yuksek ya da room availablitily 300den yuksek 
""" mask = (review['Room Price'] >= 200 ) | (review['Room Availability'] >= 300 )
print(review[mask]) """


#isin() metod kullanimi

    #evet isin icinde mi sorusunu sorar ve bize boolen deger dondurur
""" mask = review['City'].isin(['Paris','London','Austin']) 
print(review[mask]) """

# between() arasinda?
""" mask = review['Room Price'].between(80,120) #80 ve 100 kapali aralik
print(review[mask]) """

    #tarihler arasinda da yapabiliriz
""" mask = review['Review Date'].between('2012-01-01','2014-01-01')
print(review[mask]) """

# duplicated() 1den fazla tekrarlayan degerleri boolen deger olarak verir
""" review.sort_values('City', inplace=True)
print(review['City'])
print(review['City'].duplicated()) #gordugumuz gibi bize teklarlayan degerleri true olarak donduruyor """

    #simdi false degerleri yakalayarak sehirlerden Series olusturacagim
""" review.sort_values('City', inplace=True)
print(review['City'])
mask = review['City'].duplicated() == False
cities = pd.Series(review[mask]['City'].to_list())
print(cities.size) #27 tane var """

# drop_duplicates() ise True'lari droplar 
""" print(len(review))
print(len(review.drop_duplicates())) # silmesi icin her satirin ve sutunun ayni almasi gerekir ama istersek sadece bir sutuna bakabiliriz
print(len(review.drop_duplicates(subset=['City']))) #BUUUM 
print(len(review.drop_duplicates(subset=['Room Type']))) #BUUUM  """

# unique ve nunique
""" print(review.unique()) # hahah ulan unique bir tane item yok hata veriyor, benim PoE'de cok vardi... Ozledim lan kahpe """ #hata vermesinin onunla alakasi yok aptal! Bu method tek boyutta calisiyor ona calismasi icin Series ver

""" print(review['City'].unique()) # oooo NDarray olarak dondurdu
print(len(review['City'].unique())) # evet bilgidimiz bir deger olan 27yi dondurdu """

    #nunique ise numbers of unique anlamina geliyor sanirim yani unique itemlerin sayisini veriyor 
""" print(review['City'].nunique())
print(review.nunique()) # UwU ne guzel gozuktu la """