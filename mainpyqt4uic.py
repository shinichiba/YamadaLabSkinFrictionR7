import sys
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
        ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")
        
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.pushButtonOn.clicked.connect(lambda: self.pressedOnButton())
        self.pushButtonOff.clicked.connect(lambda: self.pressedOffButton())
        
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
