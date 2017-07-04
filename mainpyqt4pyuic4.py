import sys
from PyQt4 import QtGui, QtCore
from mainwindowpyqt4 import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
        ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

                ### Hooks to for buttons
        self.ui.pushButtonOn.clicked.connect(lambda: self.pressedOnButton())
        self.ui.pushButtonOff.clicked.connect(lambda: self.pressedOffButton())
        # go on setting up your handlers like:
        # self.ui.okButton.clicked.connect(function_name)
        # etc...

def main():
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
