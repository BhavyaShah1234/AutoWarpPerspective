import cv2 as cv
import numpy as np


def click_event(event, x_cord, y_cord, flags, param):
    global x, y
    if event == cv.EVENT_LBUTTONDOWN:
        x, y = x_cord, y_cord


img_path = r'CV All\scan.jpg'
x, y = -1, -1
pts1 = []
while len(pts1) < 4:
    img = cv.imread(img_path)
    cv.imshow('Clickable Image', img)
    cv.setMouseCallback('Clickable Image', click_event)
    if x > 0 and y > 0:
        print(x, y)
        pts1.append([x, y])
        x, y = -1, -1
    cv.waitKey(1)
cv.destroyAllWindows()
print(pts1)
img = cv.imread(img_path)
width = int(pow(pow(pts1[1][0] - pts1[0][0], 2) + pow(pts1[1][1] - pts1[0][1], 2), 0.5))
height = int(pow(pow(pts1[2][0] - pts1[1][0], 2) + pow(pts1[2][1] - pts1[1][1], 2), 0.5))
print(width, height)
pts1 = np.array(pts1, np.float32)
pts2 = np.array([[0, 0], [width, 0], [0, height], [width, height]], np.float32)
matrix = cv.getPerspectiveTransform(pts1, pts2)
output_img = cv.warpPerspective(img, matrix, (width, height))
cv.imshow('Warped Image', output_img)
cv.waitKey(0)
cv.destroyAllWindows()
