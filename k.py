import cv2 as cv
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import keyboard
import tkinter
from tkinter import messagebox
import webbrowser
import turtle

screen = tk.Tk()
screen.wm_title('HackED Beta Project - SmartHandUtil')
screen.geometry('800x600')
screen.resizable(0, 0)

THICKNESS = 10
# capture = cv.VideoCapture(0)  # Either path of video file you wanna play or int 0,1,2 for webcam access
WRITE = False
SHOW = True

myColors = [[0, 80, 231, 179, 208, 255]]
myColorValues = [[51, 53, 255]]

myPoints = []  ## [x, y, colorId]

'''Canvus on Tkinter'''
canvas = tk.Canvas(screen)
canvas.config(width=700, height=500, background='grey')
canvas.place(x=50, y=50)
root = turtle.TurtleScreen(canvas)
canvas.create_text(30, -240, text="Welcome to SmartHandUtil", fill="black", font=('Helvetica 15 bold'))

'''Logo initialization on Tkinter'''
t = turtle.RawTurtle(root, shape="turtle")
# s = turtle.Screen()
t.speed(1000)
i = 50
t.width(2)
t.pensize(0)
count = 0

while True:
    if count == 3:
        t.clear()
        root.clearscreen
        break
    else:
        count += 1
        t.setposition(x=0, y=-50)
        t.forward(10)
        color = ['red', 'blue', 'green', 'black']
        fillcolor = ['orange', 'darkblue', 'darkgreen', 'brown']
        for i in range(4):
            t.begin_fill()
            t.color(color[i], fillcolor[i])
            t.right(90)
            t.circle(110, extent=180)

            t.forward(190)
            t.circle(20, 180)
            t.forward(140)
            t.right(180)

            t.forward(190)
            t.circle(20, 180)
            t.forward(170)
            t.right(180)

            t.forward(185)
            t.circle(20, 180)
            t.forward(185)
            t.right(180)

            t.forward(150)
            t.circle(20, 180)
            t.forward(170)
            t.right(180)
            t.end_fill()

canvas.destroy()


# window = cv.namedWindow("Air",cv.WINDOW_FULLSCREEN)
def Readme():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open_new('https://github.com/kunaal-gupta/SmartHandUtil/blob/main/README')


def GettingStarted():
    file = open('About.txt')
    text = file.read()
    messagebox.showinfo("About SmartHandUtil", text)


