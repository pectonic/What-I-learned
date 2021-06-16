import cv2

print(cv2.__version__)

resim = cv2.imread("jaho.png")# dosyayi okur 

cv2.imshow("epik jaho image", resim) # dosyayi gosterir

cv2.waitKey(0)# bekler, parametre ise kac saniye olacagi ile alakali
# cv2.destroyWindow("epik jaho image") bu spesifik bir pencereyi kapatmaya yarariyor
cv2.destroyAllWindows() #bu alayini kapatir