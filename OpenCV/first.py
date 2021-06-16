import cv2

print(cv2.__version__)

resim = cv2.imread('E:\What-I-learned-or-I-am-learning-what\What-I-learned\OpenCV\jaho.png',0)# dosyayi okur 

cv2.imshow("Epic Jaho Moment", resim) # dosyayi gosterir

k = cv2.waitKey(0)# bekler, parametre ise kac saniye olacagi ile alakali

# cv2.destroyWindow("epik jaho image") bu spesifik bir pencereyi kapatmaya yarariyor

''' 
burada if ile hexadecimal charactersden esc(27) tusuna bastiginda cikis yapip mesaj gondermesini ve ord komutusu ile s tusuna basarsak mesaj+olan resmi kaydetme islemi yaptik
'''
if k == 27:
    print('esc bastin')
elif k == ord('s'):
    print('s tusuna bastin')
    cv2.imwrite('jaho ama gri.png',resim)


cv2.destroyAllWindows() #bu alayini kapatir