from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

from prepare import Ui_prepare

row_max = 5     # แถวของกล่องยา                                  # กำหนดจำนวน row ของยา
col_max = 8     # จำนวนลูกบอลที่ใส่ได้ในแต่ละแถว                      # กำหนดจำนวน col ของยา

class CircularColorItem(QtWidgets.QWidget):
    def __init__(self, color, text, parent=None):
        super().__init__(parent)
        self.color = color
        self.text = text["text"]
        self.enabled = text["enabled"]

    def paintEvent(self, event):
        width, height = Scale_Width_Height()
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        if self.enabled:
            painter.setBrush(QtGui.QBrush(self.color))
        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(200, 200, 200)))  # You can adjust this color as needed
        painter.drawEllipse(self.rect())

        font = painter.font()
        font.setPointSize(int(8 * height))
        painter.setFont(font)
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)

class Ui_sortDrug(object):
    def setupUi(self, sortDrug):
        UI_instance.Set(sortDrug)
        show_widget_fullscreen(sortDrug)

        sortDrug.setObjectName("sortDrug")
        sortDrug.resize(int(683 * width), int(400 * height))
        sortDrug.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(sortDrug)
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
        self.sort_label = QtWidgets.QLabel(self.frame)
        self.sort_label.setGeometry(QtCore.QRect(int(200 * width), int(70 * height), int(281 * width), int(51 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(14 * height))
        font.setBold(True)
        font.setWeight(int(75 * width))
        self.sort_label.setFont(font)
        self.sort_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.sort_label)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.sort_label.setGraphicsEffect(shadow)
        self.sort_label.setFrameShape(QtWidgets.QFrame.Box)
        self.sort_label.setLineWidth(int(1 * width))
        self.sort_label.setTextFormat(QtCore.Qt.AutoText)
        self.sort_label.setScaledContents(False)
        self.sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_label.setWordWrap(True)
        self.sort_label.setObjectName("sort_label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(int(230 * width), int(80 * height), int(37 * width), int(31 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/sort_icon.png"))
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
        self.next_pushButton = QtWidgets.QPushButton(self.frame)
        self.next_pushButton.setGeometry(QtCore.QRect(int(540 * width), int(80 * height), int(71 * width), int(31 * height)))
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
#         self.frame_2 = QtWidgets.QFrame(self.centralwidget)
#         self.frame_2.setGeometry(QtCore.QRect(80, 90, 521, 291))
#         self.frame_2.setStyleSheet("border-radius: 16px;\n"
# "background-color: rgb(236, 236, 236);")
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
        sortDrug.setCentralWidget(self.centralwidget)

        # Set up the table widget
        self.setup_table_widget()

        self.retranslateUi(sortDrug)
        QtCore.QMetaObject.connectSlotsByName(sortDrug)
            
        self.add_back_pushButton.clicked.connect(self.homepage)

        self.next_pushButton.clicked.connect(self.open_prepare)
        
        self.sort_handle()

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
    def homepage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def open_prepare(self):
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_prepare)

    def setup_table_widget(self):
        width, height = Scale_Width_Height()
        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(int(99 * width), int(76 * height), int(483 * width), int(316 * height)))                         
        self.tableWidget.setObjectName("tableWidget")

        # Set the background color of the table to white and text color to black
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        shadow = QGraphicsDropShadowEffect(self.tableWidget)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.tableWidget.setGraphicsEffect(shadow)

        self.img_in_label = QtWidgets.QLabel(self.centralwidget)
        self.img_in_label.setGeometry(QtCore.QRect(int(603 * width), int(225 * height), int(33 * width), int(31 * height)))
        self.img_in_label.setText("")
        self.img_in_label.setPixmap(QtGui.QPixmap(":/image/sort_in.png"))
        self.img_in_label.setScaledContents(True)
        self.img_in_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_in_label.setObjectName("img_in_label")

        self.in_label = QtWidgets.QLabel(self.centralwidget)
        self.in_label.setGeometry(QtCore.QRect(int(605 * width), int(195 * height), int(281 * width), int(30 * height)))
        self.in_label.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(True)
        font.setWeight(int(25 * width))
        self.in_label.setFont(font)

        self.img_out_label = QtWidgets.QLabel(self.centralwidget)
        self.img_out_label.setGeometry(QtCore.QRect(int(40 * width), int(225 * height), int(33 * width), int(31 * height)))
        self.img_out_label.setText("")
        self.img_out_label.setPixmap(QtGui.QPixmap(":/image/sort_out.png"))
        self.img_out_label.setScaledContents(True)
        self.img_out_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_out_label.setObjectName("img_in_label")

        self.out_label = QtWidgets.QLabel(self.centralwidget)
        self.out_label.setGeometry(QtCore.QRect(int(47 * width), int(195 * height), int(50 * width), int(30 * height)))
        self.out_label.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        font.setBold(True)
        font.setWeight(int(25 * width))
        self.out_label.setFont(font)


        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(col_max)
        # self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(row_max)

        cell_size = 80  # You can adjust this value as needed
        for col_idx in range(col_max):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(row_max):
            self.tableWidget.setRowHeight(row_idx, cell_size)
            
        # color_text_mapping = {
        #         (255, 255, 102): "เช้าก่อน",    # สีเหลือง
        #         (255, 192, 203): "เช้าหลัง",    # สีชมพู
        #         (178, 255, 102): "เที่ยงก่อน",   # สีเขียว
        #         (255, 178, 102): "เที่ยงหลัง",   # สีส้ม
        #         (102, 255, 255): "เย็นก่อน",    # สีฟ้า
        #         (204, 153, 255): "เย็นหลัง",    # สีม่วง
        #         (255, 102, 102): "ก่อนนอน"    # สีแดง
        #     }
            
        # color_index = 0
        
        # for row in range(row_max):
        #     for col in range(col_max):
        #         # color = (255, 255, 0)  # Default color is yellow
        #         print(f"color_index: {color_index}")
                
        #         if color_index < len(color_text_mapping):
        #             color = list(color_text_mapping.keys())[color_index]
        #             print(f"color: {color}")

        #         circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping[color])
        #         self.tableWidget.setCellWidget(row, col, circular_item)
                
        #         # print(circular_item)

        #         color_index = (color_index + 1) % len(color_text_mapping)  # Rotate colors
                
                
                
    def sort_handle(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        query = '''
        SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, 
                h.meal_id, meal_name, time
            FROM Drug_handle AS h
            LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
            LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
        '''

        cursor.execute(query)
        drug_info_list = cursor.fetchall()
        

        for drug_info in drug_info_list:
            drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, meal_id, meal_name, time = drug_info

            
            drug_remaining_meal = drug_remaining / drug_eat                 # คำนวณจำนวนมื้อทั้งหมดที่คงเหลือทั้งหมด
            drug_remaining_meal = int(drug_remaining_meal)                  # แปลงเป็นจำนวนเต็ม
            
            fraction = drug_remaining % drug_eat                            # คำนวณจำนวนเศษยาที่ไม่ลงตัวกับจำนวนยาที่กิน
            
            external_drug = int(drug_remaining_meal)                        # แปลงเป็นจำนวนเต็ม
            
            # Update external_drug with drug_remaining
            cursor.execute(f"UPDATE Drug SET drug_remaining_meal = {drug_remaining_meal}, fraction = {fraction}, external_drug = {external_drug}, internal_drug = 0 WHERE drug_id = {drug_id}")
            connection.commit()

            # Fetch updated drug information after the update
            cursor.execute(f"SELECT * FROM Drug WHERE drug_id = {drug_id}")
            updated_drug_info = cursor.fetchone()
            drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size = updated_drug_info

            # Display updated drug and meal information
            # print(f"Drug: {drug_id}, {drug_name}, {drug_description}, {drug_remaining}, {drug_remaining_meal}, {fraction}, {external_drug}, {internal_drug}, {drug_eat}, {all_drug_recieve}, {day_start}, {drug_log}")
            # print(f"Meal: {meal_id}, {meal_name}, {time}")
            # print(f"ยา: {drug_name} และรับประทาน{meal_name}")
            # print("=============================================================================")
        # print("\n")
        connection.close()
        
        check_meal = 1
        slot = 1
        
        cursor_row = 0
        cursor_col = 0
        check_all = 1
        while(slot <= row_max * col_max):
            connection = sqlite3.connect("medicine.db")
            cursor = connection.cursor()
            query = '''
                SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
                        h.meal_id, meal_name, time
                    FROM Drug_handle AS h
                    LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                    LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
                WHERE h.meal_id = ?
                '''
            
            # print(check_meal)
            cursor.execute(query, (check_meal,))   
            drug_info_list = cursor.fetchall()
            
            if not drug_info_list:
                pass
                # print(f"check all:{check_all}")
                
                if check_all == 7:
                    QtWidgets.QMessageBox.warning(self.centralwidget, "คำเตือน", "ไม่พบข้อมูลยา")
                    return
                check_all += 1
                

            if drug_info_list:
                check_all = 1
                # print(f"ลำดับ: {slot}, ยา{drug_info_list[0][14]}\n")
                # print("ประกอบไปด้วย")
                have_drug = False
                
                color_text_mapping = {
                    (255, 102, 102): {"text": "เช้าก่อน", "enabled": True},    # สีแดง
                    (255, 178, 102): {"text": "เช้าหลัง", "enabled": True},   # สีส้ม
                    (255, 255, 102): {"text": "เที่ยงก่อน", "enabled": True},    # สีเหลือง
                    (178, 255, 102): {"text": "เที่ยงหลัง", "enabled": True},   # สีเขียวอ่อน
                    (102, 255, 102): {"text": "เย็นก่อน", "enabled": True},   # สีเขียวเข้ม
                    (102, 255, 255): {"text": "เย็นหลัง", "enabled": True},    # สีฟ้า
                    (0, 180, 255): {"text": "ก่อนนอน", "enabled": True}    # สีน้ำเงิน
                }

                color_index = drug_info_list[0][14] - 1

                if color_index < len(color_text_mapping):
                    color = list(color_text_mapping.keys())[color_index]

                circular_item = CircularColorItem(QtGui.QColor(*color), color_text_mapping[color])
                self.tableWidget.setCellWidget(cursor_col, cursor_row, circular_item)
                
                # print(drug_info_list)
                for drug_info in drug_info_list:
                    drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size, meal_id, meal_name, time = drug_info
                    
                    if external_drug != 0:
                        # print(f"- {drug_name}")
                        
                        # print(f"    มื้อยานอกเครื่อง:{external_drug} (ก่อน update)")
                        # print(f"    มื้อยาในเครื่อง:{internal_drug} (ก่อน update)")
                        # print("-----------------------")
                        
                        external_drug -= 1
                        internal_drug += 1
                        
                        cursor.execute(f"UPDATE Drug SET external_drug = {external_drug}, internal_drug = {internal_drug} WHERE drug_id = {drug_id}")
                        connection.commit()
                        
                        # print(f"    มื้อยานอกเครื่อง:{external_drug} (หลัง update)")
                        # print(f"    มื้อยาในเครื่อง:{internal_drug} (หลัง update)")
                        
                        have_drug = True
                        
                    else:
                        # print("     หมด")
                        pass
                        
                query = '''
                SELECT  h.drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size,
                        h.meal_id, meal_name, time
                    FROM Drug_handle AS h
                    LEFT JOIN Drug AS d ON h.drug_id = d.drug_id
                    LEFT JOIN Meal AS m ON h.meal_id = m.meal_id
                '''
                    
                cursor.execute(query)   
                drug_info_list = cursor.fetchall()
                
                
                for drug_info in drug_info_list:
                    drug_info[6] == 0
                    # print(f"\nชื่อยา:{drug_info[1]}\nยานอกเครื่อง:{drug_info[6]}\n")
            
                all_drugs_empty = all(drug_info[6] == 0 for drug_info in drug_info_list)

                if all_drugs_empty:
                    # print("ทุกยามยาหมดแล้ว")
                    slot = (row_max * col_max) + 1
                else:
                    # print("ยังมียาที่ยังไม่หมด")
                    pass
                    
                # print("============================================================================")
                
                if have_drug:                                           # เช็คว่ามียาไหม
                    slot += 1
                    cursor_row += 1
                
                row_new = (col_max - row_max) - 1
                col_new = (row_max - col_max) - 1
                
                if cursor_row > row_max + row_new:                      # คำนวณตำแหน่งของ row
                    cursor_row = 0
                    cursor_col += 1
                if cursor_col > col_max + col_new:                      # คำนวณตำแหน่งของ col
                    cursor_col = 0
                check_meal += 1
            
            else:
                check_meal += 1    
                
            if check_meal > 7:
                check_meal = 1
            
        connection.close()



    def retranslateUi(self, sortDrug):
        _translate = QtCore.QCoreApplication.translate
        sortDrug.setWindowTitle(_translate("sortDrug", "วิธีเรียงกล่องบรรจุยา"))
        self.add_back_pushButton.setText(_translate("sortDrug", "ย้อนกลับ"))
        self.sort_label.setText(_translate("sortDrug", "       วิธีเรียงกล่องบรรจุยา"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))
        self.in_label.setText(_translate("sortDrug", "เข้า"))
        self.out_label.setText(_translate("sortDrug", "ออก"))

import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sortDrug = QtWidgets.QMainWindow()
    ui = Ui_sortDrug()
    ui.setupUi(sortDrug)
    sortDrug.show()
    sys.exit(app.exec_())