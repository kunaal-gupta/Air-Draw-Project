import tkinter as tk
import tkinter
import cv2 as cv
from PIL import Image, ImageTk
import AppOpener
from tkinter import messagebox
import webbrowser
import turtle
from AirDraw import airdraw
import cv2 as cv
import numpy as np
import pyautogui as pg



myPoints = []  ## [x, y, colorId]
def resize(frame, scale):
    """Resizing an image, Video or live video """
    width = int(frame.shape[1] * scale)  # Accessing width from the frame & increasing it by scale times
    height = int(frame.shape[0] * scale)  # Accessing height from the frame & increasing it by scale times
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def Readme():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open_new('https://github.com/kunaal-gupta/SmartHandUtil/blob/main/README')

def GettingStarted():
    file = open('About.txt')
    text = file.read()
    messagebox.showinfo("About SmartHandUtil", text)


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



''' Tkinter Window'''
screen = tk.Tk()
screen.wm_title('HackED Beta Project - SmartHandUtil')
screen.geometry('800x600')
screen.resizable(0, 0)



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
B = tk.Button(screen, height=50, width=50, text='General Use Cursor', image=Click, activebackground='lightgrey', border=3)
B.place(x=20, y=20)
B = tk.Button(screen, height=50, width=50, text='Draw in Air', image=photo, activebackground='lightgrey', border=3)
B.place(x=20, y=90)
B = tk.Button(screen, height=50, width=50, text='Use voice to action', image=mic, activebackground='lightgrey',border=3)
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

""" Video on GUI """
video = tk.Label(screen)

video.place(bordermode=tk.OUTSIDE, x=550, y=400)
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()  # Captures the video frame by frame & isTrue bolean indicating whether it's successful or not
    rframe = resize(frame, 0.3)
    kframe = rframe.copy()
    imgFlip = cv.flip(kframe, 1)

    if WRITE:
        newPoints = findColor(imgFlip, myColors)

        if len(newPoints) != 0:
            for newP in newPoints:
                myPoints.append(newP)

                # pg.moveTo(newPoints[0][0]*multiplier, newPoints[0][1]*multiplier)
                # print(pg.position())

    if len(myPoints) != 0:
        drawOnCanvus(myPoints, myColorValues)
        draw_lines(myPoints, myColorValues)

    cv2image = cv.cvtColor(imgFlip, cv.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image=img)


    # Setting the image on the label
    video.config(image=imgtk)

    screen.update()  # Updates the Tkinter window
    if not SHOW:
        cv.resizeWindow("Air", 60, 30)
    key = cv.waitKey(1) & 0xFF # break the loop if key 'c' is pressed


    if key == ord('h'):
        print('h is pressed')
        if WRITE:
            WRITE = False
            myPoints.append('skip')
        else:
            WRITE = True



capture.release()
cv.destroyWindow()

screen.mainloop()
