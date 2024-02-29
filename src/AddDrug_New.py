from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import *
import sqlite3

class NumericOnlyTextEdit(QtWidgets.QTextEdit):
    def keyPressEvent(self, event):
        # Allow only numeric characters, Backspace, and Decimal point
        if event.key() == QtCore.Qt.Key_Backspace or event.text().isdigit() or event.text() == '.':
            super().keyPressEvent(event)
        else:
            event.ignore()
            
class Ui_Add_drug(object):
    def setupUi(self, Add_drug):
        UI_instance.Set(Add_drug)
        show_widget_fullscreen(Add_drug)

        self.Add_drug = Add_drug
        
        Add_drug.setObjectName("Add_drug")
        Add_drug.resize(int(683 * width), int(400 * height))
        Add_drug.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(Add_drug)
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
        self.img_label.setGeometry(QtCore.QRect(int(283 * width), int(80 * height), int(31 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/adddrug.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(71 * width), int(31 * height)))
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
        self.drugName_label = QtWidgets.QLabel(self.frame_2)
        self.drugName_label.setGeometry(QtCore.QRect(int(10 * width), int(20 * height), int(101 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(int(10 * width), int(50 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.textEdit)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.textEdit.setGraphicsEffect(shadow)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.drugDescribe_label = QtWidgets.QLabel(self.frame_2)
        self.drugDescribe_label.setGeometry(QtCore.QRect(int(10 * width), int(110 * height), int(131 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(int(10 * width), int(140 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.textEdit_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.textEdit_2.setGraphicsEffect(shadow)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
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
        self.drugAll_label = QtWidgets.QLabel(self.frame_3)
        self.drugAll_label.setGeometry(QtCore.QRect(int(-25 * width), int(20 * height), int(251 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.textEdit_3 = NumericOnlyTextEdit(self.frame_3)
        self.textEdit_3.setGeometry(QtCore.QRect(int(12 * width), int(50 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.textEdit_3)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.textEdit_3.setGraphicsEffect(shadow)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setObjectName("textEdit_3")
        self.drugOne_label = QtWidgets.QLabel(self.frame_3)
        self.drugOne_label.setGeometry(QtCore.QRect(int(-20 * width), int(110 * height), int(261 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")
        self.textEdit_4 = NumericOnlyTextEdit(self.frame_3)
        self.textEdit_4.setGeometry(QtCore.QRect(int(12 * width), int(140 * height), int(211 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * height))
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.textEdit_4)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.textEdit_4.setGraphicsEffect(shadow)
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_4.setObjectName("textEdit_4")
        self.saveDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDrug_pushButton.setGeometry(QtCore.QRect(int(300 * width), int(330 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.saveDrug_pushButton.setFont(font)
        self.saveDrug_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.saveDrug_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.saveDrug_pushButton.setGraphicsEffect(shadow)
        self.saveDrug_pushButton.setObjectName("saveDrug_pushButton")
        Add_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_drug)
        QtCore.QMetaObject.connectSlotsByName(Add_drug)
        Add_drug.setTabOrder(self.textEdit, self.textEdit_2)
        Add_drug.setTabOrder(self.textEdit_2, self.saveDrug_pushButton)

        self.add_back_pushButton.clicked.connect(self.backpage)

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.saveDrug_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.saveDrug_pushButton))
        self.saveDrug_pushButton.released.connect(lambda: self.set_button_released_style(self.saveDrug_pushButton))

        #Add_drug.setTabOrder(self.saveDrug_pushButton, self.listHave_pushButton)
        #Add_drug.setTabOrder(self.listHave_pushButton, self.add_back_pushButton)

        

        #def open_drug_list():
        #    drug_list_window = QtWidgets.QMainWindow()
        #    drug_list_ui = Ui_drugList()
        #    drug_list_ui.setupUi(drug_list_window)
        #    drug_list_ui.load_drugs_from_database()  # เรียกฟังก์ชันนี้เมื่อเปิดหน้ารายการยา
        #    drug_list_window.show()
            
        #self.listHave_pushButton.clicked.connect(open_drug_list) 

        
        # เชื่อมต่อกับฟังก์ชัน save_drug                                                                      
        self.saveDrug_pushButton.clicked.connect(self.save_drug)

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


    def save_drug(self):
        width, height = Scale_Width_Height()
        drug_name = self.textEdit.toPlainText()
        drug_description = self.textEdit_2.toPlainText()
        drug_amount = self.textEdit_3.toPlainText()
        drug_eat = self.textEdit_4.toPlainText()
        
        if not drug_name.strip() or not drug_amount.strip() or not drug_eat.strip():
            self.saveDrug_pushButton.setEnabled(False)
            self.add_back_pushButton.setEnabled(False)
            
            error_dialog = QtWidgets.QDialog(self.centralwidget)
            error_dialog.setWindowTitle("ผิดพลาด")
            error_dialog.setModal(True)
            error_dialog.move(200, 200)
            error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            # Create and configure QLabel for the error message
            error_label = QtWidgets.QLabel("กรุณากรอกข้อมูลที่จำเป็น", error_dialog)
            font = QtGui.QFont()
            font.setPointSize(int(12 * height))
            error_label.setFont(font)
            error_label.setAlignment(QtCore.Qt.AlignCenter)

            # Create and configure OK button
            ok_button = QtWidgets.QPushButton("ตกลง", error_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(int(12 * height))
            ok_button.setFont(ok_button_font)

            # Set background color for the dialog
            error_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

            # Set button background and text color
            ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

            # Set QDialog layout
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(error_label)
            layout.addWidget(ok_button)
            error_dialog.setLayout(layout)

            # Connect the OK button's click event to close the error_dialog
            ok_button.clicked.connect(error_dialog.accept)

            # Show the QDialog
            error_dialog.exec_()
            
            self.saveDrug_pushButton.setEnabled(True)  # <-- เพิ่มบรรทัดนี้
            return  # Do not proceed with saving
        
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")
        cursor = connection.cursor()
        # เช็คว่า drug_name ที่ต้องการเพิ่มมีอยู่แล้วหรือไม่
        cursor.execute("SELECT COUNT(*) FROM Drug WHERE drug_name = ?", (drug_name,))
        count = cursor.fetchone()[0]
        if count > 0:
            # ถ้ามี drug_name นี้อยู่แล้วในฐานข้อมูล
            # แสดงข้อความว่า drug_name ซ้ำกัน
            error_dialog = QtWidgets.QDialog(self.centralwidget)
            error_dialog.setWindowTitle("ผิดพลาด")
            error_dialog.setModal(True)
            error_dialog.move(200, 200)
            error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            error_label = QtWidgets.QLabel("ชื่อยาซ้ำกัน กรุณาเปลี่ยนชื่อยา", error_dialog)
            font = QtGui.QFont()
            font.setPointSize(int(12 * height))
            error_label.setFont(font)
            error_label.setAlignment(QtCore.Qt.AlignCenter)

            ok_button = QtWidgets.QPushButton("ตกลง", error_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(int(12 * height))
            ok_button.setFont(ok_button_font)

            error_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")
            ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(error_label)
            layout.addWidget(ok_button)
            error_dialog.setLayout(layout)

            ok_button.clicked.connect(error_dialog.accept)
            error_dialog.exec_()
            return

        cursor.execute("INSERT INTO Drug (drug_name, drug_description, drug_remaining, drug_eat, all_drug_recieve) VALUES (?, ?, ?, ?, ?)", (drug_name, drug_description, drug_amount, drug_eat, drug_amount))
        connection.commit()
        connection.close()
        
        # Disable save button
        self.saveDrug_pushButton.setEnabled(False)
        self.add_back_pushButton.setEnabled(False)

        # สร้าง QDialog และกำหนดสไตล์
        message_dialog = QtWidgets.QDialog(self.centralwidget)
        message_dialog.setWindowTitle("บันทึกสำเร็จ")
        message_dialog.setModal(True)
        message_dialog.move(150, 200)
        message_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Create and configure QLabel
        message_label = QtWidgets.QLabel(message_dialog)
        message_label.setText("บันทึกข้อมูลยาเรียบร้อยแล้ว")
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        message_label.setFont(font)
        message_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create and configure OK button
        ok_button = QtWidgets.QPushButton(message_dialog)
        ok_button.setText("ตกลง")
        ok_button_font = QtGui.QFont()
        ok_button_font.setPointSize(int(12 * height))
        ok_button.setFont(ok_button_font)

        # Set background color for the dialog
        message_dialog.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 30px;")

        # Set button background and text color
        ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

        # Set QDialog layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(ok_button)
        message_dialog.setLayout(layout)

        # Connect the OK button's click event to close the dialog
        ok_button.clicked.connect(message_dialog.accept)

        # Show the QDialog
        message_dialog.exec_()
        
        # ล้างข้อมูลใน textEdit, textEdit_2, textEdit_3, textEdit_4
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.backpage()
        
    def homepage(self):
        from main import Ui_Medicine_App
        homepage_form = UI_Genarate()
        homepage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def backpage(self):
        from drug_List import Ui_drug_List
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_drug_List)

    def retranslateUi(self, Add_drug):
        _translate = QtCore.QCoreApplication.translate
        Add_drug.setWindowTitle(_translate("Add_drug", "เพิ่มยา"))
        self.label.setText(_translate("Add_drug", "   เพิ่มยา"))
        self.drugName_label.setText(_translate("Add_drug", "ชื่อยา *"))
        self.drugDescribe_label.setText(_translate("Add_drug", "คำอธิบายยา"))
        self.drugAll_label.setText(_translate("Add_drug", "จำนวนยาทั้งหมดที่มี (เม็ด) *"))
        self.saveDrug_pushButton.setText(_translate("Add_drug", "บันทึกยา"))
        #self.listHave_pushButton.setText(_translate("Add_drug", "รายการยาที่มี"))
        self.add_back_pushButton.setText(_translate("Add_drug", "ย้อนกลับ"))
        self.drugOne_label.setText(_translate("Add_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด) *"))
        
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("/home/pi/Documents/Medicine_notify/src/medicine.db")
    if not db.open():
        print("Cannot establish a database connection.")
        sys.exit(1)
        
    Add_drug = QtWidgets.QMainWindow()
    ui = Ui_Add_drug()
    ui.setupUi(Add_drug)
    Add_drug.show()
    sys.exit(app.exec_())