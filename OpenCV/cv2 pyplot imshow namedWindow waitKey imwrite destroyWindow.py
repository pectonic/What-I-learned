import cv2
from matplotlib import pyplot as plt #bazi ozellikler saglayan pencere diyebiliriz

print(cv2.__version__)

resim = cv2.imread('E:\What-I-learned-or-I-am-learning-what\What-I-learned\OpenCV\jaho.png',0)# dosyayi okur 

cv2.imshow("Epic Jaho Moment", resim) # dosyayi gosterir

cv2.namedWindow('isimlenmis babus', cv2.WINDOW_NORMAL) #bu sekilde aslinda bos bir window acabiliyoruz, WINDOW_NORMAL ise window acildiktan sonra boyutunu elle degistirebilmemize yariyor
cv2.imshow('isimlenmis babus', resim)


plt.imshow(resim, cmap='gray')# cmap renk paleti icin cunku matplotlib rgb degil de bgr kullaniyor bu da kirmizi ile mavinin yer degistirmesi demek vs.
plt.show()





k = cv2.waitKey(0)# bekler, parametre ise kac saniye olacagi ile alakali

# cv2.destroyWindow("epik jaho image") bu spesifik bir pencereyi kapatmaya yarariyor

''' 
burada if ile hexadecimal charactersden esc(27) tusuna bastiginda cikis yapip mesaj gondermesini ve ord komutusu ile s tusuna basarsak mesaj+olan resmi kaydetme islemi yaptik
'''
if k == 27:
    print('esc bastin')
elif k == ord('s'):
    print('s tusuna bastin')
    cv2.imwrite('E:\What-I-learned-or-I-am-learning-what\What-I-learned\OpenCV\jaho ama gri.png',resim)


cv2.destroyAllWindows() #bu alayini kapatir