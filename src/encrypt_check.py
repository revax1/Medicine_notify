from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import sqlite3
import string
import sys

class Ui_encrypt_check(object):
    def setupUi(self, encrypt_check):
        UI_instance.Set(encrypt_check)
        show_widget_fullscreen(encrypt_check)
        
        self.encrypt_check = encrypt_check
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.each_drug2 = each_drug_2_instance.Get()
        self.day_start = day_start_instance.Get()
        self.select_meal = select_meal_instance.Get()
        self.data_check1 = data_checkui1_instance.Get()
        self.data_check2 = data_checkui2_instance.Get()
        self.data_check3 = data_checkui3_instance.Get()
        self.updated_data2 = drug_Update_2_instance.Get()

        encrypt_check.setObjectName("encrypt_check")
        encrypt_check.resize(int(683 * width), int(400 * height))
        encrypt_check.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(encrypt_check)
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
        self.img_label.setGeometry(QtCore.QRect(int(255 * width), int(80 * height), int(31 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/encrypt.png"))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(200 * width), int(90 * height), int(291 * width), int(261 * height)))
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
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(int(10 * width), int(10 * height), int(271 * width), int(201 * height)))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.set_code_label = QtWidgets.QLabel(self.frame_3)
        self.set_code_label.setGeometry(QtCore.QRect(int(30 * width), int(10 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.set_code_label.setFont(font)
        self.set_code_label.setObjectName("set_code_label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(int(30 * width), int(40 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_2.setGraphicsEffect(shadow)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(int(1 * width))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QTextEdit(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(int(30 * width), int(130 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_3.setGraphicsEffect(shadow)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(int(1 * width))
        self.label_3.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_3.setObjectName("label_3")
        self.drugName_label_2 = QtWidgets.QLabel(self.frame_3)
        self.drugName_label_2.setGeometry(QtCore.QRect(int(30 * width), int(100 * height), int(211 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugName_label_2.setFont(font)
        self.drugName_label_2.setObjectName("drugName_label_2")
        self.next_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.next_pushButton.setGeometry(QtCore.QRect(int(100 * width), int(220 * height), int(91 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")
        encrypt_check.setCentralWidget(self.centralwidget)


        self.retranslateUi(encrypt_check)
        QtCore.QMetaObject.connectSlotsByName(encrypt_check)

        self.add_back_pushButton.clicked.connect(self.backpage)

        self.updated_data2 = drug_Update_2_instance.Get()

        # Generate a random code with both numbers and letters
        characters = string.ascii_letters + string.digits
        self.generated_code = ''.join(random.choice(characters) for _ in range(6))
        self.label_2.setText(f"{self.generated_code}")

        def check_code():
            # Get the user-entered code
            user_code = self.label_3.toPlainText().strip()

            # Check if the user-entered code matches the generated code
            if user_code == self.generated_code:
                # Code is correct, update the database with the received data
                connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
                cursor = connection.cursor()

                update_query = '''
                    UPDATE Drug
                    SET drug_name = ?,
                        drug_description = ?,
                        drug_remaining = ?,
                        drug_eat = ?,
                        drug_new = ?,
                        all_drug_recieve = ?,
                        day_start = ?,
                        drug_size = ?
                    WHERE drug_id = ?
                '''
                cursor.execute(update_query, (
                    self.updated_data2['drug_name'],
                    self.updated_data2['drug_description'],
                    self.updated_data2['drug_remaining'],
                    self.updated_data2['drug_eat'],
                    self.updated_data2['drug_new'],
                    self.updated_data2['all_drug_recieve'],
                    self.updated_data2['day_start'],
                    self.updated_data2['drug_size'],
                    self.updated_data2['drug_id']
                ))

                

                connection.commit()
                QtWidgets.QMessageBox.information(encrypt_check, "Success", "ข้อมูลถูกบันทึกเรียบร้อยแล้ว")
                # QtWidgets.QMessageBox.information.setStyleSheet("background-color: rgb(255, 255, 255);")
                from drug_List import Ui_drug_List
                homepage_form = UI_Genarate()
                homepage_form.widgetSet(UI_instance.Get(), Ui_drug_List)
                connection.close()
                
                
            else:
                # Code is incorrect, prompt the user to enter the correct code
                QMessageBox.warning(self.centralwidget, "รหัสไม่ถูกต้อง", "กรุณากรอกรหัสให้ถูกต้อง")

        self.next_pushButton.clicked.connect(check_code)

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
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 170, 127);"
        )

    # def closeAll(self):
    #     self.each_drug.closeAll()
    #     self.each_drug2.closeAll()
    #     self.day_start.closeAll() 
    #     self.select_meal.closeAll()
    #     self.data_check.closeAll()
    #     self.encrypt_check.close()

    def backpage(self):
        from data_checkui3 import Ui_data_check3
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_data_check3)

    def retranslateUi(self, encrypt_check):
        _translate = QtCore.QCoreApplication.translate
        encrypt_check.setWindowTitle(_translate("encrypt_check", "ยืนยันการแก้ไข"))
        self.label_2.setText(_translate("encrypt_check", "รหัสที่กำหนด"))
        self.add_back_pushButton.setText(_translate("encrypt_check", "ย้อนกลับ"))
        self.label.setText(_translate("encrypt_check", "       ยืนยันการแก้ไข"))
        self.set_code_label.setText(_translate("encrypt_check", "รหัสตรวจสอบ"))
        self.label_3.setText(_translate("encrypt_check", ""))
        self.drugName_label_2.setText(_translate("encrypt_check", "กรุณากรอกรหัส"))
        self.next_pushButton.setText(_translate("encrypt_check", "ยืนยัน"))

import resources_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    encrypt_check = QtWidgets.QMainWindow()
    ui = Ui_encrypt_check()
    ui.setupUi(encrypt_check)
    encrypt_check.show()
    sys.exit(app.exec_())
