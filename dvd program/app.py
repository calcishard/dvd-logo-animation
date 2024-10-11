import cv2
import numpy as np
import random

def generateRandomColor():
    randomColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return randomColor
width = 600
height = 400
blackImage = np.zeros((height, width, 3), dtype=np.uint8)

#text variables
text = "safiyya"
textFont = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
thickness = 2
color = generateRandomColor()

x = 0
y = 20
dx = 8
dy = 6

while True:

    blackImage[:] = 0

    cv2.putText(blackImage, text, (x, y), textFont, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('test', blackImage)

    x += dx
    y += dy

    if x + len(text) * 15 > width or x < 0:
        dx = -dx
        color = generateRandomColor()
    if y + 10 > height or y < 20:
        dy = -dy
        color = generateRandomColor()

    if cv2.waitKey(30) == ord("q"):
        break
cv2.destroyAllWindows()