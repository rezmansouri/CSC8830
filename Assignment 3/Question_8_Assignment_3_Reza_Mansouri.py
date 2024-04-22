import cv2
import numpy as np
import matplotlib.pyplot as plt

object = plt.imread('input/question_8.jpg')

cv2.namedWindow("Reza Mansouri - A3Q8", cv2.WINDOW_FREERATIO)
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    ssds = []
    coords = []
    for i in range(0, frame.shape[0] - object.shape[0], 30):
        for j in range(0, frame.shape[1] - object.shape[1], 30):
            candidate = frame[i:i+object.shape[0], j:j+object.shape[1]]
            ssd = np.sum(np.power(candidate-object, 2))
            ssds.append(ssd)
            coords.append((j, i))
    left_top = coords[np.argmin(ssds)]
    right_bottom = (left_top[0] + object.shape[1], left_top[1] + object.shape[0])
    frame = cv2.rectangle(frame, left_top, right_bottom, color=(0, 255, 255), thickness=5)
    cv2.imshow("Reza Mansouri - A3Q8", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(60)
    if key == 27:
        break

vc.release()
cv2.destroyWindow("Reza Mansouri - A3Q8")