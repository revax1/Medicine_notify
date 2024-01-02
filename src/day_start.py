from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
from select_meal import Ui_select_meal
from PyQt5.QtCore import QLocale
import sqlite3

class Ui_day_start(object):
    def setupUi(self, day_start, drug_List, each_drug, each_drug2):
        self.day_start = day_start
        self.drug_List = drug_List
        self.each_drug = each_drug
        self.each_drug2 = each_drug2
        
        day_start.setObjectName("day_start")
        day_start.resize(531, 401)
        day_start.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(day_start)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 320, 51))
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(420, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.next_pushButton.setObjectName("next_pushButton")
        day_start.setCentralWidget(self.centralwidget)

        self.calendar_widget = QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(125, 105, 271, 191))
        self.calendar_widget.setObjectName("calendarWidget")

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(125, 320, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")

        self.calendar_widget.selectionChanged.connect(self.update_selected_date)

        self.retranslateUi(day_start)
        QtCore.QMetaObject.connectSlotsByName(day_start)

        def close_window():
            day_start.close()

        self.add_back_pushButton.clicked.connect(close_window)

        self.next_pushButton.clicked.connect(self.open_select_meal)

        # Initialize variable to track if the date has been selected
        self.date_selected = False

    def update_selected_date(self):
        english_locale = QLocale(QLocale.English)
        QLocale.setDefault(english_locale)
        selected_date = self.calendar_widget.selectedDate()
        
        # Convert the selected date to the desired format
        formatted_date = selected_date.toString("dd-MM-yyyy")
        # Set the label text to the formatted date
        self.label_date.setText(formatted_date)
        # Enable further date changes
        self.calendar_widget.setEnabled(True)
        # Update the variable to indicate that the date has been selected
        self.date_selected = True

    def set_day_info(self, drug_id):
        self.drug_id = drug_id

    def open_select_meal(self):
        if self.date_selected:
            # Save the selected date to the database
            selected_date = self.calendar_widget.selectedDate().toString("dd/MM/yyyy")
            self.save_date_to_database(selected_date, self.drug_id)

            # Open the select_meal window
            self.select_meal_window = QtWidgets.QMainWindow()
            self.select_meal_ui = Ui_select_meal()
            self.select_meal_ui.setupUi(self.select_meal_window, self.drug_List, self.each_drug, self.each_drug2, self)
            self.select_meal_ui.set_meal_info(self.drug_id)
            self.select_meal_window.show()

            # Disable the calendar after proceeding
            self.calendar_widget.setEnabled(False)
        else:
            QMessageBox.warning(self.centralwidget, "เลือกวัน", "กรุณาเลือกวันก่อนดำเนินการถัดไป")
            
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.day_start.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2
    
    def save_date_to_database(self, selected_date, drug_id):
        # Connect to SQLite database
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        # Check if a record already exists
        cursor.execute("SELECT * FROM Drug")
        existing_record = cursor.fetchall()
        # print(existing_record)

        if existing_record:
            # Update the existing record
            cursor.execute("UPDATE Drug SET day_start = ? WHERE drug_id = ?", (selected_date, drug_id))
        
        # Commit changes and close connection
        connection.commit()
        connection.close()

    def retranslateUi(self, day_start):
        _translate = QtCore.QCoreApplication.translate
        day_start.setWindowTitle(_translate("day_start", "วันที่เริ่มรับประทานยา"))
        self.label.setText(_translate("day_start", "วันที่เริ่มรับประทานยา"))
        self.add_back_pushButton.setText(_translate("day_start", "ย้อนกลับ"))
        self.next_pushButton.setText(_translate("day_start", "ถัดไป"))
        self.label_date.setText("เลือกวันที่เริ่มรับประทานยา")          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    day_start = QtWidgets.QMainWindow()
    ui = Ui_day_start()
    ui.setupUi(day_start)
    day_start.show()
    sys.exit(app.exec_())