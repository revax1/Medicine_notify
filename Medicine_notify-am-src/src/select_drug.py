from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QTimeEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QLocale
import sqlite3

class Ui_select_drug(object):
    def setupUi(self, select_drug):
        select_drug.setObjectName("select_drug")
        select_drug.resize(531, 401)
        select_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(select_drug)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 110, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.drug_timing_label = QtWidgets.QLabel(self.centralwidget)
        self.drug_timing_label.setGeometry(QtCore.QRect(140, 30, 220, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drug_timing_label.setFont(font)
        self.drug_timing_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.drug_timing_label.setFrameShape(QtWidgets.QFrame.Box)
        self.drug_timing_label.setLineWidth(1)
        self.drug_timing_label.setTextFormat(QtCore.Qt.AutoText)
        self.drug_timing_label.setScaledContents(False)
        self.drug_timing_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drug_timing_label.setWordWrap(True)
        self.drug_timing_label.setObjectName("drug_timing_label")
        self.select_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.select_back_pushButton.setGeometry(QtCore.QRect(10, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_back_pushButton.setFont(font)
        self.select_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.select_back_pushButton.setObjectName("select_back_pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 41, 41))
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
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 130, 20, 621))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(290, 210, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.select_drug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.select_drug_pushButton.setGeometry(QtCore.QRect(80, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_drug_pushButton.setFont(font)
        self.select_drug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_drug_pushButton.setObjectName("select_drug_pushButton")
        self.drugHave_label = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label.setGeometry(QtCore.QRect(280, 140, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugHave_label.setFont(font)
        self.drugHave_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label.setObjectName("drugHave_label")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 210, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_2.setLineWidth(1)
        self.listWidget_2.setObjectName("listWidget_2")
        self.drugHave_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label_2.setGeometry(QtCore.QRect(-10, 140, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugHave_label_2.setFont(font)
        self.drugHave_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label_2.setObjectName("drugHave_label_2")
        self.add_drug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_drug_pushButton.setGeometry(QtCore.QRect(370, 360, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_drug_pushButton.setFont(font)
        self.add_drug_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 179, 85);")
        self.add_drug_pushButton.setObjectName("add_drug_pushButton")
        self.drugHave_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label_3.setGeometry(QtCore.QRect(290, 320, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.drugHave_label_3.setFont(font)
        self.drugHave_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label_3.setObjectName("drugHave_label_3")
        
        # Add the "เวลาจ่ายยา" button
        self.set_time_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_time_button.setGeometry(QtCore.QRect(400, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_time_button.setFont(font)
        self.set_time_button.setStyleSheet("background-color: rgb(81, 179, 85); color:white")
        self.set_time_button.setObjectName("set_time_button")
        self.set_time_button.setText("เวลาจ่ายยา")
        
        # Add QLabel to display selected time
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(355, 100, 170, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        
        select_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_drug)
        QtCore.QMetaObject.connectSlotsByName(select_drug)
        
        # Connect to SQLite database
        self.connection = sqlite3.connect("medicine.db")
        self.cursor = self.connection.cursor()

        # กดปุ่มเพิ่มยา
        self.add_drug_pushButton.clicked.connect(self.open_add_drug_page)
        
        # ปุ่มย้อนกลับ
        def close_window():
            select_drug.close()
        self.select_back_pushButton.clicked.connect(close_window)
        self.select_drug_pushButton.clicked.connect(self.add_selected_drug)
        
        self.load_all_drugs()  # โหลดยาทั้งหมดจาก checkbox
        
        # Connect the "เวลาจ่ายยา" button to the open_time_picker method
        self.set_time_button.clicked.connect(self.open_time_picker)
        
    def load_all_drugs(self):
        # Retrieve all drugs from the 'Drug' table
        query = "SELECT drug_id, drug_name FROM Drug"
        drugs = self.cursor.execute(query).fetchall()

        # Clear the list before adding new items
        self.listWidget_2.clear()

        # Display drug data in the list
        for drug_id, drug_name in drugs:
            checkbox_item = QtWidgets.QListWidgetItem(drug_name)
            checkbox = QtWidgets.QCheckBox(drug_name)
            checkbox_item.setSizeHint(QtCore.QSize(200, 30))
            self.listWidget_2.addItem(checkbox_item)
            self.listWidget_2.setItemWidget(checkbox_item, checkbox)
    
    def get_selected_drugs(self):
        selected_drugs = []
        for index in range(self.listWidget_2.count()):
            checkbox_item = self.listWidget_2.item(index)
            checkbox = self.listWidget_2.itemWidget(checkbox_item)
            if checkbox.isChecked():
                selected_drugs.append(checkbox_item.text())
        return selected_drugs

    def add_selected_drug(self):
        # Clear the 'รายการยาของมื้อนี้' list
        self.listWidget.clear()

        # Get the selected drugs from the 'เลือกรายการยาที่ต้องการ' list
        selected_drugs = self.get_selected_drugs()

        # Add the selected drugs to the 'รายการยาของมื้อนี้' list
        for drug in selected_drugs:
            self.listWidget.addItem(drug)
        
    def open_add_drug_page(self):
        from addDrug import Ui_Add_drug  # ชื่อไฟล์ของ UI ของหน้า 'เพิ่มยา'
        self.add_drug_window = QtWidgets.QMainWindow()
        self.add_drug_ui = Ui_Add_drug()
        self.add_drug_ui.setupUi(self.add_drug_window)

        self.add_drug_window.show()
        
    def set_drug_timing(self, text):
        self.drug_timing_label.setText(text)
        
    def open_time_picker(self):
        # Create a time picker dialog
        time_dialog = TimePickerDialog()

        # Show the dialog and get the selected time
        if time_dialog.exec_():
            selected_time = time_dialog.selected_time()

            # Set the locale to Thai
            thai_locale = QLocale(QLocale.Thai)
            selected_time_string = thai_locale.toString(selected_time, "h:mm")

            print("เวลาที่เลือก:", selected_time_string)

            # Display the selected time above the "เวลาจ่ายยา" button
            self.time_label.setText("เวลาที่เลือก: " + selected_time_string + " น.")

            # Insert the selected time into the 'Drug_Meal' table
            selected_time_for_sql = selected_time.toString("HH:mm")
            self.cursor.execute('''
                INSERT INTO Meal (time) VALUES (?)
            ''', (selected_time_for_sql,))
            self.connection.commit()  # Commit the changes to the database

    def retranslateUi(self, select_drug):
        _translate = QtCore.QCoreApplication.translate
        select_drug.setWindowTitle(_translate("select_drug", "เลือกมื้อยา"))
        self.select_back_pushButton.setText(_translate("select_drug", "ย้อนกลับ"))
        self.select_drug_pushButton.setText(_translate("select_drug", "ยืนยัน"))
        self.drugHave_label.setText(_translate("select_drug", "รายการยาของมื้อนี้"))
        self.drugHave_label_2.setText(_translate("select_drug", "เลือกรายการยาที่ต้องการ"))
        self.add_drug_pushButton.setText(_translate("select_drug", "เพิ่มยา"))
        self.drugHave_label_3.setText(_translate("select_drug", "หากไม่มียาที่ต้องการ กดปุ่มด้านล่างนี้"))
import resources_rc

class TimePickerDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("เลือกเวลาจ่ายยา")

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTime(QtCore.QTime.currentTime())

        self.confirm_button = QPushButton("ตกลง")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.time_edit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def selected_time(self):
        return self.time_edit.time()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Set the locale to English
    english_locale = QLocale(QLocale.English)
    QLocale.setDefault(english_locale)

    select_drug = QtWidgets.QMainWindow()
    ui = Ui_select_drug()
    ui.setupUi(select_drug)
    select_drug.show()
    sys.exit(app.exec_())