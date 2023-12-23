import cv2
import sys
from random import randint

tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture("videos/walking.avi")

if not video.isOpened():
    print("Não foi possivel abrir o video!")
    sys.exit()

ok, frame = video.read()

if not ok:
    print("Não é possivel ler o arquivo de video!")
    sys.exit()

# detector de objetos para pegar uma pessoa
cascade = cv2.CascadeClassifier('cascade/fullbody.xml')


def detectar():
    while True:
        ok, frame = video.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detection = cascade.detectMultiScale(frame_gray)

        for (x, y, l, a) in detection:
            cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
            cv2.imshow("Deteccao", frame)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if x > 0:
            print('Detecção esfeuada pelo haarcascade!')
            return x, y, l, a


bbox = detectar()
print(bbox)
