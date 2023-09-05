from PyQt5 import QtCore, QtGui, QtWidgets
from addDrug import Ui_Add_drug
from setting import Ui_setting
from pack_med import Ui_med_pack
import sqlite3

import datetime
from PyQt5.QtCore import QTimer, QLocale

class Ui_Medicine_App(object):
    def setupUi(self, Medicine_App):
        Medicine_App.setObjectName("Medicine_App")
        Medicine_App.setEnabled(True)
        Medicine_App.resize(531, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Medicine_App.setWindowIcon(icon)
        Medicine_App.setStyleSheet("background-color: rgb(217, 244, 255)")
        Medicine_App.setIconSize(QtCore.QSize(40, 40))
        self.Home_Page = QtWidgets.QWidget(Medicine_App)
        self.Home_Page.setObjectName("Home_Page")
        self.addDrug_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.addDrug_pushButton.setGeometry(QtCore.QRect(90, 160, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addDrug_pushButton.setFont(font)
        self.addDrug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/drug_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDrug_pushButton.setIcon(icon1)
        self.addDrug_pushButton.setIconSize(QtCore.QSize(20, 40))
        self.addDrug_pushButton.setAutoDefault(False)
        self.addDrug_pushButton.setDefault(False)
        self.addDrug_pushButton.setFlat(False)
        self.addDrug_pushButton.setObjectName("addDrug_pushButton")
        self.home_label = QtWidgets.QLabel(self.Home_Page)
        self.home_label.setGeometry(QtCore.QRect(200, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.line.setGeometry(QtCore.QRect(-10, 110, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.setting_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.setting_pushButton.setGeometry(QtCore.QRect(260, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setting_pushButton.setFont(font)
        self.setting_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_pushButton.setIcon(icon2)
        self.setting_pushButton.setIconSize(QtCore.QSize(20, 40))
        self.setting_pushButton.setAutoDefault(False)
        self.setting_pushButton.setDefault(False)
        self.setting_pushButton.setFlat(False)
        self.setting_pushButton.setObjectName("setting_pushButton")
        self.putDrug_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.putDrug_pushButton.setGeometry(QtCore.QRect(130, 220, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.putDrug_pushButton.setFont(font)
        self.putDrug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.putDrug_pushButton.setIcon(icon3)
        self.putDrug_pushButton.setIconSize(QtCore.QSize(20, 50))
        self.putDrug_pushButton.setAutoDefault(False)
        self.putDrug_pushButton.setDefault(False)
        self.putDrug_pushButton.setFlat(False)
        self.putDrug_pushButton.setObjectName("putDrug_pushButton")
        self.alignment_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.alignment_pushButton.setGeometry(QtCore.QRect(150, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.alignment_pushButton.setFont(font)
        self.alignment_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Industry-Rack-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignment_pushButton.setIcon(icon4)
        self.alignment_pushButton.setIconSize(QtCore.QSize(20, 50))
        self.alignment_pushButton.setAutoDefault(False)
        self.alignment_pushButton.setDefault(False)
        self.alignment_pushButton.setFlat(False)
        self.alignment_pushButton.setObjectName("alignment_pushButton")
        self.drugLeft_pushButton = QtWidgets.QPushButton(self.Home_Page)
        self.drugLeft_pushButton.setGeometry(QtCore.QRect(140, 340, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drugLeft_pushButton.setFont(font)
        self.drugLeft_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/table_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drugLeft_pushButton.setIcon(icon5)
        self.drugLeft_pushButton.setIconSize(QtCore.QSize(20, 50))
        self.drugLeft_pushButton.setAutoDefault(False)
        self.drugLeft_pushButton.setDefault(False)
        self.drugLeft_pushButton.setFlat(False)
        self.drugLeft_pushButton.setObjectName("drugLeft_pushButton")
        self.label_2 = QtWidgets.QLabel(self.Home_Page)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 21, 21))
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
        self.label.setGeometry(QtCore.QRect(390, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Home_Page)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        Medicine_App.setCentralWidget(self.Home_Page)

        self.retranslateUi(Medicine_App)
        QtCore.QMetaObject.connectSlotsByName(Medicine_App)
        
        # อัพเดทเวลา
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        # Connect to SQLite database
        self.connection = sqlite3.connect("medicine.db")
        self.cursor = self.connection.cursor()
        
        # Create Drug table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Drug (
                drug_id INTEGER PRIMARY KEY AUTOINCREMENT,
                drug_name TEXT,
                drug_description TEXT
            )
        ''')

        # Create Drug_Meal table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Meal (
                meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                drug_id INTEGER,
                meal_name TEXT,
                time TEXT,
                checkbox_state INTEGER,
                FOREIGN KEY (drug_id) REFERENCES Drug(drug_id)
            )
        ''')
        
        # Check if the Meal table is empty, and if so, insert default values
        self.cursor.execute("SELECT COUNT(*) FROM Meal")
        meal_count = self.cursor.fetchone()[0]

        if meal_count == 0:
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเช้า ก่อนอาหาร", "06:00", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเช้า เที่ยงอาหาร", "06:30", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเที่ยง ก่อนอาหาร", "12:00", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเที่ยง หลังอาหาร", "12:30", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเย็น ก่อนอาหาร", "18:00", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อเย็น หลังอาหาร", "18:30", 0))
            self.cursor.execute("INSERT INTO Meal (meal_name, time, checkbox_state) VALUES (?, ?, ?)",
                                ("มื้อก่อนนอน", "20:30", 0))

        self.connection.commit()
        
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
        
        self.ui_setting.back_pushButton.clicked.connect(close_setting_window)
        
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
    # Set the locale to English
    english_locale = QLocale(QLocale.English)
    QLocale.setDefault(english_locale)
    Medicine_App.show()
    sys.exit(app.exec_())
