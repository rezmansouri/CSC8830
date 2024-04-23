import cv2
import numpy as np
import matplotlib.pyplot as plt

object_1 = plt.imread('input/book.jpg')
object_2 = plt.imread('input/cream.jpg')
object_3 = plt.imread('input/bowl.jpg')

label_1 = 'Book'
label_2 = 'Cream'
label_3 = 'Bowl'

cv2.namedWindow("Reza Mansouri - A4Q1", cv2.WINDOW_FREERATIO)
vc = cv2.VideoCapture(0)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 200) 

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    ssds = []
    coords = []
    for i in range(0, frame.shape[0] - object_1.shape[0], 30):
        for j in range(0, frame.shape[1] - object_1.shape[1], 30):
            candidate = frame[i:i+object_1.shape[0], j:j+object_1.shape[1]]
            ssd = np.sum(np.power(candidate-object_1, 2))
            ssds.append(ssd)
            coords.append((j, i))
    min_ix = np.argmin(ssds)
    ssd = ssds[min_ix]
    if ssd < np.mean(ssds[~min_ix]) * .95:
        left_top = coords[min_ix]
        right_bottom = (left_top[0] + object_1.shape[1], left_top[1] + object_1.shape[0])
        frame = cv2.rectangle(frame, left_top, right_bottom, color=(0, 255, 255), thickness=5)
        frame = cv2.putText(frame, label_1, (left_top[0], left_top[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    else:
        ssds = []
        coords = []
        for i in range(0, frame.shape[0] - object_2.shape[0], 30):
            for j in range(0, frame.shape[1] - object_2.shape[1], 30):
                candidate = frame[i:i+object_2.shape[0], j:j+object_2.shape[1]]
                ssd = np.sum(np.power(candidate-object_2, 2))
                ssds.append(ssd)
                coords.append((j, i))
        min_ix = np.argmin(ssds)
        ssd = ssds[min_ix]
        if ssd < np.mean(ssds[~min_ix]) * .94:
            left_top = coords[min_ix]
            right_bottom = (left_top[0] + object_2.shape[1], left_top[1] + object_2.shape[0])
            frame = cv2.rectangle(frame, left_top, right_bottom, color=(255, 100, 0), thickness=5)
            frame = cv2.putText(frame, label_2, (left_top[0], left_top[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        else:
            ssds = []
            coords = []
            for i in range(0, frame.shape[0] - object_3.shape[0], 30):
                for j in range(0, frame.shape[1] - object_3.shape[1], 30):
                    candidate = frame[i:i+object_3.shape[0], j:j+object_3.shape[1]]
                    ssd = np.sum(np.power(candidate-object_3, 2))
                    ssds.append(ssd)
                    coords.append((j, i))
            min_ix = np.argmin(ssds)
            ssd = ssds[min_ix]
            if ssd < np.mean(ssds[~min_ix]) * .98:
                left_top = coords[min_ix]
                right_bottom = (left_top[0] + object_3.shape[1], left_top[1] + object_3.shape[0])
                frame = cv2.rectangle(frame, left_top, right_bottom, color=(0, 0, 255), thickness=5)
                frame = cv2.putText(frame, label_3, (left_top[0], left_top[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Reza Mansouri - A4Q1", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(100)
    if key == 27:
        break

vc.release()
cv2.destroyWindow("Reza Mansouri - A4Q1")
