from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from timeEdit import Ui_time_Edit

class Ui_select_time(object):
    def convert_thai_to_arabic(self, input_string):
        thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
        arabic_numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for thai, arabic in zip(thai_numerals, arabic_numerals):
                input_string = input_string.replace(thai, arabic)
        return input_string

    def open_time_edit(self, meal_label_text):
        meal_label_instance.Set(meal_label_text)

        time_edit_form = UI_Genarate()
        time_edit_form.widgetSet(UI_instance.Get(), Ui_time_Edit)

    def setupUi(self, select_time):
        UI_instance.Set(select_time)
        show_widget_fullscreen(select_time)

        select_time.setObjectName("select_time")
        select_time.resize(int(683 * width), int(400 * height))
        select_time.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(select_time)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(int(1 * width))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(260 * width), int(80 * height), int(38 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/selecttime_icon.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(int(350 * width), int(150 * height), int(141 * width), int(181 * height)))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.bd_label = QtWidgets.QLabel(self.frame_9)
        self.bd_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bd_label.setFont(font)
        self.bd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bd_label.setObjectName("bd_label")
        self.ad_label = QtWidgets.QLabel(self.frame_9)
        self.ad_label.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.ad_label.setFont(font)
        self.ad_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ad_label.setObjectName("ad_label")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(int(510 * width), int(150 * height), int(141 * width), int(181 * height)))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.bbed_label = QtWidgets.QLabel(self.frame_12)
        self.bbed_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bbed_label.setFont(font)
        self.bbed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bbed_label.setObjectName("bbed_label")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(int(30 * width), int(150 * height), int(141 * width), int(181 * height)))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.bb_label = QtWidgets.QLabel(self.frame_5)
        self.bb_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bb_label.setFont(font)
        self.bb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bb_label.setObjectName("bb_label")
        self.ab_label = QtWidgets.QLabel(self.frame_5)
        self.ab_label.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.ab_label.setFont(font)
        self.ab_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ab_label.setObjectName("ab_label")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(int(350 * width), int(310 * height), int(141 * width), int(41 * height)))
        self.frame_8.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_8)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_8.setGraphicsEffect(shadow)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(int(350 * width), int(110 * height), int(141 * width), int(61 * height)))
        self.frame_10.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.d_label = QtWidgets.QLabel(self.frame_10)
        self.d_label.setGeometry(QtCore.QRect(int(10 * width), int(0 * height), int(121 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.img_dt_label = QtWidgets.QLabel(self.centralwidget)
        self.img_dt_label.setGeometry(QtCore.QRect(int(375 * width), int(118 * height), int(25 * width), int(24 * height)))
        self.img_dt_label.setText("")
        self.img_dt_label.setPixmap(QtGui.QPixmap(":/icons/d_tab.png"))
        self.img_dt_label.setScaledContents(True)
        self.img_dt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_dt_label.setObjectName("img_dt_label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(30 * width), int(110 * height), int(141 * width), int(61 * height)))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.b_label = QtWidgets.QLabel(self.frame_2)
        self.b_label.setGeometry(QtCore.QRect(int(10 * width), int(0 * height), int(121 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        
        self.img_bt_label = QtWidgets.QLabel(self.centralwidget)
        self.img_bt_label.setGeometry(QtCore.QRect(int(50 * width), int(118 * height), int(35 * width), int(26 * height)))
        self.img_bt_label.setText("")
        self.img_bt_label.setPixmap(QtGui.QPixmap(":/icons/b_tab.png"))
        self.img_bt_label.setScaledContents(True)
        self.img_bt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_bt_label.setObjectName("img_bt_label")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(int(510 * width), int(310 * height), int(141 * width), int(41 * height)))
        self.frame_13.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_13)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_13.setGraphicsEffect(shadow)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(int(190 * width), int(150 * height), int(141 * width), int(181 * height)))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.bl_label = QtWidgets.QLabel(self.frame_6)
        self.bl_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bl_label.setFont(font)
        self.bl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bl_label.setObjectName("bl_label")
        self.al_label = QtWidgets.QLabel(self.frame_6)
        self.al_label.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(121 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.al_label.setFont(font)
        self.al_label.setAlignment(QtCore.Qt.AlignCenter)
        self.al_label.setObjectName("al_label")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(int(190 * width), int(310 * height), int(141 * width), int(41 * height)))
        self.frame_7.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_7)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_7.setGraphicsEffect(shadow)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(int(30 * width), int(310 * height), int(141 * width), int(41 * height)))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_4)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_4.setGraphicsEffect(shadow)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(int(510 * width), int(110 * height), int(141 * width), int(61 * height)))
        self.frame_11.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.bed_label = QtWidgets.QLabel(self.frame_11)
        self.bed_label.setGeometry(QtCore.QRect(int(20 * width), int(0 * height), int(105 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.img_bedt_label = QtWidgets.QLabel(self.centralwidget)
        self.img_bedt_label.setGeometry(QtCore.QRect(int(522 * width), int(120 * height), int(30 * width), int(24 * height)))
        self.img_bedt_label.setText("")
        self.img_bedt_label.setPixmap(QtGui.QPixmap(":/icons/bed_tab.png"))
        self.img_bedt_label.setScaledContents(True)
        self.img_bedt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_bedt_label.setObjectName("img_bedt_label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(190 * width), int(110 * height), int(141 * width), int(61 * height)))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.l_label = QtWidgets.QLabel(self.frame_3)
        self.l_label.setGeometry(QtCore.QRect(int(10 * width), int(0 * height), int(121 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        self.img_lt_label = QtWidgets.QLabel(self.centralwidget)
        self.img_lt_label.setGeometry(QtCore.QRect(int(212 * width), int(118 * height), int(28 * width), int(24 * height)))
        self.img_lt_label.setText("")
        self.img_lt_label.setPixmap(QtGui.QPixmap(":/icons/l_tab.png"))
        self.img_lt_label.setScaledContents(True)
        self.img_lt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_lt_label.setObjectName("img_lt_label")
        self.bb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bb_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(170 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 109, 109);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bb_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bb_pushButton.setGraphicsEffect(shadow)
        self.bb_pushButton.setObjectName("bb_pushButton")
        self.ab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ab_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(260 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ab_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.ab_pushButton.setGraphicsEffect(shadow)
        self.ab_pushButton.setObjectName("ab_pushButton")
        self.bl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bl_pushButton.setGeometry(QtCore.QRect(int(210 * width), int(170 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(239, 151, 204);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bl_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bl_pushButton.setGraphicsEffect(shadow)
        self.bl_pushButton.setObjectName("bl_pushButton")
        self.al_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.al_pushButton.setGeometry(QtCore.QRect(int(210 * width), int(260 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(169, 212, 98);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.al_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.al_pushButton.setGraphicsEffect(shadow)
        self.al_pushButton.setObjectName("al_pushButton")
        self.bd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bd_pushButton.setGeometry(QtCore.QRect(int(370 * width), int(170 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 143, 76);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bd_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bd_pushButton.setGraphicsEffect(shadow)
        self.bd_pushButton.setObjectName("bd_pushButton")
        self.ad_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ad_pushButton.setGeometry(QtCore.QRect(int(370 * width), int(260 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(119, 156, 212);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ad_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.ad_pushButton.setGraphicsEffect(shadow)
        self.ad_pushButton.setObjectName("ad_pushButton")
        self.bbed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bbed_pushButton.setGeometry(QtCore.QRect(int(530 * width), int(170 * height), int(101 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(176, 107, 193);\n"
"")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bbed_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bbed_pushButton.setGraphicsEffect(shadow)
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        self.frame_3.raise_()
        self.frame_11.raise_()
        self.frame_10.raise_()
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_9.raise_()
        self.frame_12.raise_()
        self.frame_5.raise_()
        self.frame_13.raise_()
        self.frame_6.raise_()
        self.bb_pushButton.raise_()
        self.ab_pushButton.raise_()
        self.bl_pushButton.raise_()
        self.al_pushButton.raise_()
        self.bd_pushButton.raise_()
        self.ad_pushButton.raise_()
        self.bbed_pushButton.raise_()
        select_time.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_time)
        QtCore.QMetaObject.connectSlotsByName(select_time)

        self.bb_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเช้า ก่อนอาหาร"))
        self.ab_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเช้า หลังอาหาร"))
        self.bl_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเที่ยง ก่อนอาหาร"))
        self.al_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเที่ยง หลังอาหาร"))
        self.bd_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเย็น ก่อนอาหาร"))
        self.ad_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อเย็น หลังอาหาร"))
        self.bbed_pushButton.clicked.connect(lambda: self.open_time_edit("มื้อก่อนนอน"))

        self.add_back_pushButton.clicked.connect(self.homepage)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))

        self.bb_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bb_pushButton))
        self.bb_pushButton.released.connect(lambda: self.set_button_released_style1(self.bb_pushButton))

        self.ab_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.ab_pushButton))
        self.ab_pushButton.released.connect(lambda: self.set_button_released_style2(self.ab_pushButton))

        self.bl_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bl_pushButton))
        self.bl_pushButton.released.connect(lambda: self.set_button_released_style3(self.bl_pushButton))

        self.al_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.al_pushButton))
        self.al_pushButton.released.connect(lambda: self.set_button_released_style4(self.al_pushButton))

        self.bd_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bd_pushButton))
        self.bd_pushButton.released.connect(lambda: self.set_button_released_style5(self.bd_pushButton))

        self.ad_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.ad_pushButton))
        self.ad_pushButton.released.connect(lambda: self.set_button_released_style6(self.ad_pushButton))

        self.bbed_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.bbed_pushButton))
        self.bbed_pushButton.released.connect(lambda: self.set_button_released_style7(self.bbed_pushButton))

         # Connect to the SQLite database
        self.connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = self.connection.cursor()

        # List of meal names
        meal_names = ["มื้อเช้า ก่อนอาหาร", "มื้อเช้า หลังอาหาร", "มื้อเที่ยง ก่อนอาหาร",
                      "มื้อเที่ยง หลังอาหาร", "มื้อเย็น ก่อนอาหาร", "มื้อเย็น หลังอาหาร", "มื้อก่อนนอน"]

        # Fetch and display times for each meal
        for i, meal_name in enumerate(meal_names, start=1):
                cursor.execute("SELECT time FROM Meal WHERE meal_name = ?", (meal_name,))
                result = cursor.fetchone()

                if result:
                        time_value = result[0]  # Get the time value from the result
                         # Convert Thai numerals to Arabic numerals
                        time_value = self.convert_thai_to_arabic(time_value)
                        # Set the text for each label based on the meal name
                        if meal_name == "มื้อเช้า ก่อนอาหาร":
                                self.bb_label.setText(f"{time_value}")
                        elif meal_name == "มื้อเช้า หลังอาหาร":
                                self.ab_label.setText(f"{time_value}")
                        elif meal_name == "มื้อเที่ยง ก่อนอาหาร":
                                self.bl_label.setText(f"{time_value}")
                        elif meal_name == "มื้อเที่ยง หลังอาหาร":
                                self.al_label.setText(f"{time_value}")
                        elif meal_name == "มื้อเย็น ก่อนอาหาร":
                                self.bd_label.setText(f"{time_value}")
                        elif meal_name == "มื้อเย็น หลังอาหาร":
                                self.ad_label.setText(f"{time_value}")
                        elif meal_name == "มื้อก่อนนอน":
                                self.bbed_label.setText(f"{time_value}")

        # Close the cursor and connection
        cursor.close()
        self.connection.close()

    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style1(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(235, 109, 109);"
        )

    def set_button_released_style2(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(244, 212, 99);"
        )
        
    def set_button_released_style3(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(239, 151, 204);"
        )

    def set_button_released_style4(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(169, 212, 98);"
        )

    def set_button_released_style5(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(235, 143, 76);"
        )

    def set_button_released_style6(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(119, 156, 212);"
        )

    def set_button_released_style7(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(176, 107, 193);"
        )

    def homepage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def retranslateUi(self, select_time):
        _translate = QtCore.QCoreApplication.translate
        select_time.setWindowTitle(_translate("select_time", "ตั้งเวลามื้อยา"))
        self.b_label.setText(_translate("select_time", "    มื้อเช้า"))
        self.add_back_pushButton.setText(_translate("select_time", "ย้อนกลับ"))
        self.d_label.setText(_translate("select_time", "  มื้อเย็น"))
        self.l_label.setText(_translate("select_time", "    มื้อเที่ยง"))
        self.label.setText(_translate("select_time", "      ตั้งเวลามื้อยา"))
        self.bed_label.setText(_translate("select_time", "      มื้อก่อนนอน"))
        self.bb_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ab_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bl_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.al_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bd_pushButton.setText(_translate("select_time", "ก่อน อาหาร"))
        self.ad_pushButton.setText(_translate("select_time", "หลัง อาหาร"))
        self.bbed_pushButton.setText(_translate("select_time", "ก่อนนอน"))
        self.bd_label.setText(_translate("select_time", "ก่อนอาหาร"))
        self.ad_label.setText(_translate("select_time", "หลังอาหาร"))
        self.bbed_label.setText(_translate("select_time", "ก่อนนอน"))
        self.bb_label.setText(_translate("select_time", "ก่อนอาหาร"))
        self.ab_label.setText(_translate("select_time", "หลังอาหาร"))
        self.bl_label.setText(_translate("select_time", "ก่อนอาหาร"))
        self.al_label.setText(_translate("select_time", "หลังอาหาร"))

        # Bring img_bt_label to the front
        self.img_bt_label.raise_()
        self.img_lt_label.raise_()
        self.img_dt_label.raise_()
        self.img_bedt_label.raise_()
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_time = QtWidgets.QMainWindow()
    ui = Ui_select_time()
    ui.setupUi(select_time)
    select_time.show()
    sys.exit(app.exec_())
