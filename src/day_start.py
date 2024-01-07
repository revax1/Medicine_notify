from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3

from select_meal import Ui_select_meal

class Ui_day_start(object):
    def setupUi(self, day_start):
        UI_instance.Set(day_start)
        show_widget_fullscreen(day_start)
        
        self.day_start = day_start
        self.drug_List = drug_list_instance.Get()
        self.each_drug = each_drug_instance.Get()
        self.each_drug2 = each_drug_2_instance.Get()
        self.updated_data2 = drug_Update_2_instance.Get()
        
        day_start.setObjectName("day_start")
        day_start.resize(int(683 * width), int(400 * height))
        day_start.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(day_start)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(int(0 * width), int(-60 * height), int(683 * width), int(131 * height)))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.label.setGraphicsEffect(shadow)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(int(1 * width))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(238 * width), int(80 * height), int(31 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/each_icon.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(int(50 * width), int(80 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setGeometry(QtCore.QRect(int(510 * width), int(340 * height), int(81 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(int(155 * width), int(80 * height), int(361 * width), int(261 * height)))
        self.frame_2.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(236, 236, 236);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_date = QtWidgets.QLabel(self.frame_2)
        self.label_date.setGeometry(QtCore.QRect(int(80 * width), int(3 * height), int(211 * width), int(21 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.label_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(int(165 * width), int(110 * height), int(341 * width), int(221 * height)))
        self.calendarWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        day_start.setCentralWidget(self.centralwidget)
      
        
        self.calendarWidget.selectionChanged.connect(self.update_selected_date)

        # # Set the minimum date to the current date
        # current_date = QtCore.QDate.currentDate()
        # self.calendarWidget.setMinimumDate(current_date)

        self.retranslateUi(day_start)
        self.set_day_info(drug_ID_instance.Get())
        QtCore.QMetaObject.connectSlotsByName(day_start)

        self.add_back_pushButton.clicked.connect(self.backpage)

        def save_changes():
            updated_data2 = self.updated_data2

            # If the user hasn't selected a date, use the current date
            if not self.date_selected:
                current_date = QtCore.QDate.currentDate()
                self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))
                # Convert Thai numerals to Arabic numerals
                thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
                self.convert_to_arabic_numerals(thai_numerals)
                updated_data2['day_start'] = self.label_date.text()
            else:
                updated_data2['day_start'] = self.label_date.text()
                # Convert Thai numerals to Arabic numerals
                thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
                self.convert_to_arabic_numerals(thai_numerals)

            # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
            self.open_select_meal()

        # def save_changes():                                                                  แบบเดิม
        #     updated_data2 = self.updated_data2
        #     updated_data2['day_start'] = self.label_date.text()


        #     # ส่งข้อมูลที่ถูกแก้ไขไปยังหน้าต่อไป
        #     self.open_select_meal(self.updated_data2)
        
        self.next_pushButton.clicked.connect(save_changes)
        # self.next_pushButton.clicked.connect(self.closeAll)

        # Initialize variable to track if the date has been selected
        self.date_selected = False

         # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))

    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(227, 151, 61);"
        )


    def convert_to_arabic_numerals(self, thai_numerals):
        arabic_numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for thai, arabic in zip(thai_numerals, arabic_numerals):
            self.label_date.setText(self.label_date.text().replace(thai, arabic))

    def update_selected_date(self):
        selected_date = self.calendarWidget.selectedDate()
        # Update the label with the selected date
        self.label_date.setText(selected_date.toString("dddd d MMMM yyyy"))

        # Convert Thai numerals to Arabic numerals
        thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
        self.convert_to_arabic_numerals(thai_numerals)

        # Enable further date changes
        self.calendarWidget.setEnabled(True)

        # Update the variable to indicate that the date has been selected
        self.date_selected = True


        # # Check if the selected date is not in the past                                     แบบเดิมคือไม่สามารถเลือกวันที่ผ่านมาแล้วได้
        # if  selected_date >= QtCore.QDate.currentDate():
        #     self.label_date.setText(selected_date.toString("dddd d MMMM yyyy"))

        #     # Convert Thai numerals to Arabic numerals
        #     thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
        #     self.convert_to_arabic_numerals(thai_numerals)

        #     # Enable further date changes
        #     self.calendarWidget.setEnabled(True)
        #     # Update the variable to indicate that the date has been selected
        #     self.date_selected = True
        # else:
        #     # Show a warning message and reset the selected date
        #     QMessageBox.warning(self.centralwidget, "เลือกวัน", "ไม่สามารถเลือกวันที่ผ่านมาได้")
        #     self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())



        if not self.date_selected:                                                           #กรณีถ้าไม่ได้เลือก
            current_date = QtCore.QDate.currentDate()
            self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))

            # Convert Thai numerals to Arabic numerals
            thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
            self.convert_to_arabic_numerals(thai_numerals)

            self.calendarWidget.setEnabled(True)

           
        
    def backpage(self):
        from each_drug2 import Ui_each_drug2
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_each_drug2)


    def set_day_info(self, drug_id):
        self.drug_id = drug_id
        # print(f"day_start {self.updated_data2}")
        self.label.setText(f"{self.updated_data2['drug_name']}")

        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = connection.cursor()

        # Query to retrieve data from the database based on drug_id
        query = "SELECT day_start FROM Drug WHERE drug_id = ?"
        cursor.execute(query, (drug_id,))
        result = cursor.fetchone()

        if result:
            # Set the calendarWidget and label_date based on the retrieved data
            selected_date = QtCore.QDate.fromString(result[0], "dddd d MMMM yyyy")
            self.calendarWidget.setSelectedDate(selected_date)
            self.label_date.setText(selected_date.toString("dddd d MMMM yyyy"))

            # Convert Thai numerals to Arabic numerals
            thai_numerals = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
            self.convert_to_arabic_numerals(thai_numerals)

            # Enable further date changes
            self.calendarWidget.setEnabled(True)

            # Update the variable to indicate that the date has been selected
            self.date_selected = True

        connection.close()

    def open_select_meal(self):
        if self.date_selected:
            # Save the selected date to the database
            selected_date = self.calendarWidget.selectedDate().toString("dddd d MMMM yyyy")
            # self.save_date_to_database(selected_date, self.drug_id) คอมเมนต์เพื่อไม่ให้บันทึกวันลงในฐานข้อมูล

            # Open the select_meal window
            drug_Update_2_instance.Set(self.updated_data2)
            day_start_instance.Set(self)
            each_drug_2_instance.Set(self.each_drug2)
            each_drug_instance.Set(self.each_drug)
            drug_list_instance.Set(self.drug_List)

            select_meal_form = UI_Genarate()
            select_meal_form.widgetSet(UI_instance.Get(), Ui_select_meal)

            self.calendarWidget.setEnabled(True)
        else:
            # Save the selected date to the database
            selected_date = self.calendarWidget.selectedDate().toString("dddd d MMMM yyyy")
            # self.save_date_to_database(selected_date, self.drug_id) คอมเมนต์เพื่อไม่ให้บันทึกวันลงในฐานข้อมูล

            # Open the select_meal window
            drug_Update_2_instance.Set(self.updated_data2)
            day_start_instance.Set(self)
            each_drug_2_instance.Set(self.each_drug2)
            each_drug_instance.Set(self.each_drug)
            drug_list_instance.Set(self.drug_List)

            select_meal_form = UI_Genarate()
            select_meal_form.widgetSet(UI_instance.Get(), Ui_select_meal)

            self.calendarWidget.setEnabled(True)

            # QMessageBox.warning(self.centralwidget, "เลือกวัน", "กรุณาเลือกวันก่อนดำเนินการถัดไป")
            
    def closeAll(self):
        self.each_drug.closeAll()
        self.each_drug2.closeAll()
        self.day_start.close()  # ปิดหน้าต่างที่เป็นส่วนสมาชิกของ Ui_med_pack2
    
    def save_date_to_database(self, selected_date, drug_id):
        # Connect to SQLite database
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
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
        current_date = QtCore.QDate.currentDate()
        self.label_date.setText(current_date.toString("dddd d MMMM yyyy"))
        # self.label_date.setText("เลือกวันที่เริ่มรับประทานยา")          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    day_start = QtWidgets.QMainWindow()
    ui = Ui_day_start()
    ui.setupUi(day_start)
    day_start.show()
    sys.exit(app.exec_())