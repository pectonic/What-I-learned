import cv2

cam = cv2.VideoCapture(2)

while True:
    ret, frame = cam.read()

    if not ret:
        print("kameradan goruntu okunamiyor")

    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) == ord('q'):
        print('goruntu sonlandi')
        break

cam.release()
cv2.destroyAllWindows()