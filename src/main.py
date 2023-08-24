from PyQt5 import QtCore, QtGui, QtWidgets
from addDrug import Ui_Add_drug
from setting import Ui_setting
from pack_med import Ui_med_pack, Ui_med_pack2
import datetime
from PyQt5.QtCore import QTimer

class Ui_Medicine_App(object):
    def setupUi(self, Medicine_App):
        Medicine_App.setObjectName("Medicine_App")
        Medicine_App.setEnabled(True)
        Medicine_App.resize(1124, 855)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Medicine_App.setWindowIcon(icon)
        Medicine_App.setStyleSheet("background-color: rgb(217, 244, 255)")
        Medicine_App.setIconSize(QtCore.QSize(40, 40))
        
        self.Home_Page = QtWidgets.QWidget(Medicine_App)
        self.Home_Page.setObjectName("Home_Page")
        
        self.addDrug_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.addDrug_pushButton.setGeometry(QtCore.QRect(260, 240, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.addDrug_pushButton.setFont(font)
        self.addDrug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDrug_pushButton.setIcon(icon1)
        self.addDrug_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.addDrug_pushButton.setAutoDefault(False)
        self.addDrug_pushButton.setDefault(False)
        self.addDrug_pushButton.setFlat(False)
        self.addDrug_pushButton.setObjectName("addDrug_pushButton")
        
        self.home_label = QtWidgets.QLabel(self.Home_Page)
        self.home_label.setGeometry(QtCore.QRect(420, 50, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.home_label.setFont(font)
        self.home_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_label.setFrameShape(QtWidgets.QFrame.Box)
        self.home_label.setLineWidth(1)
        self.home_label.setTextFormat(QtCore.Qt.AutoText)
        self.home_label.setScaledContents(False)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setWordWrap(True)
        self.home_label.setObjectName("home_label")
        
        self.line = QtWidgets.QFrame(self.Home_Page)
        self.line.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        
        self.setting_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.setting_pushButton.setGeometry(QtCore.QRect(570, 240, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setting_pushButton.setFont(font)
        self.setting_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_pushButton.setIcon(icon2)
        self.setting_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.setting_pushButton.setAutoDefault(False)
        self.setting_pushButton.setDefault(False)
        self.setting_pushButton.setFlat(False)
        self.setting_pushButton.setObjectName("setting_pushButton")
        
        self.putDrug_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.putDrug_pushButton.setGeometry(QtCore.QRect(290, 360, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.putDrug_pushButton.setFont(font)
        self.putDrug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.putDrug_pushButton.setIcon(icon3)
        self.putDrug_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.putDrug_pushButton.setAutoDefault(False)
        self.putDrug_pushButton.setDefault(False)
        self.putDrug_pushButton.setFlat(False)
        self.putDrug_pushButton.setObjectName("putDrug_pushButton")
        
        self.alignment_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.alignment_pushButton.setGeometry(QtCore.QRect(310, 480, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.alignment_pushButton.setFont(font)
        self.alignment_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Industry-Rack-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignment_pushButton.setIcon(icon4)
        self.alignment_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.alignment_pushButton.setAutoDefault(False)
        self.alignment_pushButton.setDefault(False)
        self.alignment_pushButton.setFlat(False)
        self.alignment_pushButton.setObjectName("alignment_pushButton")
        
        self.drugLeft_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.drugLeft_pushButton.setGeometry(QtCore.QRect(350, 600, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.drugLeft_pushButton.setFont(font)
        self.drugLeft_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/table_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drugLeft_pushButton.setIcon(icon5)
        self.drugLeft_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.drugLeft_pushButton.setAutoDefault(False)
        self.drugLeft_pushButton.setDefault(False)
        self.drugLeft_pushButton.setFlat(False)
        self.drugLeft_pushButton.setObjectName("drugLeft_pushButton")
        
        self.label_2 = QtWidgets.QLabel(self.Home_Page)
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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/home_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(self.Home_Page)
        self.label.setGeometry(QtCore.QRect(820, 60, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Home_Page)
        self.label_3.setGeometry(QtCore.QRect(80, 60, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        Medicine_App.setCentralWidget(self.Home_Page)
        
        # อัพเดทเวลา
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


        self.retranslateUi(Medicine_App)
        QtCore.QMetaObject.connectSlotsByName(Medicine_App)
        
        self.addDrug_pushButton.clicked.connect(self.open_add_drug_page)
        self.setting_pushButton.clicked.connect(self.open_setting_page)
        self.putDrug_pushButton.clicked.connect(self.open_pack_page)

        
    ###################### เวลา #############################
    def update_time(self):
        current_datetime = datetime.datetime.now()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_date = current_datetime.strftime("%a, %d %b %Y")
        
        self.label.setText(current_time)
        self.label_3.setText(current_date)

    ###################### หน้าเพิ่มยา #############################  
    def open_add_drug_page(self):
        self.add_drug_window = QtWidgets.QMainWindow()
        self.ui_add_drug = Ui_Add_drug()
        self.ui_add_drug.setupUi(self.add_drug_window)
        self.add_drug_window.show()
        
        def close_add_drug_window():
            self.add_drug_window.close()

        self.ui_add_drug.add_back_pushButton.clicked.connect(close_add_drug_window)
        
    ###################### หน้าตั้งค่ามื้อยา ############################# 
    def open_setting_page(self):
        self.setting_window = QtWidgets.QMainWindow()
        self.ui_setting = Ui_setting()
        self.ui_setting.setupUi(self.setting_window)
        self.setting_window.show()
        
        def close_setting_window():
            self.setting_window.close()
        
        self.ui_setting.setting_back_pushButton.clicked.connect(close_setting_window)
        
    ###################### หน้าวิธีจัดเรียงยา ############################# 
    def open_pack_page(self):
        self.pack_window = QtWidgets.QMainWindow()
        self.ui_pack = Ui_med_pack()
        self.ui_pack.setupUi(self.pack_window)
        self.pack_window.show()
        
        def close_pack_window():
            self.pack_window.close()
            
        self.ui_pack.pack_back_pushButton.clicked.connect(close_pack_window)

    def retranslateUi(self, Medicine_App):
        _translate = QtCore.QCoreApplication.translate
        Medicine_App.setWindowTitle(_translate("Medicine_App", "หน้าแรก"))
        self.addDrug_pushButton.setText(_translate("Medicine_App", "  เพิ่มยา"))
        self.home_label.setText(_translate("Medicine_App", "   หน้าแรก"))
        self.setting_pushButton.setText(_translate("Medicine_App", "  ตั้งค่ามื้อยา"))
        self.putDrug_pushButton.setText(_translate("Medicine_App", "  วิธีการใส่ยาในกล่องบรรจุยา"))
        self.alignment_pushButton.setText(_translate("Medicine_App", "  วิธีเรียงกล่องบรรจุยา"))
        self.drugLeft_pushButton.setText(_translate("Medicine_App", "  จำนวนมื้อยาคงเหลือ"))
        
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Medicine_App = QtWidgets.QMainWindow()
    ui = Ui_Medicine_App()
    ui.setupUi(Medicine_App)
    Medicine_App.showFullScreen()
    Medicine_App.show()
    sys.exit(app.exec_())
