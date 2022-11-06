import cv2 as cv
import numpy as np
import pyautogui as pg

multiplier = 1.1
capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access
width, height = pg.size()
write = False


capture.set(3, height)  # height)
capture.set(4, width)  # width
capture.set(10, 100)  # brightness

myColors = [[0, 80, 231, 179, 208, 255]]
# [ 98, 67, 182, 125, 255, 255]
myColorValues = [[51, 53, 255]]

myPoints = []  ## [x, y, colorId]


def findColor(img, myColors, myColorValuess):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(myColors[0][0:3])
        upper = np.array(myColors[0][3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, myColorValues[0], cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    # cv.imshow('image', mask)

    return newPoints


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return (x + w // 2), y


def drawOnCanvus(myPoints, myColorValues):
    for point_i in range(len(myPoints)):
        point = myPoints[point_i]
        cv.circle(imgFlip, (point[0], point[1]), 1, myColorValues[0], 10, lineType=-1)
        if len(myPoints)>1:
            prevPoint = myPoints[point_i - 1]
            cv.line(imgFlip, (point[0], point[1]), (prevPoint[0],prevPoint[1]),  myColorValues[point[2]], 10)



while True:
    isTrue, img = capture.read()  # Captures the video frame by frame & isTrue boolean indicating whether it's successful or not
    imgResult = img.copy()
    imgFlip = cv.flip(imgResult, 1)

    if write:
        newPoints = findColor(imgFlip, myColors, myColorValues)

        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)

                # pg.moveTo(newPoints[0][0]*multiplier, newPoints[0][1]*multiplier)
                # print(pg.position())

    if len(myPoints) != 0:
        drawOnCanvus(myPoints, myColorValues)


    cv.imshow('Result', imgFlip)  # Displaying video as a new window (windoow name, img)
    key = cv.waitKey(1) & 0xFF # break the loop if key 'c' is pressed

    if key == ord('q'):
        print(myPoints)
        break
    elif key == ord('w'):
        if write:
            write = False
        else:
            write = True
    elif key == ord('c'):
        myPoints.clear()
        print(myPoints)

capture.release()
cv.destroyWindow()  # Destroy all window