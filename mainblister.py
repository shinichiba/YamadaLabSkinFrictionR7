# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt4 GUI
#
import RPi.GPIO as GPIO
import time
import os
#GPIO.setwarnings(False)
# Set the layout for the pin declaration
GPIO.setmode(GPIO.BOARD)


# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Control Port GPIOs
SP=3  # Start Port
DP=5 # Direction Port
# set up the GPIO channels -  output
GPIO.cleanup() 
GPIO.setup(SP, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)

import sys  # We need sys so that we can pass argv to QApplication
from PyQt4 import QtGui, uic  # Import the PyQt4 module we'll need

class MyWindow(QtGui.QMainWindow):
    # access variables inside of the UI's file
        ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")
        print (self.lineEditRubbingSpeed.text())
        # output to Direction Port
        GPIO.output(DP, True)

    def pressedOffButton(self):
        print ("Pressed Off!")
        # output to Direction Port
        GPIO.output(DP, False)
        
    def lineEditRubbingSpeedtextChanged(self):
        print ("TExt changed")
        print (self.lineEditRubbingSpeed.text())
        GPIO.output(SP, True)
        
    def pressedStartButton(self):
        print ("Pressed Start!")
        # output to Start Port
        GPIO.output(SP, True)
        
    def pressedStopButton(self):
        print ("Pressed Stop!")
        # output to Start Port
        GPIO.output(SP, False)
        
    def pressedResetButton(self):
        print ("Pressed Reset!")
        # output to Start Port
        GPIO.output(SP, False)
        
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

           ### Hooks to for buttons
        self.pushButtonOn.clicked.connect(lambda: self.pressedOnButton())
        self.pushButtonOff.clicked.connect(lambda: self.pressedOffButton())
        self.pushButtonStart.clicked.connect(lambda: self.pressedStartButton())
        self.pushButtonStop.clicked.connect(lambda: self.pressedStopButton())
        self.pushButtonReset.clicked.connect(lambda: self.pressedResetButton())
        


      #  self.lineEditRubbingSpeed.textChanged.connect(lambda: self.lineEditRubbingSpeedtextChanged())
        
        self.show()
# I feel better having one of these
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    window = MyWindow()
    sys.exit(app.exec_())  # and execute the ap
    # when your code ends, the last line before the program exits would be...  
    GPIO.cleanup() 
# python bit to figure how who started This
if __name__ == '__main__':  # if we're running file directly and not importing it
    main() # run the main function

