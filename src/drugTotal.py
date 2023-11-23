

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_drugTotal(object):
    def setupUi(self, drugTotal):
        drugTotal.setObjectName("drugTotal")
        drugTotal.resize(531, 401)
        drugTotal.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(drugTotal)
        self.centralwidget.setObjectName("centralwidget")
        self.add_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_back_pushButton.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
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
        drugTotal.setCentralWidget(self.centralwidget)

        self.retranslateUi(drugTotal)
        QtCore.QMetaObject.connectSlotsByName(drugTotal)

        def close_window():
            drugTotal.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(155, 120, 217, 241))
        self.tableWidget.setObjectName("tableWidget")

        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["มื้ออาหาร", "คงเหลือ"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(7)

        

    def retranslateUi(self, drugTotal):
        _translate = QtCore.QCoreApplication.translate
        drugTotal.setWindowTitle(_translate("drugTotal", "จำนวนมื้อยาคงเหลือ"))
        self.add_back_pushButton.setText(_translate("drugTotal", "ย้อนกลับ"))
        self.label.setText(_translate("drugTotal", "จำนวนมื้อยาคงเหลือ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drugTotal = QtWidgets.QMainWindow()
    ui = Ui_drugTotal()
    ui.setupUi(drugTotal)
    drugTotal.show()
    sys.exit(app.exec_())