from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from encrypt_check import Ui_encrypt_check


class Ui_data_check3(object):
    def setupUi(self, data_check3):
        UI_instance.Set(data_check3)
        show_widget_fullscreen(data_check3)

        self.data_check3 = data_check3
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.each_drug2 = each_drug_2_instance.Get()
        self.day_start = day_start_instance.Get()
        self.select_meal = select_meal_instance.Get()
        self.data_check1 = data_checkui1_instance.Get()
        self.data_check2 = data_checkui2_instance.Get()
        self.updated_data2 = drug_Update_2_instance.Get()

        data_check3.setObjectName("data_check3")
        data_check3.resize(int(683 * width), int(400 * height))
        data_check3.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(data_check3)
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
        self.img_label.setGeometry(QtCore.QRect(int(225 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/check.png"))
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
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(int(50 * width), int(77 * height), int(250 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugName_label.setFont(font)
        self.drugName_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.drugName_label.setObjectName("drugName_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(int(510 * width), int(250 * height), int(81 * width), int(31 * height)))
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
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(100 * width), int(100 * height), int(231 * width), int(220 * height)))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_3.setGraphicsEffect(shadow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.drugDescribe_label_2 = QtWidgets.QLabel(self.frame_3)
        self.drugDescribe_label_2.setGeometry(QtCore.QRect(int(20 * width), int(20 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugDescribe_label_2.setFont(font)
        self.drugDescribe_label_2.setObjectName("drugDescribe_label_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(int(20 * width), int(50 * height), int(185 * width), int(150 * height)))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(int(12 * height))
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.listWidget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.listWidget.setGraphicsEffect(shadow)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(int(2 * width))
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setObjectName("listWidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(350 * width), int(100 * height), int(241 * width), int(120 * height)))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.day_start = QtWidgets.QLabel(self.frame_2)
        self.day_start.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.day_start.setFont(font)
        self.day_start.setObjectName("day_start")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_9)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_9.setGraphicsEffect(shadow)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setLineWidth(int(1 * width))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        data_check3.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_check3)
        self.set_data_info3(drug_ID_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(data_check3)

        self.add_back_pushButton.clicked.connect(self.backpage)
        self.next_pushButton.clicked.connect(lambda: self.open_encrypt_check())

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

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

    def backpage(self):
        # ทำการคำนวณค่า all_drug_recieve ใหม่
        drug_remaining = float(self.updated_data2['drug_remaining'])
        drug_eat = float(self.updated_data2['drug_eat'])
        self.updated_data2['drug_remaining_meal'] = str(drug_remaining * drug_eat)
        
        from data_checkui2 import Ui_data_check2
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_data_check2)

    def open_encrypt_check(self):
        drug_Update_2_instance.Set({'drug_id': self.drug_id, **self.updated_data2})
        data_checkui3_instance.Set(self)
        data_checkui2_instance.Set(self.data_check2)
        data_checkui1_instance.Set(self.data_check1)
        select_meal_instance.Set(self.select_meal)
        day_start_instance.Set(self.day_start)
        each_drug_2_instance.Set(self.each_drug2)
        each_drug_2_instance.Set(self.each_drug)
        drug_list_instance.Set(self.drug_List)

        encrypt_check_form = UI_Genarate()
        encrypt_check_form.widgetSet(UI_instance.Get(), Ui_encrypt_check)
    def set_data_info3(self, drug_id):
        self.drug_id = drug_id
        print(f"data_check3 {self.updated_data2}")
        self.drugName_label.setText(f"ชื่อยา: {self.updated_data2['drug_name']}")

        # Fetch meal data for the given drug_id from the database
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")
        cursor = connection.cursor()

        query = '''
            SELECT Meal.meal_name
            FROM Meal
            JOIN Drug_handle ON Meal.meal_id = Drug_handle.meal_id
            WHERE Drug_handle.drug_id = ?
        '''
        cursor.execute(query, (self.drug_id,))
        meal_data = cursor.fetchall()

        connection.close()
        
        # cursor.execute("SELECT * FROM Drug")
        # drugs = cursor.fetchall()
        # connection.close()
        # print(drugs)


        # Set the data in the labels and listWidget
        self.label_9.setText(f"{self.updated_data2['day_start']}")

         # Clear the listWidget before adding new items
        self.listWidget.clear()

        # # Add meal selection data to the listWidget
        # meal_data = self.updated_data2.get('meals', [])
        # print(f"Meal Data: {meal_data}")
        # self.listWidget.addItems(meal_data)

         # Add fetched meal data to the listWidget
        meal_names = [item[0] for item in meal_data]
        self.listWidget.addItems(meal_names)

    def retranslateUi(self, data_check3):
        _translate = QtCore.QCoreApplication.translate
        data_check3.setWindowTitle(_translate("data_check3", "ตรวจสอบความถูกต้อง"))
        self.label.setText(_translate("data_check3", "        ตรวจสอบความถูกต้อง  "))
        self.add_back_pushButton.setText(_translate("data_check3", "ย้อนกลับ"))
        self.drugName_label.setText(_translate("data_check3", "ชื่อยา:"))
        self.next_pushButton.setText(_translate("data_check3", "ถัดไป"))
        self.drugDescribe_label_2.setText(_translate("data_check3", "มื้อยาที่รับประทาน"))
        self.day_start.setText(_translate("data_check3", "วันแรกที่เริ่มรับประทานยา"))
        self.label_9.setText(_translate("data_check3", "วันที่"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_check3 = QtWidgets.QMainWindow()
    ui = Ui_data_check3()
    ui.setupUi(data_check3)
    data_check3.show()
    sys.exit(app.exec_())
