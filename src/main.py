from __future__ import division

from Utils import *
from UI_Generate import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer, QLocale

import sys
import time
import RPi.GPIO as GPIO

from datetime import datetime
import os
import Adafruit_PCA9685
import subprocess
import threading
# from playsound import playsound
import requests
import pygame

from drug_List import Ui_drug_List
from select_time import Ui_select_time
# from pack_med import Ui_med_pack
from pack import Ui_med_pack
from sortDrug import Ui_sortDrug
from drugTotal import Ui_drugTotal
from wifi import Ui_wifi
from module import SensorThread

import sqlite3

# subprocess.run(["/home/pi/Documents/Medicine_notify/src/permission.sh"])

######################### initial ######################\
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

# Connect to SQLite database
connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")
cursor = connection.cursor()

# Create Drug table
cursor.execute('''   
    CREATE TABLE IF NOT EXISTS Drug (
        "drug_id"	INTEGER,
        "drug_name"	TEXT,
        "drug_description"	TEXT,
        "drug_remaining"	REAL,
        "drug_remaining_meal"	INTEGER,
        "fraction"	REAL,
        "external_drug"	INTEGER,
        "internal_drug"	INTEGER,
        "drug_eat"	REAL,
        "all_drug_recieve"	INTEGER,
        "day_start"	INTEGER,
        "drug_log"	TEXT,
        "drug_new"  REAL,
        "drug_size" REAL,
        PRIMARY KEY("drug_id" AUTOINCREMENT))
''')

# Create Meal table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Meal (
        "meal_id"	INTEGER,
        "meal_name"	TEXT,
        "time"	TEXT,
        PRIMARY KEY("meal_id" AUTOINCREMENT)
    )
''')

# Create Drug_handle table 
##################### ใช้ระบุว่า ยาตัวนั้นกินมื้อไหนบ้าง ######################## 
# ทำตารางนี้มาเพื่อแทนที่ meal_state ซึ่งเป็นการเก็บ state โดยรวม
cursor.execute('''       
    CREATE TABLE IF NOT EXISTS Drug_handle (
        "handle_id"	INTEGER,
        "drug_id"	INTEGER,
        "meal_id"	INTEGER,
        FOREIGN KEY("meal_id") REFERENCES "Meal"("meal_id"),
        FOREIGN KEY("drug_id") REFERENCES "Drug"("drug_id"),
        PRIMARY KEY("handle_id" AUTOINCREMENT)
    )
