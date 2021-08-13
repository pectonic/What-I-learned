import pandas as pd

#bu derste read/head/tail/sort_values/sort_index/get kullanildi

""" review_content = pd.read_csv('Python\Pandas\Course Of Pandas\ReviewContent.csv', encoding='utf-8', engine='python')  """# evet dosyamizi okuttuk, hatalar alirsak diye parametrelere atama yapabiliyoruz

""" print(review_content) 
print(type(review_content)) """ #evet bize DataFrame olarak yansiyor ki biz bunu ogrenmedik o yuzden Series olarak kullanacagiz bunu da .csv dosyasini tanimlarken parametrelerde belirtecegiz

review_content = pd.read_csv('Python\Pandas\Course Of Pandas\ReviewContent.csv', usecols=['Review ID'], squeeze=True, encoding='utf-8', engine='python') #usecols stun secmemize yariyor, squeeze ne bilmiyorum arastirmak lazim internet olsa ahh AHHH ANANI SIKEYIM TURKTELEKOM orospu cocuklari sizi... neyse squeeze false olunca Series olarak degil de DataFrame olarak aliyor yani Series olarak almak istersek lazim

'''print(type(review_content))''' # evet series oldu guzel
""" print(review_content)""" # ilk 5 veriyi ve son 5 veriyi veriyor biz sadece bastan istedigimiz kadar veri istersek head() methodunu kullanabiliriz.(eger icini bos birakirsan defoult olarak 5 veri doner)

""" print(review_content.head(6)) """ # ve bu sefer ayirmiyor
""" print(review_content.tail()) """ #sondan baslayarak 5 veri dondu ve bunlar unutmayalim ki yeni bir series olarak geliyor, ana veri tabanina etki etmek istersek inplace=True ozelligini kullanmamiz gerekir

#peki o zaman siralamalarla biraz oynayalim

""" print(review_content.head(10))
print()
print(review_content.sort_values().head(10)) #evet degerleri kucukten buguye dogru siraladi ama bu sekilde gecici olur, tabii artik biliyoruz kalici olmasini istersek inplace=True ozellegini kullanacagiz
print()
print(review_content.head(10)) #bir degisiklik yok yane """ 

#madem inplace ozelleginden o kadar bahsettik hadi kullanalim

""" print(review_content.head(10))
print()
review_content.sort_values(inplace=True, ascending=False) # buyukten kucuge siralamak icin ise ascending=False parametresini kullaniyoruz
print()
print(review_content.head(10)) #evet etkisini gosterdi  """ 

#degere gore siraladik, simdi de indexe gore siralayalim

""" print(review_content.head(10))
print()
review_content.sort_index(inplace=True, ascending=False) 
print()
print(review_content.head(10)) 
 """

#degere gore siraladiktan sonra indexe gore tekrar siralama yapalim

""" print(review_content.head(10))
print()
review_content.sort_values(inplace=True)
print(review_content.head(10))
print()
review_content.sort_index(inplace=True)
print(review_content.head(10)) """

#Seris yapisinde indexlere gore serilere ulasma ornekleri yapalim

""" print(review_content.head(10))
print()
print(review_content[4])
print(review_content.get(4)) # normal cagirma ile bunun arasinda fark olmadigini mi dusunuyorsun? o zaman yaniliyorsun 🤠🤠🤠🤠
print()

print(review_content[1004]) #bu bize hata verecektir
print(review_content.get(1004, default='LAN ELEMAN YOK')) #ama bu bize hata degil 'None' veya ne belirlediysek onu donecektir 😎✌ """

# tekli degerlerin tiplerini ogrenelim
""" print(type(review_content[4]))
print(type(review_content.get(4))) #tipleri gordugunuz gibi numpy.int64 yaneeee bu da pandas numpy ustune kuruldugunun kanitidir.  """

#coklu secimler

print(review_content.get([3,1]))
print(type(review_content.get([3,1]))) #evet bu series tipinde ki normal
