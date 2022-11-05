import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access

capture.set(3, 640)  # height
capture.set(4, 480)  # width
capture.set(10, 130)  # brightness

myColors = [[0, 120, 177, 177, 255, 255]]

myColorValues = [[51, 153, 255]]

myPoints = []  ## [x, y, colorId]

def findColor(img, myColors):

    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    cv.circle(imgResult, (x,y), 10, myColorValues[0], cv.FILLED)
    # cv.imshow('image', mask)

def getContours(img):

    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            # cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return  x+w//2, y

def drawOnCanvus(myPoints, myColorValues):
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1], 10, myColorValues[point[2]], cv.FILLED )





while True:
    isTrue, img = capture.read()  # Captures the video frame by frame & isTrue bolean indicating whether it's successful or not
    imgResult = img.copy()
    newPoints
    findColor(img, myColors)
    cv.imshow('Video Learning OpenCV', imgResult)  # Displaying video as a new window (windoow name, img)


    if cv.waitKey(20) & 0xFF == ord('Q'):  # break the loop if key 'c' is pressed
        break

capture.release()
cv.destroyWindow()  # Destroy all window

