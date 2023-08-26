from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_med_pack(object):
    def __init__(self):
        self.med_pack = None  # Initialize med_pack as an instance variable
    
    def setupUi(self, med_pack):
        self.med_pack = med_pack  # Assign the main window instance to med_pack
        med_pack.setObjectName("med_pack")
        med_pack.resize(1104, 839)
        font = QtGui.QFont()
        font.setPointSize(10)
        med_pack.setFont(font)
        med_pack.setStyleSheet("background-color: rgb(217, 244, 255)")
        med_pack.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(med_pack)
        self.centralwidget.setObjectName("centralwidget")
        
        self.packMed_label = QtWidgets.QLabel(self.centralwidget)
        self.packMed_label.setGeometry(QtCore.QRect(230, 50, 681, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.packMed_label.setFont(font)
        self.packMed_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.packMed_label.setFrameShape(QtWidgets.QFrame.Box)
        self.packMed_label.setLineWidth(1)
        self.packMed_label.setTextFormat(QtCore.Qt.AutoText)
        self.packMed_label.setScaledContents(False)
        self.packMed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.packMed_label.setWordWrap(True)
        self.packMed_label.setObjectName("packMed_label")
        
        self.pack_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.pack_icon_label.setGeometry(QtCore.QRect(270, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pack_icon_label.setFont(font)
        self.pack_icon_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pack_icon_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pack_icon_label.setLineWidth(1)
        self.pack_icon_label.setText("")
        self.pack_icon_label.setTextFormat(QtCore.Qt.AutoText)
        self.pack_icon_label.setPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"))
        self.pack_icon_label.setScaledContents(True)
        self.pack_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pack_icon_label.setWordWrap(True)
        self.pack_icon_label.setObjectName("pack_icon_label")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        
        self.pack_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pack_back_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack_back_pushButton.setFont(font)
        self.pack_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);border: 1px solid rgb(166, 0, 0); border-radius: 10px;\n"
"background-color: rgb(166, 0, 0)")
        self.pack_back_pushButton.setObjectName("pack_back_pushButton")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 230, 931, 471))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        
        self.step_label = QtWidgets.QLabel(self.frame)
        self.step_label.setGeometry(QtCore.QRect(40, 50, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.step_label.setFont(font)
        self.step_label.setObjectName("step_label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(280, 160, 401, 231))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/image/med_pack1_img.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(930, 740, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(206, 255, 197);border: 1px solid rgb(0, 0, 0); border-radius: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/next_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_pushButton.setIcon(icon)
        self.next_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.next_pushButton.setObjectName("next_pushButton")
        
        self.next_pushButton.clicked.connect(self.showMedPack2)
        
        med_pack.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(med_pack)
        QtCore.QMetaObject.connectSlotsByName(med_pack)
        
        med_pack.showFullScreen()

        def close_window_1():
            med_pack.close()

        self.pack_back_pushButton.clicked.connect(close_window_1)
        
    def showMedPack2(self):
        self.med_pack2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_med_pack2()
        self.ui2.setupUi(self.med_pack2, self)
        self.ui2.showMedPack(self.med_pack2)
        self.med_pack2.show()
        
    def closeMedPack(self):
        self.med_pack.close()  # Close the main window
        self.med_pack2.close()


    def retranslateUi(self, med_pack):
        _translate = QtCore.QCoreApplication.translate
        med_pack.setWindowTitle(_translate("med_pack", "วิธีการใส่ยา"))
        self.packMed_label.setText(_translate("med_pack", "     วิธีการใส่ยาในกล่องบรรจุยา"))
        self.pack_back_pushButton.setText(_translate("med_pack", "ย้อนกลับ"))
        self.step_label.setText(_translate("med_pack", "1. นำยาใส่ในซองสีชา"))
        self.next_pushButton.setText(_translate("med_pack", " ถัดไป"))
import resources_rc

class Ui_med_pack2(object):
    def setupUi(self, med_pack2, ui_med_pack):
        self.ui_med_pack = ui_med_pack  # เก็บ instance ของ Ui_med_pack เอาไว้ในตัวแปร

        med_pack2.setObjectName("med_pack2")
        med_pack2.resize(1104, 839)
        font = QtGui.QFont()
        font.setPointSize(10)
        med_pack2.setFont(font)
        med_pack2.setStyleSheet("background-color: rgb(217, 244, 255)")
        med_pack2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget2 = QtWidgets.QWidget(med_pack2)
        self.centralwidget2.setObjectName("centralwidget2")
        
        self.packMed2_label = QtWidgets.QLabel(self.centralwidget2)
        self.packMed2_label.setGeometry(QtCore.QRect(230, 50, 681, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.packMed2_label.setFont(font)
        self.packMed2_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.packMed2_label.setFrameShape(QtWidgets.QFrame.Box)
        self.packMed2_label.setLineWidth(1)
        self.packMed2_label.setTextFormat(QtCore.Qt.AutoText)
        self.packMed2_label.setScaledContents(False)
        self.packMed2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.packMed2_label.setWordWrap(True)
        self.packMed2_label.setObjectName("packMed2_label")
        
        self.pack_icon2_label = QtWidgets.QLabel(self.centralwidget2)
        self.pack_icon2_label.setGeometry(QtCore.QRect(270, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pack_icon2_label.setFont(font)
        self.pack_icon2_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pack_icon2_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pack_icon2_label.setLineWidth(1)
        self.pack_icon2_label.setText("")
        self.pack_icon2_label.setTextFormat(QtCore.Qt.AutoText)
        self.pack_icon2_label.setPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"))
        self.pack_icon2_label.setScaledContents(True)
        self.pack_icon2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pack_icon2_label.setWordWrap(True)
        self.pack_icon2_label.setObjectName("pack_icon2_label")
        
        self.line2 = QtWidgets.QFrame(self.centralwidget2)
        self.line2.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line2.setLineWidth(3)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        
        self.pack_back2_pushButton = QtWidgets.QPushButton(self.centralwidget2)
        self.pack_back2_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pack_back2_pushButton.setFont(font)
        self.pack_back2_pushButton.setStyleSheet("color: rgb(255, 255, 255);border: 1px solid rgb(166, 0, 0); border-radius: 10px;\n"
"background-color: rgb(166, 0, 0)")
        self.pack_back2_pushButton.setObjectName("pack_back2_pushButton")
        
        self.frame2 = QtWidgets.QFrame(self.centralwidget2)
        self.frame2.setGeometry(QtCore.QRect(90, 230, 931, 471))
        self.frame2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setObjectName("frame2")
        
        self.step2_label = QtWidgets.QLabel(self.frame2)
        self.step2_label.setGeometry(QtCore.QRect(40, 50, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.step2_label.setFont(font)
        self.step2_label.setObjectName("step2_label")
        
        self.img2_label = QtWidgets.QLabel(self.frame2)
        self.img2_label.setGeometry(QtCore.QRect(230, 160, 451, 231))
        self.img2_label.setText("")
        self.img2_label.setPixmap(QtGui.QPixmap(":/image/med_pack2_img.png"))
        self.img2_label.setScaledContents(True)
        self.img2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img2_label.setObjectName("img2_label")
        
        self.next2_pushButton = QtWidgets.QPushButton(self.centralwidget2)
        self.next2_pushButton.setGeometry(QtCore.QRect(890, 740, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next2_pushButton.setFont(font)
        self.next2_pushButton.setStyleSheet("background-color: rgb(206, 255, 197);border: 1px solid rgb(0, 0, 0); border-radius: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/next_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next2_pushButton.setIcon(icon)
        self.next2_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.next2_pushButton.setObjectName("next2_pushButton")
        
        med_pack2.setCentralWidget(self.centralwidget2)

        self.retranslateUi(med_pack2)
        QtCore.QMetaObject.connectSlotsByName(med_pack2)
        
        self.next2_pushButton.clicked.connect(self.closeMedPack)  # เชื่อมตัวดำเนินการปิดหน้าต่าง
        
        med_pack2.showFullScreen()
        
        def close_window_2():
            med_pack2.close()

        self.pack_back2_pushButton.clicked.connect(close_window_2)
        
    def showMedPack(self, med_pack2):

        self.med_pack2 = med_pack2  # บันทึกตัวแปรเข้าสมาชิกของคลาส
        self.med_pack2.show()
        
    def closeMedPack(self):
        self.ui_med_pack.closeMedPack()  # เรียกใช้เมธอด closeMedPack ของ Ui_med_pack
        self.med_pack2.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2



    def retranslateUi(self, med_pack2):
        _translate = QtCore.QCoreApplication.translate
        med_pack2.setWindowTitle(_translate("med_pack2", "วิธีการใส่ยา"))
        self.packMed2_label.setText(_translate("med_pack2", "     วิธีการใส่ยาในกล่องบรรจุยา"))
        self.pack_back2_pushButton.setText(_translate("med_pack2", "ย้อนกลับ"))
        self.step2_label.setText(_translate("med_pack2", "2. นำซองยาสีชาใส่ในกล่องบรรจุยา"))
        self.next2_pushButton.setText(_translate("med_pack2", " เข้าใจแล้ว"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    med_pack = QtWidgets.QMainWindow()
    ui = Ui_med_pack()
    ui.setupUi(med_pack)
    
    
    sys.exit(app.exec_())
