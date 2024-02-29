from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

from Utils import *
width, height = Scale_Width_Height()

class UI_Genarate(object):
    def setupUi(self, UI, Widget):
        # Show waiting dialog
        self.waiting_dialog = WaitingDialog(widget_manager, UI)
        
        self.centralwidget = QtWidgets.QWidget(UI)
        
        self.widget = Widget()
        self.widget.setupUi(UI)
        
        QtCore.QMetaObject.connectSlotsByName(UI)
        self.waiting_dialog = WaitingDialog(widget_manager, UI_instance.Get())
        
        widget_manager.close_all_widgets()

    def widgetSet(self, UI, WidgetSet):
        Widget = WidgetSet
        self.setupUi(UI, Widget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = UI_Genarate()
    Main_Window.show()
    sys.exit(app.exec_())

