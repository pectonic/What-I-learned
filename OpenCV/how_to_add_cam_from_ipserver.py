import cv2


myUrl = "http://192.168.1.128:8080/video" #uygulamanin bize sagladigi ip 

cam = cv2.VideoCapture(myUrl) #bunu videoCapture ile aliyor ve degisgene atiyoruz

print(cam.get(3))
print(cam.get(4))


cam.set(3,320)
cam.set(4,240)

print(cam.get(3))
print(cam.get(4))

while cam.isOpened(): 
    ret, frame= cam.read() #goruntuyu yakalamak icin okuma islemi

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#kamera filtre 

    if not ret: #okuyamazsa ne yapsin
        print('kamera okunamadi')

    cv2.imshow('isimlenmis babus', frame) #imshow ile aciyoruz

    if cv2.waitKey(1) ==ord('q'): # 'q'ya basinca donguden cikmak icin yoksa kapatamayiz ustam
        break


cv2.destroyAllWindows()