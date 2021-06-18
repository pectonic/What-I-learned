import cv2 

cam = cv2.VideoCapture()#ya webcam olsa tak diye sadece 0,1 veya 2... her neyse onu gireceksin ama webcam olmayinca ip ile falan ugrasiyorsun amk 

myUrl = "http://192.168.1.128:8080/video" #uygulamanin bize sagladigi ip 

cam = cv2.VideoCapture(myUrl)

fourrc = cv2.VideoWriter_fourcc(*'XVID') # video encoder icin

out = cv2.VideoWriter('E:\What-I-learned-or-I-am-learning-what\What-I-learned\OpenCV\_firtrecordfromopencv.avi',fourrc,30.0,(640,480)) #ismini, encoder'i, fps ve cozunurluk degerleri


while cam.isOpened(): 
    ret, frame= cam.read()

    if not ret: 
        print('kameradan goruntu alinamadi')

    out.write(frame)

    cv2.imshow('video record from cam', frame) 

    if cv2.waitKey(1) ==ord('q'): 
        break

cam.release()
out.release()
cv2.destroyAllWindows()