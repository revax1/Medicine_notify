import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"


import sqlite3


class NumericOnlyTextEdit(QtWidgets.QTextEdit):
    def keyPressEvent(self, event):
        # Allow only numeric characters and certain key events (e.g., Backspace)
        if event.key() == QtCore.Qt.Key_Backspace or event.text().isdigit() or event.text() == '.':
            super().keyPressEvent(event)
        else:
            event.ignore()
class Ui_Add_drug(object):

    def setupUi(self, Add_drug, drug_List):
        self.Add_drug = Add_drug
        self.drug_List = drug_List
        
        Add_drug.setObjectName("Add_drug")
        Add_drug.resize(531, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/Resources/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Add_drug.setWindowIcon(icon)
        Add_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(Add_drug)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/drug_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(30, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(30, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 240, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAccessibleName("")
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 109, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.drugAll_label = QtWidgets.QLabel(self.centralwidget)
        self.drugAll_label.setGeometry(QtCore.QRect(280, 130, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugAll_label.setObjectName("drugAll_label")
        self.saveDrug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDrug_pushButton.setGeometry(QtCore.QRect(220, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveDrug_pushButton.setFont(font)
        self.saveDrug_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.saveDrug_pushButton.setObjectName("saveDrug_pushButton")
        #self.listHave_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.listHave_pushButton.setGeometry(QtCore.QRect(370, 40, 141, 31))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.listHave_pushButton.setFont(font)
        #self.listHave_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.listHave_pushButton.setObjectName("listHave_pushButton")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.drugOne_label = QtWidgets.QLabel(self.centralwidget)
        self.drugOne_label.setGeometry(QtCore.QRect(280, 210, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugOne_label.setObjectName("drugOne_label")

        self.textEdit_3 = NumericOnlyTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(280, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setObjectName("textEdit_3")


        self.textEdit_4 = NumericOnlyTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_4.setObjectName("textEdit_4")
        Add_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_drug)
        QtCore.QMetaObject.connectSlotsByName(Add_drug)
        Add_drug.setTabOrder(self.textEdit, self.textEdit_2)
        Add_drug.setTabOrder(self.textEdit_2, self.saveDrug_pushButton)

        self.add_back_pushButton.clicked.connect(self.closeAll)

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


    def save_drug(self):
        drug_name = self.textEdit.toPlainText()
        drug_description = self.textEdit_2.toPlainText()
        drug_amount = self.textEdit_3.toPlainText()
        drug_eat = self.textEdit_4.toPlainText()
        
        if not drug_name.strip():
            error_dialog = QtWidgets.QDialog(self.centralwidget)
            error_dialog.setWindowTitle("ผิดพลาด")
            error_dialog.setModal(True)
            error_dialog.move(200, 200)
            error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            # Create and configure QLabel for the error message
            error_label = QtWidgets.QLabel("กรุณาระบุชื่อยา", error_dialog)
            font = QtGui.QFont()
            font.setPointSize(12)
            error_label.setFont(font)
            error_label.setAlignment(QtCore.Qt.AlignCenter)

            # Create and configure OK button
            ok_button = QtWidgets.QPushButton("ตกลง", error_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(12)
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
            return  # Do not proceed with saving

        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Drug (drug_name, drug_description, drug_remaining, drug_eat) VALUES (?, ?, ?, ?)", (drug_name, drug_description, drug_amount, drug_eat))
        connection.commit()
        connection.close()

        #  # เพิ่มเรียกใช้ฟังก์ชัน update_drug_list เพื่ออัพเดตรายการยาในหน้าคลังยา
        # self.update_drug_list()

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
        font.setPointSize(12)
        message_label.setFont(font)
        message_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create and configure OK button
        ok_button = QtWidgets.QPushButton(message_dialog)
        ok_button.setText("ตกลง")
        ok_button_font = QtGui.QFont()
        ok_button_font.setPointSize(12)
        ok_button.setFont(ok_button_font)

        # Set background color for the dialog
        message_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

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
        
    def closeAll(self):
        self.drug_List.closeAll()
        self.Add_drug.close()

    def retranslateUi(self, Add_drug):
        _translate = QtCore.QCoreApplication.translate
        Add_drug.setWindowTitle(_translate("Add_drug", "เพิ่มยา"))
        self.label.setText(_translate("Add_drug", "   เพิ่มยา"))
        self.drugName_label.setText(_translate("Add_drug", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("Add_drug", "คำอธิบายยา"))
        self.drugAll_label.setText(_translate("Add_drug", "จำนวนยาทั้งหมดที่มี (เม็ด)"))
        self.saveDrug_pushButton.setText(_translate("Add_drug", "บันทึกยา"))
        #self.listHave_pushButton.setText(_translate("Add_drug", "รายการยาที่มี"))
        self.add_back_pushButton.setText(_translate("Add_drug", "หน้าหลัก"))
        self.drugOne_label.setText(_translate("Add_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด)"))
        
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("medicine.db")
    if not db.open():
        print("Cannot establish a database connection.")
        sys.exit(1)
        
    Add_drug = QtWidgets.QMainWindow()
    ui = Ui_Add_drug()
    ui.setupUi(Add_drug)
    Add_drug.show()
    sys.exit(app.exec_())