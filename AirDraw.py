import cv2 as cv
import numpy as np
import pyautogui as pg


class airdraw():
    def __init__(self):

        self.THICKNESS = 10
        self.capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access
        self.WRITE = False
        self.SHOW = True
        self.capture.set(10, 1000)  # brightness
        self.capture.set(3, 1000)  # brightness

        self.capture.set(4, 10500)  # brightness


        self.myColors = [[0, 80, 231, 179, 208, 255]]
        # [ 98, 67, 182, 125, 255, 255]
        self.myColorValues = [[51, 53, 255]]

        self.myPoints = []  ## [x, y, colorId]


        # create window
        self.width, height = pg.size()
        self.window = cv.namedWindow("Air",cv.WINDOW_FULLSCREEN)


    def findColor(self, img, myColors):
        imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        count = 0
        newPoints = []

        for color in myColors:
            lower = np.array(myColors[0][0:3])
            upper = np.array(myColors[0][3:6])
            mask = cv.inRange(imgHSV, lower, upper)
            x, y = self.Contours(mask)
            cv.circle(self.imgResult, (x, y), 10, self.myColorValues[0], cv.FILLED)
            if x != 0 and y != 0:
                newPoints.append([x, y, count])
            count += 1
        # cv.imshow('image', mask)

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

    def drawOnCanvus(self, myPoints, myColorValues):
        for point in myPoints:
            if point != 'skip':
                cv.circle(self.imgFlip, (point[0], point[1]), 1, myColorValues[0], 10, lineType=-1)

        if len(myPoints)>1:
            if myPoints[-1] != 'skip' and myPoints[-2] != 'skip':
                last = myPoints[-1]
                lastS = myPoints[-2]
                cv.line(self.imgFlip, (last[0], last[1]), (lastS[0], lastS[1]),myColorValues[0], self.THICKNESS)
            elif len(myPoints) > 2 and myPoints[-2] != 'skip':
                last = myPoints[-2]
                lastS = myPoints[-3]
                cv.line(self.imgFlip, (last[0], last[1]), (lastS[0], lastS[1]), myColorValues[0], self.THICKNESS)

    def draw_lines(self, myPoints, myColorValues):

        for index in range(len(myPoints)):
            if index > 0 and (myPoints[index] != 'skip' and myPoints[index-1] != 'skip'):
                last = myPoints[index]
                lastS = myPoints[index-1]
                cv.line(self.imgFlip, (last[0], last[1]), (lastS[0], lastS[1]), myColorValues[0], 10)

    def run(self):
        while True:
            isTrue, img = self.capture.read()  # Captures the video frame by frame & isTrue boolean indicating whether it's successful or not
            self.imgResult = img.copy()
            self.imgFlip = cv.flip(self.imgResult, 1)

            if self.WRITE:
                newPoints = self.findColor(self.imgFlip, self.myColors)

                if len(newPoints) != 0:
                    for newP in newPoints:
                        self.myPoints.append(newP)

                        # pg.moveTo(newPoints[0][0]*multiplier, newPoints[0][1]*multiplier)
                        # print(pg.position())

            if len(self.myPoints) != 0:
                self.drawOnCanvus(self.myPoints, self.myColorValues)
                self.draw_lines(self.myPoints, self.myColorValues)

            cv.imshow('Air', self.imgFlip)  # Displaying video as a new window (windoow name, img)
            # minimize window when in pressed 'k'
            if not self.SHOW:
                cv.resizeWindow("Air", 60, 30)
            key = cv.waitKey(1) & 0xFF # break the loop if key 'c' is pressed
            print(key)

            if key == ord('q'):
                break
            elif key == ord('h'):
                print('h is pressed')
                if self.WRITE:
                    self.WRITE = False
                    self.myPoints.append('skip')
                else:
                    self.WRITE = True
            elif key == ord('c'):
                self.myPoints.clear()

            elif key == ord('k'):
                if self.SHOW:
                    self.SHOW = False
                else:
                    self.SHOW = True
        # elif key == ord('p'):
        #     save_img('temp.jpg', imgFlip)

        self.capture.release()
        cv.destroyAllWindows()
      # Destroy all window


if __name__ == '__main__':
    obj = airdraw()
    obj.run()

