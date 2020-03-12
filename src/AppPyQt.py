import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,
                 showCursor=False,
                 setFullScreen=True,
                 *args, **kwargs):

        # init super QmainWindow
        super().__init__(*args, **kwargs)
        # load from .ui File
        uic.loadUi("qtDesign.ui", self)

        if showCursor:
            self.setCursor(QtCore.Qt.BlankCursor)
        if setFullScreen:
            self.showFullScreen()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(showCursor=False,
                        setFullScreen=False)
    window.show()
    app.exec_()
