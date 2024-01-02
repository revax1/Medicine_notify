from PyQt5 import QtCore, QtGui, QtWidgets
from each_drug2 import Ui_each_drug2
import sqlite3

import os
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

class Ui_each_drug(object):   
    def setupUi(self, each_drug, drug_List):
        self.each_drug = each_drug
        self.drug_List = drug_List
        
        each_drug.setObjectName("each_drug")
        each_drug.resize(531, 401)
        each_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(each_drug)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 201, 51))
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
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(430, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.drugName_label = QtWidgets.QLabel(self.centralwidget)
        self.drugName_label.setGeometry(QtCore.QRect(20, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugName_label.setFont(font)
        self.drugName_label.setObjectName("drugName_label")
        self.drugDescribe_label = QtWidgets.QLabel(self.centralwidget)
        self.drugDescribe_label.setGeometry(QtCore.QRect(20, 150, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugDescribe_label.setFont(font)
        self.drugDescribe_label.setObjectName("drugDescribe_label")
        self.drugOne_label = QtWidgets.QLabel(self.centralwidget)
        self.drugOne_label.setGeometry(QtCore.QRect(20, 210, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugOne_label.setFont(font)
        self.drugOne_label.setObjectName("drugOne_label")
        self.drugAll_label = QtWidgets.QLabel(self.centralwidget)
        self.drugAll_label.setGeometry(QtCore.QRect(20, 180, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drugAll_label.setFont(font)
        self.drugAll_label.setObjectName("drugAll_label")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(410, 280, 85, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        self.label_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(1)
        self.label_2.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(1)
        self.label_3.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(1)
        self.label_4.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 210, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(1)
        self.label_5.setCurrentCharFormat(QtGui.QTextCharFormat())
        
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.label_5.setObjectName("label_5")
        each_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(each_drug)
        QtCore.QMetaObject.connectSlotsByName(each_drug)

        def close_window():
            each_drug.close()

        self.add_back_pushButton.clicked.connect(close_window)

        
        self.next_pushButton.clicked.connect(self.open_each_drug2)

        def delete_drug():
            drug_name = self.label_2.text()  # รับชื่อยาจาก Label
            reply = QtWidgets.QMessageBox.question(each_drug, 'ลบยา', f'คุณต้องการลบยา "{drug_name}" ใช่หรือไม่?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                connection = sqlite3.connect("medicine.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Drug WHERE drug_name = ?", (drug_name,))
                connection.commit()
                connection.close()
                each_drug.close()  # ปิดหน้าต่างหลังจากลบเสร็จ
        
        self.delete_pushButton.clicked.connect(delete_drug)
        
    def closeAll(self):
        self.each_drug.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2

    def open_each_drug2(self):
        #drug_name = self.label_2.text()
        self.each_drug2_window = QtWidgets.QMainWindow()
        self.each_drug2_ui = Ui_each_drug2()
        self.each_drug2_ui.setupUi(self.each_drug2_window, self.drug_List, self)
        self.each_drug2_ui.set_drug2_info(self.drug_id)
        self.each_drug2_window.show()

    def set_drug_info(self, drug_name):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Drug WHERE drug_name = ?", (drug_name,))
        drug_info = cursor.fetchone()
        connection.close()

        if drug_info:
            self.drug_id = drug_info[0]
            # drug_info[1] is drug_name
            self.label_2.setPlainText(drug_info[1])
            # drug_info[2] is drug_description
            self.label_3.setPlainText(drug_info[2])
            # drug_info[3] is drug_amount
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
        self.drugName_label.setText(_translate("each_drug", "ชื่อยา : "))
        self.drugDescribe_label.setText(_translate("each_drug", "คำอธิบายยา : "))
        self.drugOne_label.setText(_translate("each_drug", "จำนวนยาที่กินต่อ 1 มื้อ (เม็ด) : "))
        self.drugAll_label.setText(_translate("each_drug", "จำนวนยาทั้งหมดที่มี (เม็ด) :"))
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