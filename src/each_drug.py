from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from each_drug2 import Ui_each_drug2

class CustomMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(CustomMessageBox, self).__init__(parent)
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
                border: 2px solid black;
            }
            QLabel {
                color: black;
            }
        """)

class Ui_each_drug(object):   
    def setupUi(self, each_drug):
        UI_instance.Set(each_drug)
        show_widget_fullscreen(each_drug)
        
        self.prepare_state_file = '/home/pi/Documents/Medicine_notify/state/prepare_state.txt'
        
        self.each_drug = each_drug
        self.drug_List = drug_list_instance.Get()
        
        each_drug.setObjectName("each_drug")
        each_drug.resize(int(683 * width), int(400 * height))
        each_drug.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(each_drug)
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
        self.delete_pushButton = QtWidgets.QPushButton(self.frame)
        self.delete_pushButton.setGeometry(QtCore.QRect(int(550 * width), int(80 * height), int(41 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(171, 57, 57);\n"
"color: rgb(255, 255, 255);\n"
"")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.delete_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.delete_pushButton.setGraphicsEffect(shadow)
        self.delete_pushButton.setObjectName("delete_pushButton")
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
        self.drugName_label = QtWidgets.QLabel(self.frame_2)
        self.drugName_label.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(101 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.drugDescribe_label = QtWidgets.QLabel(self.frame_2)
        self.drugDescribe_label.setGeometry(QtCore.QRect(int(10 * width), int(110 * height), int(131 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")

        self.label_2 = QtWidgets.QTextEdit(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(211 * width), int(41 * height)))
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
        self.label_2.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QTextEdit(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(211 * width), int(41 * height)))
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

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(int(350 * width), int(100 * height), int(241 * width), int(220 * height)))
        self.frame_3.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_3.setGraphicsEffect(shadow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.drugAll_label = QtWidgets.QLabel(self.frame_3)
        self.drugAll_label.setGeometry(QtCore.QRect(int(-30 * width), int(20 * height), int(251 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.drugOne_label = QtWidgets.QLabel(self.frame_3)
        self.drugOne_label.setGeometry(QtCore.QRect(int(-25 * width), int(110 * height), int(261 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")

        self.label_4 = QtWidgets.QTextEdit(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_4)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_4.setGraphicsEffect(shadow)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(int(1 * width))
        self.label_4.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QTextEdit(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(221 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(False)
        font.setWeight(int(25 * width))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label_5)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label_5.setGraphicsEffect(shadow)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(int(1 * width))
        self.label_5.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_5.setObjectName("label_5")

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
        each_drug.setCentralWidget(self.centralwidget)


        self.retranslateUi(each_drug)
        self.set_drug_info(drug_name_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(each_drug)

        self.add_back_pushButton.clicked.connect(self.backpage)
        self.delete_pushButton.clicked.connect(self.delete_drug)
        # self.next_pushButton.clicked.connect(self.open_each_drug2)

                

        def save_changes():
            # ตรวจสอบข้อมูลที่ถูกแก้ไขและบันทึกลงฐานข้อมูลหรือตัวแปรที่เหมาะสม
            updated_data = {} 
            updated_data['drug_name'] = self.label_2.toPlainText()
            updated_data['drug_description'] = self.label_3.toPlainText()
            updated_data['drug_remaining'] = self.label_4.toPlainText()
            updated_data['drug_eat'] = self.label_5.toPlainText()

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้า each_drug2
            drug_Update_instance.Set(updated_data)
            self.open_each_drug2()
        
        self.next_pushButton.clicked.connect(save_changes)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.delete_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.delete_pushButton))
        self.delete_pushButton.released.connect(lambda: self.set_button_released_style(self.delete_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))

    def delete_drug(self):
        drug_name = drug_name_instance.Get()
        
        drug_name = self.label_2.toPlainText()  # รับชื่อยาจาก Label

        # Use the custom message box
        QMessageBox = CustomMessageBox()
        
        reply = QMessageBox.question(self.each_drug, 'ลบยา', f'คุณต้องการลบยา "{drug_name}" ใช่หรือไม่?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
            cursor = connection.cursor()
            cursor.execute("SELECT drug_id FROM Drug WHERE drug_name = ?", (drug_name,))
            result = cursor.fetchone()
            print(result)
            cursor.execute("DELETE FROM Drug WHERE drug_name = ?", (drug_name,))
            
            cursor.execute("DELETE FROM Drug_handle WHERE drug_id = ?", result)
            connection.commit()
            connection.close()
            self.save_prepare_state(False)
            self.backpage()  # ปิดหน้าต่างหลังจากลบเสร็จ


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
        from drug_List import Ui_drug_List
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_drug_List)

    def closeAll(self):
        self.each_drug.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2

    def open_each_drug2(self):
        # print(f"each_drug {drug_Update_instance.Get()}")

        each_drug_instance.Set(self)
        drug_list_instance.Set(self.drug_List)
        drug_ID_instance.Set(self.drug_id)
        each_drug2_form = UI_Genarate()
        each_drug2_form.widgetSet(UI_instance.Get(), Ui_each_drug2)
        
    def save_prepare_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.prepare_state_file, 'w') as f:
            f.write(prepare_str)

    def set_drug_info(self, drug_name):
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Drug WHERE drug_name = ?", (drug_name,))
        drug_info = cursor.fetchone()
        print(drug_info)
        connection.close()

        if drug_info:
            self.label.setText(drug_info[1])

            self.drug_id = drug_info[0]
            # drug_info[1] is drug_name
            self.label_2.setPlainText(drug_info[1])
            # drug_info[2] is drug_description
            self.label_3.setPlainText(drug_info[2])
            # drug_info[3] is drug_remaining
            self.label_4.setPlainText(str(drug_info[3]))  # Use str() to convert to string
            # drug_info[4] is drug_eat
            self.label_5.setPlainText(str(drug_info[8]))  # Use str() to convert to string


    def retranslateUi(self, each_drug):
        _translate = QtCore.QCoreApplication.translate
        each_drug.setWindowTitle(_translate("each_drug", "ยาแต่ละตัว"))
        self.label.setText(_translate("each_drug", "ชื่อยา"))
        self.add_back_pushButton.setText(_translate("each_drug", "ย้อนกลับ"))
        #self.edit_pushButton.setText(_translate("each_drug", "แก้ไข"))
        self.delete_pushButton.setText(_translate("each_drug", "ลบ"))
        self.drugName_label.setText(_translate("each_drug", "ชื่อยา *"))
        self.drugDescribe_label.setText(_translate("each_drug", "คำอธิบายยา"))
        self.drugOne_label.setText(_translate("each_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด) *"))
        self.drugAll_label.setText(_translate("each_drug", "จำนวนยาทั้งหมดที่มี (เม็ด) *"))
        self.next_pushButton.setText(_translate("each_drug", "ถัดไป"))
        self.label_2.setText(_translate("each_drug", "ชื่อยา"))
        self.label_3.setText(_translate("each_drug", "คำอธิบายยา"))
        self.label_4.setText(_translate("each_drug", "ยาทั้งหมด"))
        self.label_5.setText(_translate("each_drug", "ยาที่กิน"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    each_drug = QtWidgets.QMainWindow()
    ui = Ui_each_drug()
    ui.setupUi(each_drug)
    each_drug.show()
    sys.exit(app.exec_())
