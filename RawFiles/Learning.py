# import cv2 as cv
# import numpy as np
#
#
# def image_read():
#     """ Reading images  """
#
#     img = cv.imread('Kunaal.jpg')  # reading pixels of image
#     cv.imshow('Image Learning OpenCV', img)  # Displaying image as a new window (windoow name, img)
#
#     cv.waitKey(0)
#
#
# def video_read():
#     """Reading Video or live video"""
#
#     capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access
#
#     capture.set(3, 630)  # height
#     capture.set(4, 480)  # width
#     capture.set(10, 200)  # brightness
#
#     while True:
#         isTrue, frame = capture.read()  # Captures the video frame by frame & isTrue bolean indicating whether it's successful or not
#         cv.imshow('Video Learning OpenCV', frame)  # Displaying video as a new window (windoow name, img)
#
#         if cv.waitKey(20) & 0xFF == ord('c'):  # break the loop if key 'c' is pressed
#             break
#
#     capture.release()
#     cv.destroyWindow()  # Destroy all window
#
#
#
# # --------------------------------------------------------------------------------------------------------------------
# def resize(frame, scale):
#     """Resizing an image, Video or live video """
#
#     width = int(frame.shape[1] * scale)  # Accessing width from the frame & increasing it by scale times
#     height = int(frame.shape[0] * scale)  # Accessing height from the frame & increasing it by scale times
#
#     dimensions = (width, height)
#
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#
#
# # img = cv.imread('Kunaal.jpg')  # reading pixels of image
# #
# # rimg = resize(img, scale=0.25)
# # cv.imshow('Image Learning OpenCV', rimg)  # Displaying image as a new window (windoow name, img)
# #
# # cv.waitKey(0)
# # -----------------------------------------------------------------------------------------------------------------------
#
# def rescaleFrame(height, width):
#     """ Rescaling Live Video"""
#
#     capture = cv.VideoCapture(0)  # Opening videocam
#
#     capture.set(3, width)  # Chaning prop width: 3
#     capture.set(4, height)  # Chaning prop width: 4
#
#     # + paste readvideo function
#
#
# def grayscale_blur():
#     img = cv.imread('Kunaal.jpg')  # reading pixels of image
#     cv.imshow('Image Learning OpenCV', img)  # Displaying image as a new window (windoow name, img)
#
#     # Grayscale
#     gray = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
#     cv.imshow('Gray', gray)
#
#     # Blurring image
#     blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#     cv.imshow('Blur', blur)
#
#     # Edging Cascade
#     edge = cv.Canny(blur, 50, 50)
#     cv.imshow('Edges', edge)
#
#     cv.waitKey(0)
#
#
# def colourdetection():
#     img = cv.imread('Kunaal.jpg')  # reading pixels of image
#
#     def empty(A):
#         pass
#
#
#
#     cv.namedWindow('TrackBars')  # New window called trackbar
#     cv.resizeWindow('TrackBars', 340, 240)  # Resizing Window
#
#     # Trackbars (TrackName, WindowName, IntialVal, MaxVal, function
#     cv.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
#     cv.createTrackbar('Hue Max', 'TrackBars', 47, 179, empty)
#     cv.createTrackbar('Sat Min', 'TrackBars', 104, 255, empty)
#     cv.createTrackbar('Sat Max', 'TrackBars', 102, 255, empty)
#     cv.createTrackbar('Val Min', 'TrackBars', 0, 255, empty)
#     cv.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)
#
#     while True:
#         imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
#         #  Getting value of trackbar (TrackbarName, WindowName)
#         HueMin = cv.getTrackbarPos('Hue Min', 'TrackBars')
#         HueMax = cv.getTrackbarPos('Hue Max', 'TrackBars')
#         SatMin = cv.getTrackbarPos('Sat Min', 'TrackBars')
#         SatMax = cv.getTrackbarPos('Sat Max', 'TrackBars')
#         ValMin = cv.getTrackbarPos('Val Min', 'TrackBars')
#         ValMax = cv.getTrackbarPos('Val Max', 'TrackBars')
#
#         print(HueMin, HueMax, SatMin, SatMax, ValMin, ValMax)
#
#         lower = np.array([HueMin, SatMin, ValMin])
#         upper = np.array([HueMax, SatMax, ValMax])
#         mask = cv.inRange(imgHSV, lower, upper)
#         imgResult = cv.bitwise_and(img, img, mask = mask)
#
#         cv.imshow('Image HSV', imgHSV)
#         cv.imshow('Mask', mask)
#         cv.imshow('Result', imgResult)
#
#         cv.waitKey(1)
#
# colourdetection()
#
#
#
# def airPainting():
#
#     capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access
#
#     capture.set(3, 640)  # height
#     capture.set(4, 480)  # width
#     capture.set(10, 130)  # brightness
#
#     while True:
#         isTrue, frame = capture.read()  # Captures the video frame by frame & isTrue bolean indicating whether it's successful or not
#         cv.imshow('Video Learning OpenCV', frame)  # Displaying video as a new window (windoow name, img)
#
#         if cv.waitKey(20) & 0xFF == ord('Q'):  # break the loop if key 'c' is pressed
#             break
#
#     capture.release()
#     cv.destroyWindow()  # Destroy all window
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import cv2
import numpy as np

#### global ####
x, y, k = 200, 200, -1

cap = cv2.VideoCapture(0)


def take_inp(event, x1, y1, flag, param):
    global x, y, k
    if event == cv2.EVENT_LBUTTONDOWN:
        x = x1
        y = y1
        k = 1


cv2.namedWindow("enter_point")
cv2.setMouseCallback("enter_point", take_inp)

# taking input point
while True:

    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("enter_point", inp_img)

    if k == 1 or cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break

stp = 0
# opical flow starts here


old_pts = np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2)

mask = np.zeros_like(inp_img)

while True:
    _, new_inp_img = cap.read()
    new_inp_img = cv2.flip(new_inp_img, 1)
    new_gray = cv2.cvtColor(new_inp_img, cv2.COLOR_BGR2GRAY)
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img,
                                                    new_gray,
                                                    old_pts,
                                                    None, maxLevel=1,
                                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                              15, 0.08))

    for i, j in zip(old_pts, new_pts):
        x, y = j.ravel()
        a, b = i.ravel()
        if cv2.waitKey(2) & 0xff == ord('q'):
            stp = 1

        elif cv2.waitKey(2) & 0xff == ord('w'):
            stp = 0

        elif cv2.waitKey(2) == ord('n'):
            mask = np.zeros_like(new_inp_img)

        if stp == 0:
            mask = cv2.line(mask, (a, b), (x, y), (0, 0, 255), 6)

        cv2.circle(new_inp_img, (x, y), 6, (0, 255, 0), -1)

    new_inp_img = cv2.addWeighted(mask, 0.3, new_inp_img, 0.7, 0)
    cv2.putText(mask, "'q' to gap 'w' - start 'n' - clear", (10, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow("ouput", new_inp_img)
    cv2.imshow("result", mask)

    gray_inp_img = new_gray.copy()
    old_pts = new_pts.reshape(-1, 1, 2)

    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
cap.release()