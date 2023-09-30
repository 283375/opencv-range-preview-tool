import cv2
import numpy as np

arr = []

for _ in range(256):
    arr.append([])

for i, s in enumerate(range(256)):
    for h in range(180):
        arr[i].append([h, s, 255])

arr = np.array(arr, np.uint8)

img = cv2.cvtColor(arr, cv2.COLOR_HSV2BGR)
cv2.imwrite("hsv.png", img)
