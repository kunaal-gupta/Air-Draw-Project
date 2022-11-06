from cv2 import cv2 as cv
import numpy as np
# import win32gui,win32con
import pyautogui as pg

class Cursor():
    def __init__(self):
        self.vid = cv.VideoCapture(0)
        self.window = cv.namedWindow("AIR", cv.WINDOW_NORMAL)
        cv.resizeWindow("AIR", (500,500))
        self.motion = True
        self.myColorValues = [[51, 53, 255]]
        self.myColors = [[0, 80, 231, 179, 208, 255]]
        self.thickness = 10
        self.myPoints = []

    def findColor(self, img, myColors):
        imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        count = 0
        newPoints = []

        for color in self.myColors:
            lower = np.array(myColors[0][0:3])
            upper = np.array(myColors[0][3:6])
            mask = cv.inRange(imgHSV, lower, upper)
            x, y = self.Contours(mask)
            cv.circle(self.imgResult, (x, y), self.thickness, self.myColorValues[0], cv.FILLED)
            if x != 0 and y != 0:
                newPoints.append([x, y, count])
            count += 1

        return newPoints

    def Contours(self, img):
        contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        x, y, w, h = 0, 0, 0, 0
        for cnt in contours:
            area = cv.contourArea(cnt)
            if area > 500:
                cv.drawContours(self.imgResult, cnt, -1, (255, 0, 0), 3)
                peri = cv.arcLength(cnt, True)
                approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
                x, y, w, h = cv.boundingRect(approx)
        return (x + w // 2), y

    def click(self):
        if len(self.myPoints) > 10:
            count = 0
            x = self.myPoints[-10][0]
            y = self.myPoints[-10][1]
            width = height = 10
            for i in range(-10, len(self.myPoints)):
                print('x=', x, 'y=', y, 'i[x] = ', self.myPoints[i][0], 'i[y] = ', self.myPoints[i][1])
                if x < self.myPoints[i][0] < x + width and y < self.myPoints[i][1] < y + height:
                    count += 1
            if count > 8:
                pg.click(x=(x + (x + width)) // 2, y=(y + (y + height)) // 2, clicks=2, interval = 0.05)



    def move(self):
        # Minimize = win32gui.GetForegroundWindow()
        # win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

        multiplier = 1
        while True:
            success, img = self.vid.read()
            self.imgResult = img.copy()
            self.imgFlip = cv.flip(self.imgResult, 1)
            if self.motion:
                newPoints = self.findColor(self.imgFlip, self.myColors)

            if len(newPoints) != 0:
                for newP in newPoints:
                    pg.moveTo(newPoints[0][0]*multiplier, newPoints[0][1]*multiplier)
                    self.myPoints.append(newP)

            self.click()
            cv.imshow("AIR", self.imgFlip)
            key = cv.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            elif key == ord('k'):
                if self.motion:
                    self.motion = False
                else:
                    self.motion = True
            elif key == 32:
                pg.click(pg.position())


def main():

    obj = Cursor()
    obj.move()

main()