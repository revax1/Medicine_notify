from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
import sqlite3

class Ui_Add_drug(object):
    def setupUi(self, Add_drug):
        Add_drug.setObjectName("Add_drug")
        Add_drug.resize(1104, 839)
        Add_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(Add_drug)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 50, 301, 71))
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
        self.label_2.setGeometry(QtCore.QRect(450, 70, 41, 41))
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
        self.line.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(70, 220, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 290, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(70, 370, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 440, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(560, 210, 20, 621))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(680, 290, 341, 411))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        
        self.drugHave_label = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label.setGeometry(QtCore.QRect(740, 220, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.drugHave_label.setFont(font)
        self.drugHave_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label.setObjectName("drugHave_label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 690, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);border: 2px solid rgb(85, 170, 127); border-radius: 10px;\n"
"background-color: rgb(85, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(890, 730, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);border: 1px solid rgb(0, 0, 0); border-radius: 10px;")
        self.delete_pushButton.setObjectName("delete_pushButton")
        
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);border: 2px solid rgb(166, 0, 0); border-radius: 10px;\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        
        Add_drug.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(Add_drug)
        QtCore.QMetaObject.connectSlotsByName(Add_drug)
        
        Add_drug.showFullScreen()
    
        def close_window():
            Add_drug.close()
            
        self.add_back_pushButton.clicked.connect(close_window)
        
        # เชื่อมต่อกับฟังก์ชัน save_drug                                                                          เพิ่งเพิ่มล่าสุด
        self.pushButton.clicked.connect(self.save_drug)
        # เชื่อมต่อกับฟังก์ชัน delete_drug
        self.delete_pushButton.clicked.connect(self.delete_drug)
        
        self.check_and_create_drug_table()

        # เรียกฟังก์ชันแสดงรายการยาที่มี
        self.load_drug_list()
        
    def check_and_create_drug_table(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Drug (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)")
        connection.commit()
        connection.close()

    def save_drug(self):
        drug_name = self.textEdit.toPlainText()
        drug_description = self.textEdit_2.toPlainText()
        
        if not drug_name.strip():
            error_dialog = QtWidgets.QDialog(self.centralwidget)
            error_dialog.setWindowTitle("ผิดพลาด")
            error_dialog.setModal(True)
            error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            # Create and configure QLabel for the error message
            error_label = QtWidgets.QLabel("กรุณาระบุชื่อยา", error_dialog)
            font = QtGui.QFont()
            font.setPointSize(18)
            error_label.setFont(font)
            error_label.setAlignment(QtCore.Qt.AlignCenter)

            # Create and configure OK button
            ok_button = QtWidgets.QPushButton("ตกลง", error_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(22)
            ok_button.setFont(ok_button_font)

            # Set background color for the dialog
            error_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

            # Set button background and text color
            ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

            # Set QDialog layout
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(error_label)
            layout.addWidget(ok_button)
            layout.setContentsMargins(40, 30, 40, 30)  # Add margins to the layout (left, top, right, bottom)
            error_dialog.setLayout(layout)

            # Connect the OK button's click event to close the error_dialog
            ok_button.clicked.connect(error_dialog.accept)

            # Show the QDialog
            error_dialog.exec_()
            return  # Do not proceed with saving

        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Drug (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)")
        cursor.execute("INSERT INTO Drug (name, description) VALUES (?, ?)", (drug_name, drug_description))
        connection.commit()
        connection.close()

        # สร้าง QDialog และกำหนดสไตล์
        message_dialog = QtWidgets.QDialog(self.centralwidget)
        message_dialog.setWindowTitle("บันทึกสำเร็จ")
        message_dialog.setModal(True)
        message_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # Create and configure QLabel
        message_label = QtWidgets.QLabel(message_dialog)
        message_label.setText("บันทึกข้อมูลยาเรียบร้อยแล้ว")
        font = QtGui.QFont()
        font.setPointSize(22)
        message_label.setFont(font)
        message_label.setAlignment(QtCore.Qt.AlignCenter)

        # Create and configure OK button
        ok_button = QtWidgets.QPushButton(message_dialog)
        ok_button.setText("ตกลง")
        ok_button_font = QtGui.QFont()
        ok_button_font.setPointSize(22)
        ok_button.setFont(ok_button_font)

        # Set background color for the dialog
        message_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

        # Set button background and text color
        ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 15px;")

        # Set QDialog layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(ok_button)
        layout.setContentsMargins(50, 30, 50, 30)  # Add margins to the layout (left, top, right, bottom)
        message_dialog.setLayout(layout)

        # Connect the OK button's click event to close the dialog
        ok_button.clicked.connect(message_dialog.accept)

        # Show the QDialog
        message_dialog.exec_()
        
        # ล้างข้อมูลใน textEdit และ textEdit_2
        self.textEdit.clear()
        self.textEdit_2.clear()
        
        # เรียกฟังก์ชันแสดงรายการยาที่มี                                                                            เพิ่งเพิ่มล่าสุด
        self.load_drug_list()

    def delete_drug(self): 
        selected_item = self.listWidget.currentItem()

        if selected_item:
            drug_name = selected_item.text()

            confirm_dialog = QDialog(self.centralwidget)
            confirm_dialog.setWindowTitle("ยืนยันการลบ")
            confirm_dialog.setModal(True)
            confirm_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

            # สร้าง QLabel แสดงข้อความยืนยัน
            confirm_label = QtWidgets.QLabel(confirm_dialog)
            confirm_label.setText( f"คุณต้องการลบรายการยา '{drug_name}' ใช่หรือไม่?")
            font = QtGui.QFont()
            font.setPointSize(22)
            confirm_label.setFont(font)
            confirm_label.setAlignment(QtCore.Qt.AlignCenter)

            # สร้างปุ่ม OK และ Cancel
            ok_button = QPushButton("ใช่", confirm_dialog)
            ok_button_font = QtGui.QFont()
            ok_button_font.setPointSize(22)
            ok_button.setFont(ok_button_font)
            cancel_button = QPushButton("ไม่", confirm_dialog)
            cancel_button_font = QtGui.QFont()
            cancel_button_font.setPointSize(22)
            cancel_button.setFont(ok_button_font)

            
            confirm_dialog.setStyleSheet("background-color: rgb(255, 241, 129); border-radius: 30px;")

            # กำหนดรูปแบบสไตล์ของปุ่ม
            ok_button.setStyleSheet("background-color: rgb(85, 170, 127); color: white; border: none; border-radius: 10px;")
            cancel_button.setStyleSheet("background-color: rgb(166, 0, 0); color: white; border: none; border-radius: 10px;")

            # สร้างเครื่องหมายสำหรับการปิด Dialog
            ok_button.clicked.connect(confirm_dialog.accept)
            cancel_button.clicked.connect(confirm_dialog.reject)

            # สร้าง Layout และเพิ่มวัตถุลงไป
            layout = QVBoxLayout()
            layout.addWidget(confirm_label)
            layout.addWidget(ok_button)
            layout.addWidget(cancel_button)
            layout.setContentsMargins(50, 30, 50, 30)  # Add margins to the layout (left, top, right, bottom)
            confirm_dialog.setLayout(layout)

            # แสดง Dialog และตรวจสอบผลลัพธ์
            result = confirm_dialog.exec_()

            if result == QDialog.Accepted:
                connection = sqlite3.connect("medicine.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Drug WHERE name=?", (drug_name,))
                connection.commit()
                connection.close()

                self.load_drug_list()

    def load_drug_list(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM Drug")
        drugs = cursor.fetchall()
        connection.close()

        self.listWidget.clear()

        for drug in drugs:
            drug_name = drug[0]
            self.listWidget.addItem(drug_name)


    def retranslateUi(self, Add_drug):
        _translate = QtCore.QCoreApplication.translate
        Add_drug.setWindowTitle(_translate("Add_drug", "เพิ่มยา"))
        self.label.setText(_translate("Add_drug", "   เพิ่มยา"))
        self.drugName_label.setText(_translate("Add_drug", "ชื่อยา"))
        self.drugDescribe_label.setText(_translate("Add_drug", "คำอธิบายยา"))
        self.drugHave_label.setText(_translate("Add_drug", "รายการยาที่มี"))
        self.pushButton.setText(_translate("Add_drug", "บันทึกยา"))
        self.delete_pushButton.setText(_translate("Add_drug", "ลบรายการ"))
        self.add_back_pushButton.setText(_translate("Add_drug", "ย้อนกลับ"))
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
