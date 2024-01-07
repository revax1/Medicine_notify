from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import json

from module import SensorThread
import os

class NotifyThread(QThread):
    update_signal = pyqtSignal(bool)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super(NotifyThread, self).__init__(parent)
        self.main_state_file = 'main_state.txt'

    def run(self):
        while True:
            # print("hi there")
            self.homepage = self.load_main_state()
            
            # self.update_signal.emit()
            if self.homepage:
                print("get homepage")
                self.update_signal.emit(self.homepage)
                self.save_main_state(False)
                # self.finished.emit()
            self.msleep(1000)  # Wait for 1 second
            
    # def handle_current_time_signal(self):
    # def print(self):
    #     print("hi")
    
    def load_main_state(self):
        if os.path.exists(self.main_state_file):
            with open(self.main_state_file, 'r') as f:
                content = f.read().strip()
                state = content == 'True'
                # print(f'Loaded state: {state}')
                return state
        return False

    def save_main_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.main_state_file, 'w') as f:
            f.write(prepare_str)

class Ui_notify(object):
    def setupUi(self, notify):
        UI_instance.Set(notify)
        show_widget_fullscreen(notify)
        
        self.state_file = '/home/pi/Documents/Medicine_notify/state/servo_state.txt'
        self.prepare_state_file = '/home/pi/Documents/Medicine_notify/state/prepare_state.txt'
        self.meal_drug_list_file = '/home/pi/Documents/Medicine_notify/state/meal_drug_list.json'
        self.notify_state_file = '/home/pi/Documents/Medicine_notify/state/notify_state.txt'
        # self.main_state_file = '/home/pi/Documents/Medicine_notify/state/main_state.txt'

        notify.setObjectName("notify")
        notify.resize(int(683 * width), int(400 * height))
        notify.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(notify)
        self.centralwidget.setObjectName("centralwidget")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(int(190 * width), int(20 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(20 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label6.setFont(font)
        self.label6.setStyleSheet("border-radius: 34px;\n"
"color: rgb(23, 73, 110);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label6)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label6.setGraphicsEffect(shadow)
        self.label6.setFrameShape(QtWidgets.QFrame.Box)
        self.label6.setLineWidth(int(1 * width))
        self.label6.setTextFormat(QtCore.Qt.AutoText)
        self.label6.setScaledContents(False)
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setWordWrap(True)
        self.label6.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.label6)
        self.img_label.setGeometry(QtCore.QRect(int(50 * width), int(9 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/notify.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(195 * width), int(100 * height), int(275 * width), int(275 * height)))
        self.frame.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(int(8 * width), int(10 * height), int(260 * width), int(260 * height)))
        self.frame_2.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.time_name = QtWidgets.QLabel(self.frame_2)
        self.time_name.setGeometry(QtCore.QRect(int(20 * width), int(10 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.time_name.setFont(font)
        self.time_name.setStyleSheet("border-radius: 16px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.time_name)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.time_name.setGraphicsEffect(shadow)
        self.time_name.setFrameShape(QtWidgets.QFrame.Box)
        self.time_name.setLineWidth(int(1 * width))
        self.time_name.setTextFormat(QtCore.Qt.AutoText)
        self.time_name.setScaledContents(False)
        self.time_name.setAlignment(QtCore.Qt.AlignCenter)
        self.time_name.setWordWrap(True)
        self.time_name.setObjectName("time_name")
        self.meal_name = QtWidgets.QLabel(self.frame_2)
        self.meal_name.setGeometry(QtCore.QRect(int(20 * width), int(60 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.meal_name.setFont(font)
        self.meal_name.setStyleSheet("border-radius: 16px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.meal_name)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.meal_name.setGraphicsEffect(shadow)
        self.meal_name.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_name.setLineWidth(int(1 * width))
        self.meal_name.setTextFormat(QtCore.Qt.AutoText)
        self.meal_name.setScaledContents(False)
        self.meal_name.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_name.setWordWrap(True)
        self.meal_name.setObjectName("meal_name")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(int(20 * width), int(140 * height), int(211 * width), int(100 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(16 * height))
        font.setWeight(int(25 * width))
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.listWidget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.listWidget.setGraphicsEffect(shadow)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(int(20 * width), int(110 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(410, 120, 200, 31))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_2.setFont(font)
        # self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        # self.label_2.setObjectName("label_2")
        notify.setCentralWidget(self.centralwidget)

        self.retranslateUi(notify)
        QtCore.QMetaObject.connectSlotsByName(notify)
        
        # meal_drug_list = meal_drug_list_instance.Get()
        meal_drug_list = self.load_meal_drug_list()
        
        get_prepare = self.load_prepare_state()
        if get_prepare:
                selected_items = []
                
                cur_row, cur_col, servoNum = self.load_state()

                for row, col, drug_id, drug_name, meal_id, meal_name, time, state in meal_drug_list:
                        if col == cur_col and row == cur_row:
                                selected_items.append((row, col, drug_id, drug_name, meal_id, meal_name, time))

                if selected_items:
                        row, col, _, _, _, meal_name, time = selected_items[0]  # Assuming only one item will be selected
                        self.meal_name.setText(f"{meal_name}")
                        self.time_name.setText(f"เวลา {time} น.")
                        for item in selected_items:
                                self.listWidget.addItem(f"- {item[3]}")  # Add drug_name to listWidget
                else:
                        self.meal_name.setText("")
                        self.time_name.setText("")
                        
        # self.homepage = self.load_main_state()  
        # print(self.homepage)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.setupUi(notify))
        # self.timer.start(1000)  # 1 วินาที
        
        self.thread = NotifyThread()
        self.thread.update_signal.connect(self.tohomepage)
        
        self.thread.finished.connect(self.thread.quit)
        self.thread.start()

    def tohomepage(self, get_home):
        # print("hi")
        from main import Ui_Medicine_App
        # self.homepage = self.load_main_state()  
        # print(self.homepage)
        if get_home:
            
            main_form = UI_Genarate()
            main_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)
            self.thread.quit()
            # self.closeWindow()
            
    # def closeWindow(self):
    #     self.close()
            
    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                content = f.read().split(',')
                state = (int(content[0]), int(content[1]), int(content[1]))
                print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
                return state
        return 0, 0, 0  # default values if the file doesn't exist

    def load_prepare_state(self):
        if os.path.exists(self.prepare_state_file):
            with open(self.prepare_state_file, 'r') as f:
                content = f.read().strip()
                state = content == 'True'
                # print(f'Loaded state: {state}')
                return state
        return False

    def load_meal_drug_list(self):
        if os.path.exists(self.meal_drug_list_file):
                with open(self.meal_drug_list_file, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    return content
        return []
            
    def save_notify_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.notify_state_file, 'w') as f:
            f.write(prepare_str)
            
    # def load_main_state(self):
    #     if os.path.exists(self.main_state_file):
    #         with open(self.main_state_file, 'r') as f:
    #             content = f.read().strip()
    #             state = content == 'True'
    #             # print(f'Loaded state: {state}')
    #             return state
    #     return False

    # def save_main_state(self, prepare):
    #     prepare_str = 'True' if prepare else 'False'
    #     with open(self.main_state_file, 'w') as f:
    #         f.write(prepare_str)

    def retranslateUi(self, notify):
        _translate = QtCore.QCoreApplication.translate
        notify.setWindowTitle(_translate("notify", "แจ้งเตือน"))
        self.label6.setText(_translate("notify", "  แจ้งเตือน"))
        # self.close_pushButton.setText(_translate("notify", "ปิดแจ้งเตือน"))
        self.meal_name.setText(_translate("notify", "มื้อเช้า หลังอาหาร"))
        self.time_name.setText(_translate("notify", " เวลา 06:30 น."))
        self.label_2.setText(_translate("notify", "รายการยามีดังนี้"))
        # self.label_2.setText(_translate("notify", "กรุณากดปุ่มด้านล่างนี้"))

import resources_rc

# notify = Ui_notify()

# timer = QTimer()
# timer.timeout.connect(notify.setupUi)
# timer.start(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notify = QtWidgets.QMainWindow()
    ui = Ui_notify()
    ui.setupUi(notify)
    notify.show()
    
    # from main import Ui_Medicine_App
    # app = QtWidgets.QApplication(sys.argv)
    # notify = QtWidgets.QMainWindow()
    # ui = Ui_Medicine_App()
    # ui.setupUi(notify)
    # notify.show()
    
    sensor_thread = SensorThread()
    sensor_thread.run_thread()
    # sensor_thread.current_time_signal.connect(ui.handle_current_time_signal)
    

    sys.exit(app.exec_())
