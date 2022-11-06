from cv2 import cv2 as cv
import pyautogui as pg
import numpy as np
import pytesseract
import time
import subprocess as sp
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

class VtoA():
    def _init_(self):
        pass

    def take_screenshot(self):
        screenshot = pg.screenshot()
        print('screenchot taken')
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        print('converted to BGR')
        return screenshot

    def ss_to_text(self, search_text):
        screenshot = self.take_screenshot()
        # gaussian blur for more efficiency of OTSU's thresh
        gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        cv.imshow('gray', gray)
        ret, thresh1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (14,14))

        dilation = cv.dilate(thresh1, kernel, iterations=1)
        contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        image2 = screenshot.copy()
        for cnt in contours:
            x,y,width,height = cv.boundingRect(cnt)
            textimg = image2[y:y+height, x:x+width]
            text = pytesseract.image_to_string(textimg)
            if text == search_text:
                return x,y,width,height

        return None


    def main_run(self):
        time.sleep(2)
        self.ss_to_text()  #TODO
        cv.waitKey(0)
        cv.destroyAllWindows()

def main():
    obj = VtoA()+
    obj.main_run()

main()