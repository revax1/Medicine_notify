from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
import sys
import Adafruit_PCA9685

from AddDrug_New import Ui_Add_drug
from each_drug import Ui_each_drug
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
# from select_meal import Ui_select_meal

class Ui_drug_List(object):       
    def setupUi(self, drug_List):
        self.state_file = '/home/pi/Documents/Medicine_notify/state/servo_state.txt'
        # self.servo_min = 150
        # self.servo_max = 600
        # self.pwm = Adafruit_PCA9685.PCA9685()
        
        UI_instance.Set(drug_List)
        show_widget_fullscreen(drug_List)

        self.drug_List = drug_List
        drug_List.setObjectName("drug_List")
        drug_List.resize(int(683 * width), int(400 * height))
        drug_List.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(drug_List)
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
        self.img_label.setGeometry(QtCore.QRect(int(285 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/druglist_icon.png"))
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
        self.add_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_pushButton.setGeometry(QtCore.QRect(int(530 * width), int(80 * height), int(71 * width), int(31 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_pushButton)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.add_pushButton.setGraphicsEffect(shadow)
        self.add_pushButton.setObjectName("add_pushButton")
        drug_List.setCentralWidget(self.centralwidget)

        self.retranslateUi(drug_List)
        QtCore.QMetaObject.connectSlotsByName(drug_List)

        self.drug_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.drug_list_widget.setGeometry(QtCore.QRect(int(100 * width), int(90 * height), int(491 * width), int(261 * height)))
        self.drug_list_widget.setStyleSheet("border-radius: 4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(226, 226, 226);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.drug_list_widget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.drug_list_widget.setGraphicsEffect(shadow)
        self.update_drug_list()  # เรียกใช้ฟังก์ชันเพื่อแสดงรายการยาในคลังยา

        # Connect the itemClicked signal to handle_drug_item_click method
        self.drug_list_widget.itemClicked.connect(self.handle_drug_item_click) #คลิกชื่อยาแล้วเปิดหน้าeach_drug
            
        # self.add_back_pushButton.clicked.connect(self.open_drug_list_again)
        self.add_back_pushButton.clicked.connect(self.backpage)
            
        self.add_pushButton.clicked.connect(self.open_add_drug)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.add_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_pushButton))
        self.add_pushButton.released.connect(lambda: self.set_button_released_style(self.add_pushButton))

    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 170, 127);"
        )


    # def handle_drug_item_click(self, item):
    #     drug_item_form = UI_Genarate()
    #     drug_item_form.widgetSet(UI.Get(), Ui_each_drug)

    #     drug_List_Data().Set(self)

    #     # Get the text of the clicked item (drug name)
    #     drug_name = item.text()
    #     self.each_drug_ui = Ui_each_drug() 
        
    #     # Set drug info for the each_drug window
    #     self.each_drug_ui.set_drug_info(drug_name)

    #     # Pass the drug name to the each_drug window
    #     self.each_drug_ui.label.setText(drug_name)

    def handle_drug_item_click(self, item):
        
        # Get the text of the clicked item (drug name)
        drug_list_instance.Set(self)
        drug_name_instance.Set(item.text())

        drug_item_form = UI_Genarate()
        drug_item_form.widgetSet(UI_instance.Get(), Ui_each_drug)       

    def backpage(self):
        
        # cur_col, cur_row, servoNum = self.load_state()
        # self.pwm.set_pwm(servoNum, 0, self.servo_max)
        # self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)
        
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def open_add_drug(self):
        add_drug_form = UI_Genarate()
        add_drug_form.widgetSet(UI_instance.Get(), Ui_Add_drug)
        
    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                content = f.read().split(',')
                state = (int(content[0]), int(content[1]), int(content[2]))
                # print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
                return state
        return 0, 0, 0  # default values if the file doesn't exist

    def update_drug_list(self):
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
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
        self.label.setText(_translate("drug_List", "     คลังยา"))
        self.add_back_pushButton.setText(_translate("drug_List", "ย้อนกลับ"))
        self.add_pushButton.setText(_translate("drug_List", "เพิ่มยา"))
              
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("/home/pi/Documents/Medicine_notify/db/medicine.db")
    if not db.open():
        print("Cannot establish a database connection.")
        sys.exit(1)
        
    drug_List = QtWidgets.QMainWindow()
    ui = Ui_drug_List()
    ui.setupUi(drug_List)
    drug_List.show()
    sys.exit(app.exec_())
