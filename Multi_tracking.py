import cv2
import sys
from random import randint


tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']


def createTrackerByName(trackerType):
    if trackerType == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif trackerType == tracker_types[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == tracker_types[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == tracker_types[4]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == tracker_types[6]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None

        print('Nome incorreto')
        print('Os rastreadores disponiveis são:')

        for t in tracker_types:
            print(t)

    return tracker


cap = cv2.VideoCapture('videos/race.mp4')

ok, frame = cap.read()

if not ok:
    print('Não foi possivel carregar o video!!!')
    sys.exit(1)

bboxes = []
colors = []

while True:
    bbox = cv2.selectROI('MultiTracker', frame)
    bboxes.append(bbox)
    colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    print('Precione Q para sair da caixa de seleção e começar a rastrear!')
    print('Precione qualquer outra tecla para selecionar o proximo objeto!')

    # esperar a tecla que o usuario digitar
    k = cv2.waitKey(0) & 0XFF

    # verificar se digitou o Q
    if (k == 113):
        break

print(f'Caixas delimitadoras selecionadas: {bboxes}')
print(f'Cores: {colors}')

trackerType = 'CSRT'
multiTracker = cv2.MultiTracker_create()

# inicializar cada box x
for bbox in bboxes:
    multiTracker.add(createTrackerByName(trackerType), frame, bbox)

# percorre o video com as box criadas
while cap.isOpened():
    ok, frame = cap.read()

    if not ok:
        break

    ok, boxes = multiTracker.update(frame)

    for i, newbox in enumerate(boxes):
        (x, y, w, h) = [int(v) for v in newbox]

        cv2.rectangle(frame, (x, y), (x + w, y + h), colors[i], 2, 1)

        cv2.imshow('MultiTracker', frame)

        if cv2.waitKey(1) & 0XFF == 27:
            break
