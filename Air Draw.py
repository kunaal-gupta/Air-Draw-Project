import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
# cv.flip()# Either path of video file you wanna play or int 0,1,2 for webcam access

capture.set(3, 500)  # height
capture.set(4, 500)  # width
capture.set(10, 100)  # brightness

myColors = [[0, 80, 231, 179, 208, 255]]

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
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1]), 5, myColorValues[point[2]],10, lineType=-1)


while True:
    isTrue, img = capture.read()  # Captures the video frame by frame & isTrue boolean indicating whether it's successful or not
    imgFlip = cv.flip(img, 1)
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvus(myPoints, myColorValues)

    cv.imshow('Result', imgResult)  # Displaying video as a new window (windoow name, img)
    if cv.waitKey(1) & 0xFF == ord('Q'):  # break the loop if key 'c' is pressed
        break

capture.release()
cv.destroyWindow()  # Destroy all window
