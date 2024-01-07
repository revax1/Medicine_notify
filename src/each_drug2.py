from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from day_start import Ui_day_start

class Ui_each_drug2(object):
    def setupUi(self, each_drug2):
        UI_instance.Set(each_drug2)
        show_widget_fullscreen(each_drug2)
        
        self.each_drug2 = each_drug2
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.updated_data = drug_Update_instance.Get()

        each_drug2.setObjectName("each_drug2")
        each_drug2.resize(int(683 * width), int(400 * height))
        each_drug2.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(each_drug2)
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
        font.setWeight(75)
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
        self.img_label.setGeometry(QtCore.QRect(int(238 * width), int(80 * height), int(31 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/each_icon.png"))
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
        self.frame_2.setGeometry(QtCore.QRect(int(100 * width), int(100 * height), int(231 * width), int(220 * height)))
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
        self.drugSize = QtWidgets.QLabel(self.frame_2)
        self.drugSize.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(191 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugSize.setFont(font)
        self.drugSize.setObjectName("drugSize")
        self.drugNew = QtWidgets.QLabel(self.frame_2)
        self.drugNew.setGeometry(QtCore.QRect(int(10 * width), int(110 * height), int(200 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugNew.setFont(font)
        self.drugNew.setObjectName("drugNew")
        self.size_label = QtWidgets.QTextEdit(self.frame_2)
        self.size_label.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.size_label.setFont(font)
        self.size_label.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.size_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.size_label.setGraphicsEffect(shadow)
        self.size_label.setFrameShape(QtWidgets.QFrame.Box)
        self.size_label.setLineWidth(int(1 * width))
        self.size_label.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.size_label.setObjectName("size_label")

        self.label_6 = QtWidgets.QTextEdit(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_6)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_6.setGraphicsEffect(shadow)

        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(int(1 * width))
        self.label_6.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_6.setObjectName("label_6")

        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(350 * width), int(100 * height), int(241 * width), int(220 * height)))
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
        self.drugStill = QtWidgets.QLabel(self.frame_3)
        self.drugStill.setGeometry(QtCore.QRect(int(-30 * width), int(20 * height), int(251 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugStill.setFont(font)
        self.drugStill.setAlignment(QtCore.Qt.AlignCenter)
        self.drugStill.setObjectName("drugStill")
        self.drugGot = QtWidgets.QLabel(self.frame_3)
        self.drugGot.setGeometry(QtCore.QRect(int(-20 * width), int(110 * height), int(261 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugGot.setFont(font)
        self.drugGot.setAlignment(QtCore.Qt.AlignCenter)
        self.drugGot.setObjectName("drugGot")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_7)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_7.setGraphicsEffect(shadow)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(int(1 * width))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_8)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_8.setGraphicsEffect(shadow)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(int(1 * width))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")

        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(int(510 * width), int(330 * height), int(81 * width), int(31 * height)))
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
        each_drug2.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(each_drug2)
        self.set_drug2_info(drug_ID_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(each_drug2)

        self.add_back_pushButton.clicked.connect(self.backpage)

        # self.next_pushButton.clicked.connect(self.open_day_start)

        def save_changes():
            # ตรวจสอบข้อมูลที่ถูกแก้ไขและบันทึกลงฐานข้อมูลหรือตัวแปรที่เหมาะสม
            updated_data2 = drug_Update_instance.Get()


            updated_data2['drug_size'] = self.size_label.toPlainText()
            updated_data2['drug_new'] = self.label_6.toPlainText()
            updated_data2['drug_remaining_meal'] = self.label_7.text()
            updated_data2['all_drug_recieve'] = self.label_8.text()
            
            
            # ทำการคำนวณค่า all_drug_recieve ใหม่
            all_drug_recieve = int(updated_data2['all_drug_recieve'])
            drug_new = int(updated_data2['drug_new'])
            updated_data2['all_drug_recieve'] = str(all_drug_recieve + drug_new)

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
            drug_Update_2_instance.Set(updated_data2)
            self.open_day_start()

        self.next_pushButton.clicked.connect(save_changes)

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
        from each_drug import Ui_each_drug
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_each_drug)

    def open_day_start(self):
        # print(f"each_drug2 ครั้งที่ 2 {drug_Update_2_instance.Get()}")
        drug_list_instance.Set(self.drug_List)
        each_drug_instance.Set(self.each_drug)
        each_drug_2_instance.Set(self.each_drug)

        day_start_form = UI_Genarate()
        day_start_form.widgetSet(UI_instance.Get(), Ui_day_start)

    def set_drug2_info(self, drug_id):
        # print(f"each_drug2 {self.updated_data}")
        self.drug_id = drug_id
        self.label.setText(f"{self.updated_data['drug_name']}")
        # print(drug_id)
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = connection.cursor()
        query = '''
            SELECT * FROM Drug WHERE drug_id = ?
            '''
        cursor.execute(query, (drug_id,))  
        drug_info = cursor.fetchone()

        if drug_info:
            # Convert the tuple to a list for modification
            drug_info_list = list(drug_info)

            drug_info_list[4] = drug_info_list[3] / drug_info_list[8]
            
            # ตั้งให้ drug_new มีค่าเริ่มต้นเป็น 0 แทน
            if drug_info_list[12] == None: 
                drug_info_list[12] = 0

            # Convert the list back to a tuple
            drug_info = tuple(drug_info_list)

            self.drug_id = drug_info[0]
            self.size_label.setText(f"{drug_info[13]}")
            self.label_6.setText(f"0")
            self.label_7.setText(f"{drug_info[4]}")
            self.label_8.setText(f"{drug_info[9]}")

    def retranslateUi(self, each_drug2):
        _translate = QtCore.QCoreApplication.translate
        each_drug2.setWindowTitle(_translate("each_drug2", "ยาแต่ละตัว"))
        self.label_6.setText(_translate("each_drug2", "ยาที่ได้รับมาใหม่"))
        self.next_pushButton.setText(_translate("each_drug2", "ถัดไป"))
        self.drugStill.setText(_translate("each_drug2", "จำนวนมื้อยาคงเหลือ (มื้อ)"))
        self.label.setText(_translate("each_drug2", "ชื่อยา"))
        self.size_label.setText(_translate("each_drug2", ""))
        self.drugSize.setText(_translate("each_drug2", "ขนาดเม็ดยา (มิลลิเมตร)"))
        self.drugNew.setText(_translate("each_drug2", "จำนวนยาที่ได้รับมาใหม่ (เม็ด)"))
        self.drugGot.setText(_translate("each_drug2", "จำนวนยาที่ได้รับมาแล้ว (เม็ด)"))
        self.add_back_pushButton.setText(_translate("each_drug2", "ย้อนกลับ"))
        self.label_7.setText(_translate("each_drug2", "ยาคงเหลือ"))
        # self.delete_pushButton.setText(_translate("each_drug2", "ลบ"))
        self.label_8.setText(_translate("each_drug2", "ยาที่ได้รับมาแล้ว"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    each_drug2 = QtWidgets.QMainWindow()
    ui = Ui_each_drug2()
    ui.setupUi(each_drug2)
    each_drug2.show()
    sys.exit(app.exec_())