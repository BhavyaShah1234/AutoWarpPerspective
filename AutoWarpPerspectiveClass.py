import cv2 as cv
import numpy as np


class WarpPerspective:
    def __init__(self, image_path):
        self.image_path = image_path
        self.x, self.y = -1, -1
        self.pts1 = []

    def click_event(self, event, x_cord, y_cord, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.x = x_cord
            self.y = y_cord

    def get_points(self, points, draw=False):
        while len(self.pts1) < points:
            img = cv.imread(self.image_path)
            if len(self.pts1) > 0 and draw:
                for i in range(len(self.pts1)):
                    cv.circle(img, (self.pts1[i][0], self.pts1[i][1]), 5, (0, 200, 0), -1)
            cv.imshow('Clickable Image', img)
            cv.setMouseCallback('Clickable Image', self.click_event)
            if self.x > 0 and self.y > 0:
                self.pts1.append([self.x, self.y])
                self.x, self.y = -1, -1
            cv.waitKey(1)
        cv.destroyAllWindows()
        return self.pts1

    def warp(self):
        img = cv.imread(self.image_path)
        pts1 = np.array(self.get_points(4, False), dtype='float32')
        width = int(pow(pow(self.pts1[1][0] - self.pts1[0][0], 2) + pow(self.pts1[1][1] - self.pts1[0][1], 2), 0.5))
        height = int(pow(pow(self.pts1[2][0] - self.pts1[1][0], 2) + pow(self.pts1[2][1] - self.pts1[1][1], 2), 0.5))
        pts2 = [[0, 0], [width, 0], [0, height], [width, height]]
        pts2 = np.array(pts2, dtype='float32')
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        out = cv.warpPerspective(img, matrix, (width, height))
        cv.imshow('Warped Image', out)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':
    w = WarpPerspective('cards.jpg')
    pts = w.get_points(4, True)
    print(pts)
    w.warp()
