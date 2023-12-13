import cv2
import sys
from random import randint

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

tracker_type = tracker_types[6]

# Qual ferramenta usar
if int(minor_ver) < 3:
    tracker = tracker_type
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()

# Vamos carregar o video
video = cv2.VideoCapture('videos/race.mp4')

if not video.isOpened():
    print('Não foi possivel carregar o video!!!')
    sys.exit()

# Rodar o video
ok, frame = video.read()

if not ok:
    print('Não foi possivel ler o arquivo de video!!!')
    sys.exit()

# Criar a caixa de seleção
bbox = cv2.selectROI(frame, False)

# Inicialização da seleção do objeto
ok = tracker.init(frame, bbox)

# Criar cores RGB aleatorias para caixa de seleção
colors = (randint(0, 255), randint(0, 255), randint(0, 255))

# Executando o video
while True:
    ok, frame = video.read()

    if not ok:
        break

    # Numero de ciclos de clock (Começo do frame)
    timer = cv2.getTickCount()
    # Vai atualizando a posição do frame
    ok, bbox = tracker.update(frame)

    # Calcular o FPS
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]

        # Criar o retangulo
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2, 1)
    else:
        cv2.putText(frame, 'Falha no ratreamento', (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    # Ratreador
    cv2.putText(frame, tracker_type + 'Tracker', (100, 20),
                cv2.FONT_HERSHEY_SIMPLEX, .75, (50,170, 50), 2)

    # FPS
    cv2.putText(frame, 'FPS' + str(int(fps)), (100, 50),
                cv2.FONT_HERSHEY_SIMPLEX, .75, (50, 170, 50), 2)

    # Mostrar o resultado
    cv2.imshow('Tracking', frame)

    # Atribuindo um butão para parar o rastreamento
    if cv2.waitKey(1) & 0XFF == 27:
        break
