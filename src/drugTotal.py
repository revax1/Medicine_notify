from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_drugTotal(object):
    def setupUi(self, drugTotal):
        UI_instance.Set(drugTotal)
        show_widget_fullscreen(drugTotal)

        drugTotal.setObjectName("drugTotal")
        drugTotal.resize(int(683 * width), int(400 * height))
        drugTotal.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(drugTotal)
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
        self.img_label.setGeometry(QtCore.QRect(int(238 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/drugleft_icon.png"))
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
        self.frame_2.setGeometry(QtCore.QRect(int(90 * width), int(90 * height), int(512 * width), int(261 * height)))
        self.frame_2.setStyleSheet("border-radius: 9px;\n"
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
        drugTotal.setCentralWidget(self.centralwidget)

        self.retranslateUi(drugTotal)
        QtCore.QMetaObject.connectSlotsByName(drugTotal)
            
        self.add_back_pushButton.clicked.connect(self.homepage)

        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(int(107 * width), int(105 * height), (int(450 * width) + 30), int(230 * height)))
        # font = QtGui.QFont()
        # font.setPointSize(int(11 * height))
        # font.setBold(True)
        # font.setWeight(50)
        # self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")


        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ชื่อยา", "จำนวนยาคงเหลือในเครื่อง", "จำนวนยาคงเหลือนอกเครื่อง"])

        # Set the width of the columns
        self.tableWidget.setColumnWidth(0, int(150 * width))  # Adjust the width as needed
        self.tableWidget.setColumnWidth(1, int(150 * width))  # Adjust the width as needed
        self.tableWidget.setColumnWidth(2, int(150 * width))  # Adjust the width as needed

         # Set the background color of the table to white and text color to black
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(7)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.load_drug_data()

    def load_drug_data(self):
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT drug_name, external_drug, internal_drug, drug_eat FROM Drug 
        ''')

        # Fetch all rows from the result set
        drug_data = cursor.fetchall()

        # Set the number of rows in the table equal to the number of records
        self.tableWidget.setRowCount(len(drug_data))

        # Populate the table with the retrieved data
        for row_num, row_data in enumerate(drug_data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem()

                # If calculating for external_drug or internal_drug columns, apply the formula
                if col_num == 1 or col_num == 2:
                    drug_eat = row_data[3]  #  ตรงกับตำแหน่งที่สี่ คือ drug_eat

                    # Check for None values before performing multiplication
                    if col_data is not None and drug_eat is not None:
                        # Set the text with the desired format
                        item.setText(f"{col_data} มื้อ ({col_data * drug_eat} เม็ด)")
                    else:
                        item.setText("N/A")  # Or any default value you prefer
                else:
                    # For other columns, directly set the text
                    item.setText(str(col_data))

                self.tableWidget.setItem(row_num, col_num, item)

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

    def homepage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def retranslateUi(self, drugTotal):
        _translate = QtCore.QCoreApplication.translate
        drugTotal.setWindowTitle(_translate("drugTotal", "จำนวนยาคงเหลือ"))
        self.add_back_pushButton.setText(_translate("drugTotal", "ย้อนกลับ"))
        self.label.setText(_translate("drugTotal", "           จำนวนยาคงเหลือ   "))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drugTotal = QtWidgets.QMainWindow()
    ui = Ui_drugTotal()
    ui.setupUi(drugTotal)
    drugTotal.show()
    sys.exit(app.exec_())