''')

connection.commit()      
################################################################

class Ui_Medicine_App(object):
    def setupUi(self, Medicine_App):
        drug_list_instance.Set(None)
        drug_name_instance.Set(None)
        drug_ID_instance.Set(None)
        each_drug_instance.Set(None)
        each_drug_2_instance.Set(None)
        drug_Update_instance.Set(None)
        drug_Update_2_instance.Set(None)
        day_start_instance.Set(None)
        select_meal_instance.Set(None)
        data_checkui1_instance.Set(None)
        data_checkui2_instance.Set(None)
        data_checkui3_instance.Set(None)
        meal_label_instance.Set(None)
        wifi_name_instance.Set(None)

        UI_instance.Set(Medicine_App)
        show_widget_fullscreen(Medicine_App)

        Medicine_App.setObjectName("Medicine_App")
        Medicine_App.resize(int(683 * width), int(400 * height))
        Medicine_App.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(Medicine_App)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);\n" )
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.home_label = QtWidgets.QLabel(self.frame)
        self.home_label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.home_label.setFont(font)
        self.home_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.home_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.home_label.setGraphicsEffect(shadow)
        self.home_label.setFrameShape(QtWidgets.QFrame.Box)
        self.home_label.setLineWidth(int(1 * width))
        self.home_label.setTextFormat(QtCore.Qt.AutoText)
        self.home_label.setScaledContents(False)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setWordWrap(True)
        self.home_label.setObjectName("home_label")
        self.img_home_label = QtWidgets.QLabel(self.frame)
        self.img_home_label.setGeometry(QtCore.QRect(int(277 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_home_label.setText("")
        self.img_home_label.setPixmap(QtGui.QPixmap(":/icons/home2_icon.png"))
        self.img_home_label.setScaledContents(True)
        self.img_home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_home_label.setObjectName("img_home_label")
        
        self.wifi_pushButton = QtWidgets.QPushButton(self.frame)
        self.wifi_pushButton.setGeometry(QtCore.QRect(int(590 * width), int(76 * height), int(41 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.wifi_pushButton.setFont(font)
        self.wifi_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        
        self.img_wifi_label = QtWidgets.QLabel(self.wifi_pushButton)
        self.img_wifi_label.setGeometry(QtCore.QRect(int(5 * width), int(8 * height), int(31 * width), int(23 * height)))
        self.img_wifi_label.setText("")
        self.img_wifi_label.setPixmap(QtGui.QPixmap(":/icons/wifi_icon.png"))
        self.img_wifi_label.setScaledContents(True)
        self.img_wifi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_wifi_label.setObjectName("img_wifi_label")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(int(50 * width), int(97 * height), int(100 * width), int(16 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(8 * height))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(int(43 * width), int(77 * height), int(71 * width), int(16 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(8 * height))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(205 * width), int(90 * height), int(271 * width), int(281 * height)))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);\n")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDrug_pushButton.setGeometry(QtCore.QRect(int(225 * width), int(110 * height), int(231 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.addDrug_pushButton.setFont(font)
        self.addDrug_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.addDrug_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.addDrug_pushButton.setGraphicsEffect(shadow)

        # icon = QtGui.QIcon()                                                                      ไม่ได้ลบไอคอนแบบเก่าแค่คอมเม้นไว้
        # icon.addPixmap(QtGui.QPixmap(":/icons/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_druglist_label = QtWidgets.QLabel(self.centralwidget)
        self.img_druglist_label.setGeometry(QtCore.QRect(int(292 * width), int(119 * height), int(25 * width), int(24 * height)))
        self.img_druglist_label.setText("")
        self.img_druglist_label.setPixmap(QtGui.QPixmap(":/icons/druglist_tab.png"))
        self.img_druglist_label.setScaledContents(True)
        self.img_druglist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_druglist_label.setObjectName("img_druglist_label")

        # self.addDrug_pushButton.setIcon(icon)
        # self.addDrug_pushButton.setIconSize(QtCore.QSize(20, 40))
        # self.addDrug_pushButton.setAutoDefault(False)
        # self.addDrug_pushButton.setDefault(False)
        # self.addDrug_pushButton.setFlat(False)
        self.addDrug_pushButton.setObjectName("addDrug_pushButton")
        self.setting_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setting_pushButton.setGeometry(QtCore.QRect(int(225 * width), int(160 * height), int(231 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.setting_pushButton.setFont(font)
        self.setting_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.setting_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.setting_pushButton.setGraphicsEffect(shadow)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/icons/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_selecttime_label = QtWidgets.QLabel(self.centralwidget)
        self.img_selecttime_label.setGeometry(QtCore.QRect(int(275 * width), int(169 * height), int(26 * width), int(24 * height)))
        self.img_selecttime_label.setText("")
        self.img_selecttime_label.setPixmap(QtGui.QPixmap(":/icons/selecttime_tab.png"))
        self.img_selecttime_label.setScaledContents(True)
        self.img_selecttime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_selecttime_label.setObjectName("img_selecttime_label")

        # self.setting_pushButton.setIcon(icon1)
        # self.setting_pushButton.setIconSize(QtCore.QSize(20, 40))
        # self.setting_pushButton.setAutoDefault(False)
        # self.setting_pushButton.setDefault(False)
        # self.setting_pushButton.setFlat(False)
        self.setting_pushButton.setObjectName("setting_pushButton")
        self.putDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.putDrug_pushButton.setGeometry(QtCore.QRect(int(225 * width), int(210 * height), int(231 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.putDrug_pushButton.setFont(font)
        self.putDrug_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.putDrug_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.putDrug_pushButton.setGraphicsEffect(shadow)
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_pack_label = QtWidgets.QLabel(self.centralwidget)
        self.img_pack_label.setGeometry(QtCore.QRect(int(260 * width), int(219 * height), int(25 * width), int(24 * height)))
        self.img_pack_label.setText("")
        self.img_pack_label.setPixmap(QtGui.QPixmap(":/icons/pack_tab.png"))
        self.img_pack_label.setScaledContents(True)
        self.img_pack_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_pack_label.setObjectName("img_pack_label")

        # self.putDrug_pushButton.setIcon(icon2)
        # self.putDrug_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.putDrug_pushButton.setAutoDefault(False)
        # self.putDrug_pushButton.setDefault(False)
        # self.putDrug_pushButton.setFlat(False)
        self.putDrug_pushButton.setObjectName("putDrug_pushButton")
        self.alignment_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.alignment_pushButton.setGeometry(QtCore.QRect(int(225 * width), int(260 * height), int(231 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.alignment_pushButton.setFont(font)
        self.alignment_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.alignment_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.alignment_pushButton.setGraphicsEffect(shadow)
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap(":/icons/Industry-Rack-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_sort_label = QtWidgets.QLabel(self.centralwidget)
        self.img_sort_label.setGeometry(QtCore.QRect(int(252 * width), int(269 * height), int(27 * width), int(24 * height)))
        self.img_sort_label.setText("")
        self.img_sort_label.setPixmap(QtGui.QPixmap(":/icons/sort_tab.png"))
        self.img_sort_label.setScaledContents(True)
        self.img_sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_sort_label.setObjectName("img_sort_label")

        # self.alignment_pushButton.setIcon(icon3)
        # self.alignment_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.alignment_pushButton.setAutoDefault(False)
        # self.alignment_pushButton.setDefault(False)
        # self.alignment_pushButton.setFlat(False)
        self.alignment_pushButton.setObjectName("alignment_pushButton")
        self.drugLeft_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.drugLeft_pushButton.setGeometry(QtCore.QRect(int(225 * width), int(310 * height), int(231 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.drugLeft_pushButton.setFont(font)
        self.drugLeft_pushButton.setStyleSheet("border-radius: 9px;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.drugLeft_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.drugLeft_pushButton.setGraphicsEffect(shadow)
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap(":/icons/table_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.img_drugleft_label = QtWidgets.QLabel(self.centralwidget)
        self.img_drugleft_label.setGeometry(QtCore.QRect(int(255 * width), int(318 * height), int(27 * width), int(24 * height)))
        self.img_drugleft_label.setText("")
        self.img_drugleft_label.setPixmap(QtGui.QPixmap(":/icons/drugleft_tab.png"))
        self.img_drugleft_label.setScaledContents(True)
        self.img_drugleft_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_drugleft_label.setObjectName("img_drugleft_label")

        # self.drugLeft_pushButton.setIcon(icon4)
        # self.drugLeft_pushButton.setIconSize(QtCore.QSize(20, 50))
        # self.drugLeft_pushButton.setAutoDefault(False)
        # self.drugLeft_pushButton.setDefault(False)
        # self.drugLeft_pushButton.setFlat(False)
        self.drugLeft_pushButton.setObjectName("drugLeft_pushButton")
        Medicine_App.setCentralWidget(self.centralwidget)

        self.retranslateUi(Medicine_App)
        QtCore.QMetaObject.connectSlotsByName(Medicine_App)
        
        # อัพเดทเวลา
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        # Connect to SQLite database
        self.connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")
        self.cursor = self.connection.cursor()
        
        # Check if the Meal table is empty, and if so, insert default values
        self.cursor.execute("SELECT COUNT(*) FROM Meal")
        meal_count = self.cursor.fetchone()[0]
        
        ############################### ปลื้มแก้ ######################################    
        if meal_count == 0:
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเช้า ก่อนอาหาร", "06:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเช้า หลังอาหาร", "06:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเที่ยง ก่อนอาหาร", "12:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเที่ยง หลังอาหาร", "12:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเย็น ก่อนอาหาร", "18:00"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อเย็น หลังอาหาร", "18:30"))
            self.cursor.execute("INSERT INTO Meal (meal_name, time) VALUES (?, ?)",
                                ("มื้อก่อนนอน", "20:30"))

        self.connection.commit()
        
        self.addDrug_pushButton.clicked.connect(self.open_drug_List_page)
        self.setting_pushButton.clicked.connect(self.open_select_time_page)
        self.putDrug_pushButton.clicked.connect(self.open_pack_page)
        self.alignment_pushButton.clicked.connect(self.open_sortdrug_page)
        self.drugLeft_pushButton.clicked.connect(self.open_drugTotal_page)
        self.wifi_pushButton.clicked.connect(self.open_wifi_page)

        # Set up button press and release styling
        self.addDrug_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.addDrug_pushButton))
        self.addDrug_pushButton.released.connect(lambda: self.set_button_released_style(self.addDrug_pushButton))

        self.setting_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.setting_pushButton))
        self.setting_pushButton.released.connect(lambda: self.set_button_released_style(self.setting_pushButton))

        self.putDrug_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.putDrug_pushButton))
        self.putDrug_pushButton.released.connect(lambda: self.set_button_released_style(self.putDrug_pushButton))

        self.alignment_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.alignment_pushButton))
        self.alignment_pushButton.released.connect(lambda: self.set_button_released_style(self.alignment_pushButton))

        self.drugLeft_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.drugLeft_pushButton))
        self.drugLeft_pushButton.released.connect(lambda: self.set_button_released_style(self.drugLeft_pushButton))

        self.wifi_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.wifi_pushButton))
        self.wifi_pushButton.released.connect(lambda: self.set_button_released_style(self.wifi_pushButton))
        
        
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
            "background-color: rgb(255, 255, 255);"
        )
        
    ###################### เวลา #############################
    def update_time(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_date = current_datetime.strftime("%a, %d %b %Y")
        
        self.label.setText(current_time)
        self.label_3.setText(current_date)

    ###################### หน้าคลังยา #############################  
    def open_drug_List_page(self):
        drug_List_form = UI_Genarate()
        drug_List_form.widgetSet(UI_instance.Get(), Ui_drug_List)
        self.timer.stop()

    ###################### หน้าตั้งเวลามื้อยา ############################# 
    def open_select_time_page(self):
        select_time_form = UI_Genarate()
        select_time_form.widgetSet(UI_instance.Get(), Ui_select_time)
        self.timer.stop()
        
    # ###################### หน้าวิธีบรรจุยา #############################                                            อันเก่า
    # def open_pack_page(self):
    #     self.pack_window = QtWidgets.QMainWindow()
    #     self.ui_pack = Ui_med_pack()
    #     self.ui_pack.setupUi(self.pack_window)
    #     self.pack_window.show()
        
    #     def close_pack_window():
    #         self.pack_window.close()
            
    #     self.ui_pack.pack_back_pushButton.clicked.connect(close_pack_window)
        
        ##################### หน้าคำแนะนำการใส่ยา ############################# 
    def open_pack_page(self):
        pack_form = UI_Genarate()
        pack_form.widgetSet(UI_instance.Get(), Ui_med_pack)
        self.timer.stop()

    ###################### หน้าวิธีจัดเรียงยาตามผัง ############################# 
    def open_sortdrug_page(self):
        sortdrug_form = UI_Genarate()
        sortdrug_form.widgetSet(UI_instance.Get(), Ui_sortDrug)
        self.timer.stop()
    
    ##################### หน้าจำนวนมื้อยาคงเหลือ ############################# 
    def open_drugTotal_page(self):
        drugTotal_form = UI_Genarate()
        drugTotal_form.widgetSet(UI_instance.Get(), Ui_drugTotal)
        self.timer.stop()


    ##################### หน้าwifi ############################# 
    def open_wifi_page(self):
        wifi_form = UI_Genarate()
        wifi_form.widgetSet(UI_instance.Get(), Ui_wifi)
        self.timer.stop()


    def retranslateUi(self, Medicine_App):
        _translate = QtCore.QCoreApplication.translate
        Medicine_App.setWindowTitle(_translate("Medicine_App", "หน้าหลัก"))
        self.addDrug_pushButton.setText(_translate("Medicine_App", "  คลังยา"))
        self.home_label.setText(_translate("Medicine_App", "     หน้าหลัก"))
        self.setting_pushButton.setText(_translate("Medicine_App", "  ตั้งเวลามื้อยา"))
        self.putDrug_pushButton.setText(_translate("Medicine_App", "  คำแนะนำการใส่ยา"))
        self.alignment_pushButton.setText(_translate("Medicine_App", "  วิธีเรียงกล่องบรรจุยา"))
        self.drugLeft_pushButton.setText(_translate("Medicine_App", "  จำนวนยาคงเหลือ"))
        self.wifi_pushButton.setText(_translate("Medicine_App", ""))

    
        self.img_wifi_label.raise_()
        
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Medicine_App = QtWidgets.QMainWindow()
    ui = Ui_Medicine_App()
    ui.setupUi(Medicine_App)
    # Set the locale to English
    english_locale = QLocale(QLocale.English)
    QLocale.setDefault(english_locale)
    Medicine_App.show()
    sensor_thread = SensorThread()
    sensor_thread.run_thread()

    sys.exit(app.exec_())