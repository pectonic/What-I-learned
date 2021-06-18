import cv2


myUrl = "http://192.168.1.128:8080"

cam = cv2.VideoCapture(myUrl)

while cam.isOpened():
    ret, frame= cam.read()

    if not ret:
        print('kamera okunamadi')

    cv2.imshow("goruntu",frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cv2.destroyAllWindows()    