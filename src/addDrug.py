from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setGeometry(QtCore.QRect(890, 730, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_pushButton.setObjectName("delete_pushButton")
        
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        
        Add_drug.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(Add_drug)
        QtCore.QMetaObject.connectSlotsByName(Add_drug)
        
        Add_drug.showFullScreen()
    
        def close_window():
            Add_drug.close()
            
        self.add_back_pushButton.clicked.connect(close_window)


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
    Add_drug = QtWidgets.QMainWindow()
    ui = Ui_Add_drug()
    ui.setupUi(Add_drug)
    Add_drug.show()
    sys.exit(app.exec_())
