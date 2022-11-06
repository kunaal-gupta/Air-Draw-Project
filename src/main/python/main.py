from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox, QHBoxLayout,
                             QPushButton, QRadioButton, QVBoxLayout, QMessageBox)
import sys
from AirDraw import airdraw

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.topRightGroupBox = QGroupBox("Group 2")
        self.win = None
        # self.btnstate()
        self.originalPalette = QApplication.palette()
        self.setWindowTitle('Hacked Beta Project')
        QApplication.setPalette(self.originalPalette)
        self.readme()
        self.createTopLeftGroupBox()


        topLayout = QHBoxLayout()
        topLayout.addStretch(1)


        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.readme, 2, 1)


        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Options: ")

        radioButton1 = QRadioButton("General Use Cursor")
        radioButton2 = QRadioButton("Draw in Air")
        radioButton3 = QRadioButton("Use voice to action")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)

        radioButton1.toggled.connect(lambda: self.btnstate(radioButton1))
        radioButton2.toggled.connect(lambda: self.btnstate(radioButton2))
        radioButton3.toggled.connect(lambda: self.btnstate(radioButton3))



        self.topLeftGroupBox.setLayout(layout)

    def btnstate(self, b):

        if b.text() == "General Use Cursor":
            if b.isChecked() == True:
                Obj = airdraw()
                Obj.run()
        elif b.text() == "Draw in Air":
            if b.isChecked() == True:
                Obj = airdraw()
                Obj.run()
        elif b.text() == "Use voice to action":
            if b.isChecked() == True:
                Obj = airdraw()
                Obj.run()


    def readme(self):
        self.readme = QGroupBox("Help: ")

        b1 = QPushButton("ReadMe")
        b1.setCheckable(True)
        b1.clicked.connect(self.openReadMe)
        # b1.toggle()

        layout = QVBoxLayout()
        layout.addWidget(b1)
        self.readme.setLayout(layout)

    def openReadMe(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("SmartHand Developed by Dynamic-Dev")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("About SmartHand")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()


if __name__ == '__main__':
    appctxt = ApplicationContext()
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(appctxt.app.exec())
