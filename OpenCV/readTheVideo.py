import cv2


videoFile = cv2.VideoCapture('E:\What-I-learned-or-I-am-learning-what\What-I-learned\OpenCV\soyle_nasil_sevdigimi.mp4')


while videoFile.isOpened():
    ret, frame = videoFile.read()

    if not ret:
        print('bozuk')

    cv2.imshow('video',frame)

    if cv2.waitKey(1) == ord('q'):
        print('bitti, kapatiyoruz')
        break

videoFile.release()
cv2.destroyAllWindows()