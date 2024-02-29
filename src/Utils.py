from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os

import pyautogui

def Scale_Width_Height():
    scale = 1
    size_screen = pyautogui.size()
    width = ((size_screen.width / scale) / 683)
    height = ((size_screen.height / scale) / 400)
    return width, height

width, height = Scale_Width_Height()

# Set the XAUTHORITY environment variable to the correct path
os.environ['XAUTHORITY'] = '/home/pi/.Xauthority'



class WidgetManager:
    def __init__(self):
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)
        
    def remove_widget(self, widget):
        self.widgets.remove(widget)

    def close_all_widgets(self):
        for widget in self.widgets:
            widget.close()
        self.widgets = []

widget_manager = WidgetManager()


class WaitingDialog(QDialog):
    def __init__(self, widget_manager, parent=None):
        super(WaitingDialog, self).__init__(parent)
        self.setWindowTitle("Waiting...")
        self.setModal(True)
        self.setFixedSize(int(100 * width), int(110 * height))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        font = QFont()
        font.setPointSize(int(10 * height))
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.img_label = QLabel()
        self.img_label.setPixmap(QPixmap(":/image/load.png"))

        self.img_label.setScaledContents(True)
        layout.addWidget(self.img_label, alignment=Qt.AlignCenter)

        self.retranslateUi()
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        widget_manager.add_widget(self)
        self.show()
        QtWidgets.QApplication.processEvents()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("loading", "กรุณารอสักครู่..."))

class Widget_Window:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

UI_instance = Widget_Window()

def show_widget_fullscreen(widget):
    widget.showFullScreen()
    # widget.showNormal()

class drug_List_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_list_instance = drug_List_Data()
        
class drug_Name_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_name_instance = drug_Name_Data()

class drug_ID:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_ID_instance = drug_ID()

class each_drug_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

each_drug_instance = each_drug_Data()

class each_drug_2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

each_drug_2_instance = each_drug_2_Data()

class drug_Update_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_Update_instance = drug_Update_Data()

class drug_Update_2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

drug_Update_2_instance = drug_Update_2_Data()

class day_start_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

day_start_instance = day_start_Data()

class select_meal_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

select_meal_instance = select_meal_Data()

class data_checkui1_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui1_instance = data_checkui1_Data()

class data_checkui2_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui2_instance = data_checkui2_Data()

class data_checkui3_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

data_checkui3_instance = data_checkui3_Data()

class meal_label_text:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

meal_label_instance = meal_label_text()

class wifi_name_Data:
    def __init__(self):
        self.value = None
        
    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value

wifi_name_instance = wifi_name_Data()

class prepare_Data:
    def __init__(self):
        self._value = None

    def Get(self):
        return self._value

    def Set(self, new_value):
        self._value = new_value
        
prepare_instance = prepare_Data()