def resize(frame, scale):
    """Resizing an image, Video or live video """
    width = int(frame.shape[1] * scale)  # Accessing width from the frame & increasing it by scale times
    height = int(frame.shape[0] * scale)  # Accessing height from the frame & increasing it by scale times
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def findColor(img, myColors):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(myColors[0][0:3])
        upper = np.array(myColors[0][3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = Contours(mask)
        cv.circle(imgResult, (x, y), 10, myColorValues[0], cv.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1

    return newPoints


def Contours(img):
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
        if point != 'skip':
            cv.circle(imgFlip, (point[0], point[1]), 1, myColorValues[0], 10, lineType=-1)

    if len(myPoints) > 1:
        if myPoints[-1] != 'skip' and myPoints[-2] != 'skip':
            last = myPoints[-1]
            lastS = myPoints[-2]
            cv.line(imgFlip, (last[0], last[1]), (lastS[0], lastS[1]), myColorValues[0], THICKNESS)
        elif len(myPoints) > 2 and myPoints[-2] != 'skip':
            last = myPoints[-2]
            lastS = myPoints[-3]
            cv.line(imgFlip, (last[0], last[1]), (lastS[0], lastS[1]), myColorValues[0], THICKNESS)


def draw_lines(myPoints, myColorValues):
    for index in range(len(myPoints)):
        if index > 0 and (myPoints[index] != 'skip' and myPoints[index - 1] != 'skip'):
            last = myPoints[index]
            lastS = myPoints[index - 1]
            cv.line(imgFlip, (last[0], last[1]), (lastS[0], lastS[1]), myColorValues[0], 10)


def air_draw():
    global WRITE
    tk.messagebox.showinfo("Air Draw Info",
                           "You are about to enable air draw feature of this project.\nPress 'h' to play & pause. Press q to quite")

    if WRITE:
        WRITE = False
        myPoints.append('skip')
    else:
        WRITE = True


'''Icons for different choice'''
photo = tkinter.PhotoImage(file=r"Icons/writing.png")
Click = tkinter.PhotoImage(file=r"Icons/clicker.png")
mic = tkinter.PhotoImage(file=r"Icons/microphone.png")

"""Color panel for pen """
orange = tkinter.PhotoImage(file=r"Icons/orange.png")
blue = tkinter.PhotoImage(file=r"Icons/blue.png")
green = tkinter.PhotoImage(file=r"Icons/green.png")
yellow = tkinter.PhotoImage(file=r"Icons/yellow.png")
black = tkinter.PhotoImage(file=r"Icons/black.png")

'''Menu bar in GUI '''
menubar = tkinter.Menu(screen)

FileMenu = tkinter.Menu(screen, tearoff=0)
FileMenu.add_command(label='Open')
FileMenu.add_command(label='Save as')
FileMenu.add_command(label='Settings')
FileMenu.add_command(label='Exit', command=screen.destroy)

EditMenu = tk.Menu(screen, tearoff=0)
EditMenu.add_command(label='Undo')
EditMenu.add_command(label='Clear')

HelpMenu = tk.Menu(screen, tearoff=0)
HelpMenu.add_command(label='About', command=Readme)
HelpMenu.add_command(label='Getting Started', command=GettingStarted)
HelpMenu.add_command(label='Submit a Feedback')

menubar.add_cascade(label='File', menu=FileMenu)
menubar.add_cascade(label='Edit', menu=EditMenu)
menubar.add_cascade(label='Help', menu=HelpMenu)

screen.config(menu=menubar)

''' Buttons on GUI '''
B = tk.Button(screen, height=50, width=50, text='General Use Cursor', image=Click, activebackground='lightgrey',
              border=3)
B.place(x=20, y=20)
B = tk.Button(screen, height=50, width=50, text='Draw in Air', image=photo, activebackground='lightgrey', border=3,
              command=air_draw)
B.place(x=20, y=90)
B = tk.Button(screen, height=50, width=50, text='Use voice to action', image=mic, activebackground='lightgrey',
              border=3)
B.place(x=20, y=160)

B = tk.Button(screen, height=30, width=35, border=0, image=orange)
B.place(x=90, y=20)
B = tk.Button(screen, height=30, width=35, border=0, image=black)
B.place(x=135, y=20)
B = tk.Button(screen, height=30, width=35, border=0, image=blue)
B.place(x=180, y=20)
B = tk.Button(screen, height=30, width=35, border=0, image=yellow)
B.place(x=225, y=20)
B = tk.Button(screen, height=30, width=35, border=0, image=green)
B.place(x=270, y=20)

video = tk.Label(screen)

video.place(bordermode=tk.OUTSIDE, x=100, y=100)
capture = cv.VideoCapture(0)

while True:
    isTrue, img = capture.read()  # Captures the video frame by frame & isTrue boolean indicating whether it's successful or not
    imgResult = img.copy()
    imgFlip = cv.flip(imgResult, 1)

    if WRITE:
        newPoints = findColor(imgFlip, myColors)

        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvus(myPoints, myColorValues)
        draw_lines(myPoints, myColorValues)

    # cv.imshow('Air', imgFlip)  # Displaying video as a new window (windoow name, img)
    cv2image = cv.cvtColor(imgFlip, cv.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    # # Setting the image on the label
    video.config(image=imgtk)
    screen.update()  # Updates the Tkinter window

    if keyboard.is_pressed("q"):
        print('q')

        break
    elif keyboard.is_pressed("h"):
        print('h is pressed')
        if WRITE:
            WRITE = False
            myPoints.append('skip')
        else:
            WRITE = True

capture.release()
cv.destroyWindow()

screen.mainloop()
