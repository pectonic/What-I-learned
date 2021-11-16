import numpy as np
import matplotlib.pyplot as plt

'''matplotlibte grafikler figure object olarak dizayn edilir'''

""" deneme_figure = plt.figure() # figure olusturduk """

data = np.random.randn(50).cumsum() # cumsum() kumelatif toplami verir

""" x1 = deneme_figure.add_subplot(2,2,1) # add_subplot alt tablo eklemeye yarar. 4 tane tablo olusturdu ve birincisini x1'e atadi
x1.plot(data, 'k--') # seklini semalini verdik

x2 = deneme_figure.add_subplot(2,2,2) # ikinciyi x2'ye atadik
x2.plot(data, 'ro')

x3 = deneme_figure.add_subplot(2,2,3) # ucuncuyu x3'e atadik
x3.plot(data, 'b^')

x4 = deneme_figure.add_subplot(2,2,4) # dorduncuyu x4'e atadik
x4.plot(data, 'ys')

plt.show() """



''' grafiklerde gorsellik ozellikleri'''

""" x1 = [1,2,3,4,5,6]
x2 = [19,20,21,22,23,24]
deneme_figure2 = plt.figure()
deneme_tablo = deneme_figure2.add_subplot(1,1,1)
# plt.plot(x1,x2, linestyle='--', color='b') 
plt.plot(data, 'r2:') # bircok attrubute var baba internetnetten baki ver :P, bastan sonra seyleri belirler: rengini, kesisim noktalarini, ana cizgi
plt.show() """
 


'''eksenleri etiketlendirme '''

""" deneme_fig3 = plt.figure()
deneme_tablo3 = deneme_fig3.add_subplot(1,1,1)
deneme_tablo3.plot(data, 'g--') 
deneme_tablo3.set_xticks([0,15,30,45]) # x labelin degerleri
deneme_tablo3.set_xticklabels(['bir','iki','uc','YARAAAAAA😎'], rotation=45, fontsize='small')  """

""" deneme_tablo3.set_title('aynen kanka sifir sikinti 🙂')
deneme_tablo3.set_xlabel('yatti balik yan gider')
deneme_tablo3.set_ylabel('uctu balik fena gider')  """
# veya bunlar yerine baba set ozelligini kullanalim
""" ozellikler = {'title':'wow grafik',
              'xlabel':'deneme x icin baba',
              'ylabel':'deneme y icin gulum'}
deneme_tablo3.set(**ozellikler)

plt.show() """







