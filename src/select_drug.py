from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_select_drug(object):
    def setupUi(self, select_drug):
        select_drug.setObjectName("select_drug")
        select_drug.resize(1105, 835)
        select_drug.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(select_drug)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.drug_timing_label = QtWidgets.QLabel(self.centralwidget)
        self.drug_timing_label.setGeometry(QtCore.QRect(320, 50, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
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
        self.select_back_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_back_pushButton.setFont(font)
        self.select_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.select_back_pushButton.setObjectName("select_back_pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 41, 41))
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
        self.select_drug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.select_drug_pushButton.setGeometry(QtCore.QRect(210, 730, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_drug_pushButton.setFont(font)
        self.select_drug_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_drug_pushButton.setObjectName("select_drug_pushButton")
        self.drugHave_label = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label.setGeometry(QtCore.QRect(740, 220, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.drugHave_label.setFont(font)
        self.drugHave_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label.setObjectName("drugHave_label")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(80, 290, 411, 411))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_2.setLineWidth(1)
        self.listWidget_2.setObjectName("listWidget_2")
        self.drugHave_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label_2.setGeometry(QtCore.QRect(110, 220, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.drugHave_label_2.setFont(font)
        self.drugHave_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label_2.setObjectName("drugHave_label_2")
        
        self.add_drug_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_drug_pushButton.setGeometry(QtCore.QRect(780, 760, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_drug_pushButton.setFont(font)
        self.add_drug_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 179, 85);")
        self.add_drug_pushButton.setObjectName("add_drug_pushButton")
        
        self.drugHave_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.drugHave_label_3.setGeometry(QtCore.QRect(670, 720, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugHave_label_3.setFont(font)
        self.drugHave_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.drugHave_label_3.setObjectName("drugHave_label_3")
        select_drug.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_drug)
        QtCore.QMetaObject.connectSlotsByName(select_drug)
        
        select_drug.showFullScreen()
        
        # กดปุ่มเพิ่มยา
        self.add_drug_pushButton.clicked.connect(self.open_add_drug_page)
        
        # ปุ่มย้อนกลับ
        def close_window():
            select_drug.close()
        self.select_back_pushButton.clicked.connect(close_window)
        self.select_drug_pushButton.clicked.connect(self.add_selected_drug)
        
        self.load_all_drugs()  # โหลดยาทั้งหมดจาก checkbox
        
    def load_all_drugs(self):
        # Connect to MongoDB
        client = pymongo.MongoClient()
        db = client["Medicine-Notify"]
        col = db["Drug"]

        # Retrieve all drugs from the collection
        drugs = col.find()

        # Clear the list before adding new items
        self.listWidget_2.clear()

        # Display drug data in the list
        for drug in drugs:
            drug_name = drug.get("name", "ไม่มีชื่อยา")
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_drug = QtWidgets.QMainWindow()
    ui = Ui_select_drug()
    ui.setupUi(select_drug)
    select_drug.show()
    sys.exit(app.exec_())