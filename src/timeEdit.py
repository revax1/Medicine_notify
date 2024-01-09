from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_time_Edit(object):
    def __init__(self):
        self.meal_label_text = meal_label_instance.Get()
        self.connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")

    def convert_thai_to_arabic(self, thai_numeral):
        thai_to_arabic_mapping = {
            '๐': '0',
            '๑': '1',
            '๒': '2',
            '๓': '3',
            '๔': '4',
            '๕': '5',
            '๖': '6',
            '๗': '7',
            '๘': '8',
            '๙': '9'
        }

        arabic_numeral = ''.join(thai_to_arabic_mapping.get(char, char) for char in thai_numeral)
        return arabic_numeral


        
    def setupUi(self, time_Edit):
        UI_instance.Set(time_Edit)
        show_widget_fullscreen(time_Edit)

        time_Edit.setObjectName("time_Edit")
        time_Edit.resize(int(683 * width), int(400 * height))
        time_Edit.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(time_Edit)
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
        self.frame_2.setGeometry(QtCore.QRect(int(220 * width), int(100 * height), int(241 * width), int(231 * height)))  
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
        self.frame_3.setGeometry(QtCore.QRect(int(20 * width), int(10 * height), int(201 * width), int(141 * height)))  
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_3.setGraphicsEffect(shadow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.timeEdit_label = QtWidgets.QLabel(self.frame_3)
        self.timeEdit_label.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(181 * width), int(21 * height)))  
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.timeEdit_label.setFont(font)
        self.timeEdit_label.setObjectName("timeEdit_label")
        self.timeEdit_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.timeEdit_pushButton.setGeometry(QtCore.QRect(int(80 * width), int(180 * height), int(91 * width), int(31 * height)))  
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        self.timeEdit_pushButton.setFont(font)
        self.timeEdit_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.timeEdit_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.timeEdit_pushButton.setGraphicsEffect(shadow)
        self.timeEdit_pushButton.setObjectName("timeEdit_pushButton")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(int(250 * width), int(160 * height), int(181 * width), int(51 * height)))  
        self.timeEdit.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit.setObjectName("timeEdit")

        self.img_b_label = QtWidgets.QLabel(self.centralwidget)
        self.img_b_label.setGeometry(QtCore.QRect(int(232 * width), int(20 * height), int(42 * width), int(31 * height)))  
        self.img_b_label.setText("")
        self.img_b_label.setPixmap(QtGui.QPixmap(":/icons/b_label.png"))
        self.img_b_label.setScaledContents(True)
        self.img_b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_b_label.setObjectName("img_b_label")

        self.img_l_label = QtWidgets.QLabel(self.centralwidget)
        self.img_l_label.setGeometry(QtCore.QRect(int(232 * width), int(20 * height), int(35 * width), int(31 * height)))  
        self.img_l_label.setText("")
        self.img_l_label.setPixmap(QtGui.QPixmap(":/icons/l_label.png"))
        self.img_l_label.setScaledContents(True)
        self.img_l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_l_label.setObjectName("img_l_label")

        self.img_d_label = QtWidgets.QLabel(self.centralwidget)
        self.img_d_label.setGeometry(QtCore.QRect(int(240 * width), int(20 * height), int(33 * width), int(31 * height)))  
        self.img_d_label.setText("")
        self.img_d_label.setPixmap(QtGui.QPixmap(":/icons/d_label.png"))
        self.img_d_label.setScaledContents(True)
        self.img_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_d_label.setObjectName("img_d_label")

        self.img_bed_label = QtWidgets.QLabel(self.centralwidget)
        self.img_bed_label.setGeometry(QtCore.QRect(int(253 * width), int(20 * height), int(42 * width), int(31 * height)))  
        self.img_bed_label.setText("")
        self.img_bed_label.setPixmap(QtGui.QPixmap(":/icons/bed_label.png"))
        self.img_bed_label.setScaledContents(True)
        self.img_bed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_bed_label.setObjectName("img_bed_label")

        time_Edit.setCentralWidget(self.centralwidget)

        self.retranslateUi(time_Edit)
        QtCore.QMetaObject.connectSlotsByName(time_Edit)

        self.label.setText(f"      {self.meal_label_text}")


        self.add_back_pushButton.clicked.connect(self.backpage)

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT time FROM Meal WHERE meal_name = ?", (self.meal_label_text,))
            result = cursor.fetchone()
            print(result)

            if result:
                stored_time_thai = result[0]
                stored_time_arabic = self.convert_thai_to_arabic(stored_time_thai)
                stored_qtime = QtCore.QTime.fromString(stored_time_arabic, "HH:mm")
                self.timeEdit.setTime(stored_qtime)

                # Hide all meal images
                self.img_b_label.hide()
                self.img_l_label.hide()
                self.img_d_label.hide()
                self.img_bed_label.hide()

                # Show the image for the current meal
                if self.meal_label_text == "มื้อเช้า ก่อนอาหาร":
                    self.img_b_label.show()
                elif self.meal_label_text == "มื้อเช้า หลังอาหาร":
                    self.img_b_label.show()
                elif self.meal_label_text == "มื้อเที่ยง ก่อนอาหาร":
                    self.img_l_label.show()
                elif self.meal_label_text == "มื้อเที่ยง หลังอาหาร":
                    self.img_l_label.show()
                elif self.meal_label_text == "มื้อเย็น ก่อนอาหาร":
                    self.img_d_label.show()
                elif self.meal_label_text == "มื้อเย็น หลังอาหาร":
                    self.img_d_label.show()
                elif self.meal_label_text == "มื้อก่อนนอน":
                    self.img_bed_label.show()

        except Exception as e:
            QtWidgets.QMessageBox.critical(time_Edit, "Error", f"เกิดข้อผิดพลาดในการดึงข้อมูล: {str(e)}")

        def save_time():
            selected_time = self.timeEdit.time().toString("HH:mm")
            print(selected_time)
            meal_name = self.meal_label_text

            try:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE Meal SET time = ? WHERE meal_name = ?", (selected_time, meal_name))
                self.connection.commit()
               # Create a QMessageBox
                msg = QMessageBox()

                # Set the palette to control the background color
                palette = QtGui.QPalette()
                palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))  # Set your desired background color
                msg.setPalette(palette)

                # Set the text color
                msg.setStyleSheet("color: rgb(0, 0, 0);")

                # Show the QMessageBox
                msg.information(time_Edit, "Success", "เวลาถูกบันทึกเรียบร้อยแล้ว")

                

                # Retrieve the updated time from the database
                cursor.execute("SELECT time FROM Meal WHERE meal_name = ?", (meal_name,))
                result = cursor.fetchone()

                if result:
                    stored_time_thai = result[0]
                    stored_time_arabic = self.convert_thai_to_arabic(stored_time_thai)
                    stored_qtime = QtCore.QTime.fromString(stored_time_arabic, "HH:mm")
                    self.timeEdit.setTime(stored_qtime)
                    print(f"Updated time in QTimeEdit: {stored_time_arabic}")
                self.backpage()

            except Exception as e:
                QtWidgets.QMessageBox.critical(time_Edit, "Error", f"เกิดข้อผิดพลาด: {str(e)}")



        self.timeEdit_pushButton.clicked.connect(save_time)
        
        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.timeEdit_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.timeEdit_pushButton))
        self.timeEdit_pushButton.released.connect(lambda: self.set_button_released_style(self.timeEdit_pushButton))

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

    def backpage(self):
        from select_time import Ui_select_time
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_select_time)
        

    def retranslateUi(self, time_Edit):
        _translate = QtCore.QCoreApplication.translate
        time_Edit.setWindowTitle(_translate("time_Edit", "ตั้งเวลา"))
        self.add_back_pushButton.setText(_translate("time_Edit", "ย้อนกลับ"))
        self.label.setText(_translate("time_Edit", "มื้อเช้า ก่อนอาหาร"))
        self.timeEdit_label.setText(_translate("time_Edit", "เลือกเวลาที่ต้องการ"))
        self.timeEdit_pushButton.setText(_translate("time_Edit", "ยืนยัน"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    time_Edit = QtWidgets.QMainWindow()

    locale = QtCore.QLocale(QtCore.QLocale.English)
    QtCore.QLocale.setDefault(locale)
    
    ui = Ui_time_Edit()
    ui.setupUi(time_Edit)
    time_Edit.show()
    sys.exit(app.exec_())
