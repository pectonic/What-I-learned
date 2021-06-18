import cv2


myUrl = "http://192.168.1.128:8080/video" #uygulamanin bize sagladigi ip 

cam = cv2.VideoCapture(myUrl) #bunu videoCapture ile aliyor ve degisgene atiyoruz

cv2.namedWindow('isimlenmis babus', cv2.WINDOW_NORMAL) #bu windowun cozunurlugunu elle degistirebilmek icin


while cam.isOpened(): 
    ret, frame= cam.read() #goruntuyu yakalamak icin okuma islemi

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#kamera filtre 

    if not ret: #okuyamazsa ne yapsin
        print('kamera okunamadi')

    cv2.imshow('isimlenmis babus', frame) #imshow ile aciyoruz

    if cv2.waitKey(1) ==ord('q'): # 'q'ya basinca donguden cikmak icin yoksa kapatamayiz ustam
        break

print(cam.get(4)) #yuksekligi veriyor, sayi degerlerinin ne anlama geldigini buradan bakabiliriz https://www.programmersought.com/article/71733898510/
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) #veya bu sekilde de yazabilir ve yuksekligi alabilir
cv2.destroyAllWindows()