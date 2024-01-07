from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

# from data_check import Ui_data_check
from data_checkui1 import Ui_data_check1

class Ui_select_meal(object):
    def setupUi(self, select_meal):
        UI_instance.Set(select_meal)
        show_widget_fullscreen(select_meal)

        self.select_meal = select_meal
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.each_drug2 = each_drug_2_instance.Get()
        self.day_start = day_start_instance.Get()
        self.updated_data2 = drug_Update_2_instance.Get()
        
        select_meal.setObjectName("select_meal")
        select_meal.resize(int(683 * width), int(400 * height))
        select_meal.setStyleSheet("\n"
        "background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(select_meal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: " + str(int(40 * width)) + "px;\n"
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
        self.meal_label = QtWidgets.QLabel(self.frame)
        self.meal_label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.meal_label.setFont(font)
        self.meal_label.setStyleSheet("border-radius: " + str(int(16 * width)) + "px;\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.meal_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.meal_label.setGraphicsEffect(shadow)
        self.meal_label.setFrameShape(QtWidgets.QFrame.Box)
        self.meal_label.setLineWidth(int(1 * width))
        self.meal_label.setTextFormat(QtCore.Qt.AutoText)
        self.meal_label.setScaledContents(False)
        self.meal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.meal_label.setWordWrap(True)
        self.meal_label.setObjectName("meal_label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(238 * width), int(80 * height), int(31 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/each_icon.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.back_pushButton = QtWidgets.QPushButton(self.frame)
        self.back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("border-radius: " + str(int(9 * width)) + "px;\n"
        "color: rgb(0, 0, 0);\n"
    "background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.back_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.back_pushButton.setGraphicsEffect(shadow)
        self.back_pushButton.setObjectName("back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(30 * width), int(120 * height), int(141 * width), int(61 * height)))
        self.frame_2.setStyleSheet("border-radius: " + str(int(16 * width)) + "px;\n"
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
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(int(30 * width), int(260 * height), int(141 * width), int(41 * height)))
        self.frame_4.setStyleSheet("border-radius: " + str(int(16 * width)) + "px;\n"
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
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(int(30 * width), int(160 * height), int(141 * width), int(121 * height)))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.bb_label = QtWidgets.QLabel(self.frame_5)
        self.bb_label.setGeometry(QtCore.QRect(int(30 * width), int(20 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.bb_label.setFont(font)
        self.bb_label.setStyleSheet("border-radius: " + str(int(9 * width)) + "px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(235, 109, 109);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bb_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bb_label.setGraphicsEffect(shadow)
        self.bb_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bb_label.setLineWidth(int(1 * width))
        self.bb_label.setTextFormat(QtCore.Qt.AutoText)
        self.bb_label.setScaledContents(False)
        self.bb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bb_label.setWordWrap(True)
        self.bb_label.setObjectName("bb_label")
        self.bb_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.bb_checkBox.setGeometry(QtCore.QRect(int(10 * width), int(0 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_checkBox.sizePolicy().hasHeightForWidth())
        self.bb_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.bb_checkBox.setFont(font)
        self.bb_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bb_checkBox.setText("")
        self.bb_checkBox.setTristate(False)
        self.bb_checkBox.setObjectName("bb_checkBox")
        self.ab_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.ab_checkBox.setGeometry(QtCore.QRect(int(10 * width), int(60 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ab_checkBox.sizePolicy().hasHeightForWidth())
        self.ab_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.ab_checkBox.setFont(font)
        self.ab_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ab_checkBox.setText("")
        self.ab_checkBox.setTristate(False)
        self.ab_checkBox.setObjectName("ab_checkBox")
        self.ab_label = QtWidgets.QLabel(self.frame_5)
        self.ab_label.setGeometry(QtCore.QRect(int(30 * width), int(80 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.ab_label.setFont(font)
        self.ab_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
        "background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ab_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.ab_label.setGraphicsEffect(shadow)
        self.ab_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ab_label.setLineWidth(int(1 * width))
        self.ab_label.setTextFormat(QtCore.Qt.AutoText)
        self.ab_label.setScaledContents(False)
        self.ab_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ab_label.setWordWrap(True)
        self.ab_label.setObjectName("ab_label")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(int(190 * width), int(160 * height), int(141 * width), int(121 * height)))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(190 * width), int(120 * height), int(141 * width), int(61 * height)))
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
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(int(190 * width), int(260 * height), int(141 * width), int(41 * height)))
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
        self.bl_label = QtWidgets.QLabel(self.centralwidget)
        self.bl_label.setGeometry(QtCore.QRect(int(220 * width), int(180 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.bl_label.setFont(font)
        self.bl_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(239, 151, 204);\n"
        "")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bl_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bl_label.setGraphicsEffect(shadow)
        self.bl_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bl_label.setLineWidth(int(1 * width))
        self.bl_label.setTextFormat(QtCore.Qt.AutoText)
        self.bl_label.setScaledContents(False)
        self.bl_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bl_label.setWordWrap(True)
        self.bl_label.setObjectName("bl_label")
        self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bl_checkBox.setGeometry(QtCore.QRect(int(200 * width), int(160 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bl_checkBox.sizePolicy().hasHeightForWidth())
        self.bl_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.bl_checkBox.setFont(font)
        self.bl_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bl_checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bl_checkBox.setText("")
        self.bl_checkBox.setTristate(False)
        self.bl_checkBox.setObjectName("bl_checkBox")
        self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.al_checkBox.setGeometry(QtCore.QRect(int(200 * width), int(220 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.al_checkBox.sizePolicy().hasHeightForWidth())
        self.al_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.al_checkBox.setFont(font)
        self.al_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.al_checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.al_checkBox.setText("")
        self.al_checkBox.setTristate(False)
        self.al_checkBox.setObjectName("al_checkBox")
        self.al_label = QtWidgets.QLabel(self.centralwidget)
        self.al_label.setGeometry(QtCore.QRect(int(220 * width), int(240 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.al_label.setFont(font)
        self.al_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(169, 212, 98);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.al_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.al_label.setGraphicsEffect(shadow)
        self.al_label.setFrameShape(QtWidgets.QFrame.Box)
        self.al_label.setLineWidth(int(1 * width))
        self.al_label.setTextFormat(QtCore.Qt.AutoText)
        self.al_label.setScaledContents(False)
        self.al_label.setAlignment(QtCore.Qt.AlignCenter)
        self.al_label.setWordWrap(True)
        self.al_label.setObjectName("al_label")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(int(350 * width), int(260 * height), int(141 * width), int(41 * height)))
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
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(int(350 * width), int(160 * height), int(141 * width), int(121 * height)))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.ad_label = QtWidgets.QLabel(self.frame_9)
        self.ad_label.setGeometry(QtCore.QRect(int(30 * width), int(80 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.ad_label.setFont(font)
        self.ad_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(119, 156, 212);\n"
        "")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.ad_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.ad_label.setGraphicsEffect(shadow)
        self.ad_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ad_label.setLineWidth(int(1 * width))
        self.ad_label.setTextFormat(QtCore.Qt.AutoText)
        self.ad_label.setScaledContents(False)
        self.ad_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ad_label.setWordWrap(True)
        self.ad_label.setObjectName("ad_label")
        self.ad_checkBox = QtWidgets.QCheckBox(self.frame_9)
        self.ad_checkBox.setGeometry(QtCore.QRect(int(10 * width), int(60 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_checkBox.sizePolicy().hasHeightForWidth())
        self.ad_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.ad_checkBox.setFont(font)
        self.ad_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ad_checkBox.setText("")
        self.ad_checkBox.setTristate(False)
        self.ad_checkBox.setObjectName("ad_checkBox")
        self.bd_label = QtWidgets.QLabel(self.frame_9)
        self.bd_label.setGeometry(QtCore.QRect(int(30 * width), int(20 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.bd_label.setFont(font)
        self.bd_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(235, 143, 76);\n"
        "")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bd_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bd_label.setGraphicsEffect(shadow)
        self.bd_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bd_label.setLineWidth(int(1 * width))
        self.bd_label.setTextFormat(QtCore.Qt.AutoText)
        self.bd_label.setScaledContents(False)
        self.bd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bd_label.setWordWrap(True)
        self.bd_label.setObjectName("bd_label")
        self.bd_checkBox = QtWidgets.QCheckBox(self.frame_9)
        self.bd_checkBox.setGeometry(QtCore.QRect(int(10 * width), int(0 * height), int(16 * width), int(71 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bd_checkBox.sizePolicy().hasHeightForWidth())
        self.bd_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.bd_checkBox.setFont(font)
        self.bd_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bd_checkBox.setText("")
        self.bd_checkBox.setTristate(False)
        self.bd_checkBox.setObjectName("bd_checkBox")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(int(350 * width), int(120 * height), int(141 * width), int(61 * height)))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(int(245 * width), int(90 * height), int(211 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(int(510 * width), int(120 * height), int(141 * width), int(61 * height)))
        self.frame_11.setStyleSheet("border-radius: 16px;\n"
    "background-color: rgb(244, 212, 99);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.bed_label = QtWidgets.QLabel(self.frame_11)
        self.bed_label.setGeometry(QtCore.QRect(int(20 * width), int(0 * height), int(101 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.bed_label.setFont(font)
        self.bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bed_label.setObjectName("bed_label")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(int(510 * width), int(160 * height), int(141 * width), int(121 * height)))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.bbed_label = QtWidgets.QLabel(self.frame_12)
        self.bbed_label.setGeometry(QtCore.QRect(int(30 * width), int(20 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(50 * width))
        self.bbed_label.setFont(font)
        self.bbed_label.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(176, 107, 193);\n"
        "")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.bbed_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.bbed_label.setGraphicsEffect(shadow)
        self.bbed_label.setFrameShape(QtWidgets.QFrame.Box)
        self.bbed_label.setLineWidth(int(1 * width))
        self.bbed_label.setTextFormat(QtCore.Qt.AutoText)
        self.bbed_label.setScaledContents(False)
        self.bbed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bbed_label.setWordWrap(True)
        self.bbed_label.setObjectName("bbed_label")
        self.bbed_checkBox = QtWidgets.QCheckBox(self.frame_12)
        self.bbed_checkBox.setGeometry(QtCore.QRect(int(10 * width), int(10 * height), int(16 * width), int(51 * height)))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbed_checkBox.sizePolicy().hasHeightForWidth())
        self.bbed_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        self.bbed_checkBox.setFont(font)
        self.bbed_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bbed_checkBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bbed_checkBox.setText("")
        self.bbed_checkBox.setTristate(False)
        self.bbed_checkBox.setObjectName("bbed_checkBox")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(int(510 * width), int(260 * height), int(141 * width), int(41 * height)))
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
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(int(540 * width), int(320 * height), int(71 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
    "color: rgb(0, 0, 0);\n"
    "background-color: rgb(227, 151, 61);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")

        
        self.frame_10.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()
        self.frame_7.raise_()
        self.frame_6.raise_()
        self.bl_label.raise_()
        self.bl_checkBox.raise_()
        self.al_checkBox.raise_()
        self.al_label.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.label_2.raise_()
        self.frame_11.raise_()
        self.frame_12.raise_()
        self.next_pushButton.raise_()
        self.frame_13.raise_()
        self.bbed_label.raise_()
        self.bbed_checkBox.raise_()
        select_meal.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_meal)
        QtCore.QMetaObject.connectSlotsByName(select_meal)
        

        self.back_pushButton.clicked.connect(self.backpage)
        # self.next_pushButton.clicked.connect(close_window)

        # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
        self.next_pushButton.clicked.connect(self.save_checkbox_states_and_close)
        # เพิ่มการเชื่อมต่อฐานข้อมูล SQLite3
        self.conn = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        self.cursor = self.conn.cursor()

        self.set_meal_info(drug_ID_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(select_meal)

        def save_changes():
            updated_data2 = self.updated_data2
            # updated_data2['meals'] = self.label_date.text()
            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
            drug_Update_2_instance.Set(self.updated_data2)
            self.open_data_check1()
        
        self.next_pushButton.clicked.connect(save_changes)
        # self.next_pushButton.clicked.connect(self.closeAll)

         # Set up button press and release styling
        self.back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.back_pushButton))
        self.back_pushButton.released.connect(lambda: self.set_button_released_style(self.back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))


    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(227, 151, 61);"
        )

    
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.day_start.closeAll()  
        self.select_meal.close()
    
    def backpage(self):
        from day_start import Ui_day_start
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_day_start)
        
    def open_data_check1(self):
        drug_Update_2_instance.Set(self.updated_data2)
        select_meal_instance.Set(self)
        day_start_instance.Set(self.day_start)
        each_drug_2_instance.Set(self.each_drug2)
        each_drug_2_instance.Set(self.each_drug)
        drug_list_instance.Set(self.drug_List)

        data_check1_form = UI_Genarate()
        data_check1_form.widgetSet(UI_instance.Get(), Ui_data_check1)

    def set_meal_info(self, drug_id):
        self.drug_id = drug_id

        print(f"select_meal {self.updated_data2}")
        self.meal_label.setText(f"{self.updated_data2['drug_name']}")

        # print("drug_id: ",drug_id)
        
        # Check which meal_id is associated with the given drug_id
        self.cursor.execute('SELECT meal_id FROM Drug_handle WHERE drug_id = ?', (drug_id,))
        data = self.cursor.fetchall()

        # load ค่าจากฐานข้อมูลมาแสดงค่าใน Checkbox
        for meal_id in data:
            # print(meal_id)
            if meal_id == (1,):
                self.bb_checkBox.setChecked(True)

            elif meal_id == (2,):
                self.ab_checkBox.setChecked(True)
                
            elif meal_id == (3,):
                self.bl_checkBox.setChecked(True)
               
            elif meal_id == (4,):
                self.al_checkBox.setChecked(True)
               
            elif meal_id == (5,):
                self.bd_checkBox.setChecked(True)
               
            elif meal_id == (6,):
                self.ad_checkBox.setChecked(True)
               
            elif meal_id == (7,):
                self.bbed_checkBox.setChecked(True)


        # Print or use the associated meal_ids as needed
        # print("Associated meal_ids:", associated_meal_ids)

    def save_checkbox_states_and_close(self):
        self.save_checkbox_states()
                
    def save_checkbox_states(self):
        checkbox_states = {
            "bb_checkBox": self.bb_checkBox.isChecked(),
            "ab_checkBox": self.ab_checkBox.isChecked(),
            "bl_checkBox": self.bl_checkBox.isChecked(),
            "al_checkBox": self.al_checkBox.isChecked(),
            "bd_checkBox": self.bd_checkBox.isChecked(),
            "ad_checkBox": self.ad_checkBox.isChecked(),
            "bbed_checkBox": self.bbed_checkBox.isChecked()
        }

        # Iterate through checkbox states
        for checkbox_name, state in checkbox_states.items():
            # print(f"{checkbox_name}: {state}")

            # Determine meal_id based on checkbox_name
            meal_id = None
            if "bb_checkBox" in checkbox_name:
                meal_id = 1
            elif "ab_checkBox" in checkbox_name:
                meal_id = 2
            elif "bl_checkBox" in checkbox_name:
                meal_id = 3
            elif "al_checkBox" in checkbox_name:
                meal_id = 4
            elif "bd_checkBox" in checkbox_name:
                meal_id = 5
            elif "ad_checkBox" in checkbox_name:
                meal_id = 6
            elif "bbed_checkBox" in checkbox_name:
                meal_id = 7

            # Check if the record already exists
            self.cursor.execute('''
                SELECT * FROM Drug_handle
                WHERE drug_id = ? AND meal_id = ?
            ''', (self.drug_id, meal_id))

            existing_data = self.cursor.fetchone()

            if state:
                # Insert the record if it doesn't exist
                if not existing_data:
                    self.cursor.execute('''
                        INSERT INTO Drug_handle (drug_id, meal_id)
                        VALUES (?, ?)
                    ''', (self.drug_id, meal_id))
                    # print(f"Inserted: drug_id={self.drug_id}, meal_id={meal_id}")
                else:
                    pass
            else:
                # Delete the record if it exists
                if existing_data:
                    self.cursor.execute('''
                        DELETE FROM Drug_handle
                        WHERE drug_id = ? AND meal_id = ?
                    ''', (self.drug_id, meal_id))
                    # print(f"Deleted: drug_id={self.drug_id}, meal_id={meal_id}")
                else:
                    # print(f"Skipped: Record doesn't exist - drug_id={self.drug_id}, meal_id={meal_id}")
                    pass

        self.conn.commit()
    
    def retranslateUi(self, select_meal):
        _translate = QtCore.QCoreApplication.translate
        select_meal.setWindowTitle(_translate("select_meal", "เลือกมื้อ"))
        self.meal_label.setText(_translate("select_meal", "    เลือกมื้อยาที่ต้องการ"))
        self.back_pushButton.setText(_translate("select_meal", "ย้อนกลับ"))
        self.label_2.setText(_translate("select_meal", "เลือกมื้อที่ต้องการรับประทานยา"))
        self.bb_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.b_label.setText(_translate("select_meal", "มื้อเช้า"))
        self.ab_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.bl_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.al_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.l_label.setText(_translate("select_meal", "มื้อเที่ยง"))
        self.bd_label.setText(_translate("select_meal", "ก่อน อาหาร"))
        self.ad_label.setText(_translate("select_meal", "หลัง อาหาร"))
        self.d_label.setText(_translate("select_meal", "มื้อเย็น"))
        self.bed_label.setText(_translate("select_meal", "มื้อก่อนนอน"))
        self.bbed_label.setText(_translate("select_meal", "ก่อนนอน"))
        self.next_pushButton.setText(_translate("select_meal", "ถัดไป"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_meal = QtWidgets.QMainWindow()
    ui = Ui_select_meal()
    ui.setupUi(select_meal)
    select_meal.show()
    sys.exit(app.exec_())