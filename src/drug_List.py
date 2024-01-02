from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from AddDrug_New import Ui_Add_drug
from each_drug import Ui_each_drug
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
# from select_meal import Ui_select_meal
import sqlite3
from PyQt5.QtCore import QLocale
import sys

class Ui_drug_List(object):       
    def setupUi(self, drug_List):
        self.drug_List = drug_List
        drug_List.setObjectName("drug_List")
        drug_List.resize(531, 401)
        drug_List.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(drug_List)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 141, 51))
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
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setGeometry(QtCore.QRect(410, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 179, 85);")
        self.add_pushButton.setObjectName("add_pushButton")
        drug_List.setCentralWidget(self.centralwidget)

        self.retranslateUi(drug_List)
        QtCore.QMetaObject.connectSlotsByName(drug_List)

        self.drug_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.drug_list_widget.setGeometry(QtCore.QRect(20, 120, 491, 261))
        self.update_drug_list()  # เรียกใช้ฟังก์ชันเพื่อแสดงรายการยาในคลังยา

        # Connect the itemClicked signal to handle_drug_item_click method
        self.drug_list_widget.itemClicked.connect(self.handle_drug_item_click) #คลิกชื่อยาแล้วเปิดหน้าeach_drug

        def close_window():
            drug_List.close()
            
        # self.add_back_pushButton.clicked.connect(self.open_drug_list_again)
        self.add_back_pushButton.clicked.connect(close_window)
            
        self.add_pushButton.clicked.connect(self.open_add_drug)

    def handle_drug_item_click(self, item):
        # Get the text of the clicked item (drug name)
        drug_name = item.text()

        # Open the each_drug window with the selected drug
        self.each_drug_window = QtWidgets.QMainWindow()           
        self.each_drug_ui = Ui_each_drug()                          
        
        self.each_drug_ui.setupUi(self.each_drug_window, self)     
        
        # Set drug info for the each_drug window
        self.each_drug_ui.set_drug_info(drug_name)

        # Pass the drug name to the each_drug window
        self.each_drug_ui.label.setText(drug_name)   
        self.each_drug_window.show()                    
        
    def closeAll(self):
        self.drug_List.close()

    def open_add_drug(self):
        self.add_drug_window = QtWidgets.QMainWindow()
        self.add_drug_ui = Ui_Add_drug()
        self.add_drug_ui.setupUi(self.add_drug_window, self)
        self.add_drug_window.show()

    def update_drug_list(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()
        cursor.execute("SELECT drug_name FROM Drug")
        drugs = cursor.fetchall()
        connection.close()

        # Clear existing items in the drug list widget
        self.drug_list_widget.clear()

        # Add new items to the drug list widget
        for drug in drugs:
            self.drug_list_widget.addItem(drug[0])
            
    def retranslateUi(self, drug_List):
        _translate = QtCore.QCoreApplication.translate
        drug_List.setWindowTitle(_translate("drug_List", "คลังยา"))
        self.label.setText(_translate("drug_List", "คลังยา"))
        self.add_back_pushButton.setText(_translate("drug_List", "ย้อนกลับ"))
        self.add_pushButton.setText(_translate("drug_List", "เพิ่มยา"))
              
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("medicine.db")
    if not db.open():
        print("Cannot establish a database connection.")
        sys.exit(1)
        
    drug_List = QtWidgets.QMainWindow()
    ui = Ui_drug_List()
    ui.setupUi(drug_List)
    drug_List.show()
    sys.exit(app.exec_())
