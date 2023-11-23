import os
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

def handleVisibleChanged():
    if not QtGui.QGuiApplication.inputMethod().isVisible():
        return
    for w in QtGui.QGuiApplication.allWindows():
        if w.metaObject().className() == "QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QtCore.QObject, "keyboard")
            if keyboard is not None:
                r = w.geometry()
                r.moveTop(keyboard.property("y"))
                w.setMask(QtGui.QRegion(r))
                return

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.line_edit = None
        self.init_ui()

    def init_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.line_edit2)
        self.setCentralWidget(self.main_widget)
        
        QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
