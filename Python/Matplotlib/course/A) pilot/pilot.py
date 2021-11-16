import matplotlib
import matplotlib.pyplot as plt 
import numpy as np


'''basitinden bir tablo yapisi'''
""" first = np.arange(10) # numpy kullanarak tek boyutlu bir ndarray olusturduk

plt.plot(first) # olusturdugumuz ndarrayi bir tablo uzerine yerlestirdik
plt.title('deneme') # tablonun basligi
plt.ylabel('y label') # tablonun y labeli
plt.xlabel('x label') # tablonun x labeli
plt.show() # tabloyu ayri bir pencerede gosterdik
 """


'''x degerine karsilik y degeri gelen bir tablo yapisi'''
""" x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y, 'ro') # x'e karsilik y geliyor. Tirnak icinde r:red o:dot ifade eder
plt.show()
 """


'''bir ndarrayi farkli bicimlerde gostermek '''
""" deneme_ndarray = np.arange(0.,5.,0.2) # 0dan baslayarak 0.2 artis ile 5e kadar devam bir ndarray
plt.plot(deneme_ndarray,deneme_ndarray,'r--',deneme_ndarray,deneme_ndarray**2,'bs',deneme_ndarray,deneme_ndarray**3,'g^') # kendisi r:red --:tirelerden olustur, karesi b:blue s:square, kupu g:green ^:triangel
plt.show()
 """

''' plt.savefig() ile save etmek'''
""" deneme_ndarray = np.arange(0.,5.,0.2)
plt.plot(deneme_ndarray,deneme_ndarray,'r--',deneme_ndarray,deneme_ndarray**2,'bs',deneme_ndarray,deneme_ndarray**3,'g^')
plt.savefig('Python\Matplotlib\course\A) pilot\deneme.pdf', dpi=300, bbox_inches = 'tight') # dpi: dot per inch 
 """
