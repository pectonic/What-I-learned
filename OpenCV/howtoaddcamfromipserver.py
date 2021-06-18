import cv2


myUrl = "http://192.168.1.128:8080/video" #uygulamanin bize sagladigi ip 

cam = cv2.VideoCapture(myUrl) #bunu videoCapture ile aliyor ve degisgene atiyoruz

cv2.namedWindow('isimlenmis babus', cv2.WINDOW_NORMAL) #bu windowun cozunurlugunu elle degistirebilmek icin


while cam.isOpened(): 
    ret, frame= cam.read() #goruntuyu yakalamak icin okuma islemi

    if not ret: #okuyamazsa ne yapsin
        print('kamera okunamadi')

    cv2.imshow('isimlenmis babus', frame) #imshow ile aciyoruz

    if cv2.waitKey(1) ==ord('q'): # 'q'ya basinca donguden cikmak icin yoksa kapatamayiz ustam
        break

cv2.destroyAllWindows()