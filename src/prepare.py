from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import sqlite3

row_max = 5     # แถวของกล่องยา                                  # กำหนดจำนวน row ของยา
col_max = 8     # จำนวนลูกบอลที่ใส่ได้ในแต่ละแถว                      # กำหนดจำนวน col ของยา
current_ball_index = 0
class CircularColorItem(QtWidgets.QWidget):
    def __init__(self, color, text, parent=None):
        super().__init__(parent)
        self.color = color
        self.text = text["text"]
        self.enabled = text["enabled"]

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        if self.enabled:
            painter.setBrush(QtGui.QBrush(self.color))
        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(200, 200, 200)))  # You can adjust this color as needed
        painter.drawEllipse(self.rect())

        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)


class Ui_prepare(object):

    def setupUi(self, prepare):
        prepare.setObjectName("prepare")
        prepare.resize(683, 400)
        prepare.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(prepare)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -60, 683, 131))
        self.frame.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame.setGraphicsEffect(shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.prepare_label = QtWidgets.QLabel(self.frame)
        self.prepare_label.setGeometry(QtCore.QRect(200, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.prepare_label.setFont(font)
        self.prepare_label.setStyleSheet("border-radius: 16px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 110);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.prepare_label)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.prepare_label.setGraphicsEffect(shadow)
        self.prepare_label.setFrameShape(QtWidgets.QFrame.Box)
        self.prepare_label.setLineWidth(1)
        self.prepare_label.setTextFormat(QtCore.Qt.AutoText)
        self.prepare_label.setScaledContents(False)
        self.prepare_label.setAlignment(QtCore.Qt.AlignCenter)
        self.prepare_label.setWordWrap(True)
        self.prepare_label.setObjectName("prepare_label")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(230, 80, 37, 31))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/icons/sort_icon.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.add_back_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_back_pushButton.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_back_pushButton.setFont(font)
        self.add_back_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 212, 99);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.add_back_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.add_back_pushButton.setGraphicsEffect(shadow)
        self.add_back_pushButton.setObjectName("add_back_pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 80, 201, 301))
        self.frame_2.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_2)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_2.setGraphicsEffect(shadow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 181, 281))
        self.frame_3.setStyleSheet("border-radius: 9px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 161, 231))
        self.listWidget.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(250, 80, 401, 301))
        self.frame_4.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(236, 236, 236);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_4)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.frame_4.setGraphicsEffect(shadow)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.previous_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.previous_pushButton.setGeometry(QtCore.QRect(210, 5, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previous_pushButton.setFont(font)
        self.previous_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(115, 172, 131);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.previous_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.previous_pushButton.setGraphicsEffect(shadow)
        self.previous_pushButton.setObjectName("previous_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.next_pushButton.setGeometry(QtCore.QRect(300, 5, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setStyleSheet("border-radius: 9px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 151, 61);")
         # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.next_pushButton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.next_pushButton.setGraphicsEffect(shadow)
        self.next_pushButton.setObjectName("next_pushButton")

        prepare.setCentralWidget(self.centralwidget)

        # Set up the table widget
        self.setup_table_widget()

        # self.selected_ball_index = -1

        self.retranslateUi(prepare)
        QtCore.QMetaObject.connectSlotsByName(prepare)

        def close_window():
            prepare.close()
            
        self.add_back_pushButton.clicked.connect(close_window)

        # Set up button press and release styling
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))
        self.add_back_pushButton.released.connect(lambda: self.set_button_released_style(self.add_back_pushButton))

        self.next_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.next_pushButton))
        self.next_pushButton.released.connect(lambda: self.set_button_released_style(self.next_pushButton))

        self.previous_pushButton.pressed.connect(lambda: self.set_button_pressed_style2(self.previous_pushButton))
        self.previous_pushButton.released.connect(lambda: self.set_button_released_style2(self.previous_pushButton))

        # self.next_pushButton.clicked.connect(self.next_pushButton_clicked)                                                           ตรงนี้
        # self.add_back_pushButton.clicked.connect(self.add_back_pushButton_clicked)

        # self.previous_pushButton.clicked.connect(self.move_to_previous_ball)
        self.next_pushButton.clicked.connect(self.move_to_next_ball)

        self.sort_handle()

        # self.update_ball_colors()

    # def next_pushButton_clicked(self):
    #     global current_ball_index
    #     current_ball_index = (current_ball_index + 1) % (row_max * col_max)                                                          ตรงนี้
    #     self.sort_handle()

    # def add_back_pushButton_clicked(self):
    #     global current_ball_index
    #     current_ball_index = (current_ball_index - 1) % (row_max * col_max)
    #     self.sort_handle()
        
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

    def set_button_pressed_style2(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )

    def set_button_released_style2(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(115, 172, 131);"
        )

    # def move_to_previous_ball(self):
        # if self.selected_ball_index >= 0:
        #     self.selected_ball_index -= 1
        #     print(self.selected_ball_index)
            # self.update_ball_colors()
            # if self.selected_ball_index == -1:
            #     self.sort_handle()

    def move_to_next_ball(self):
        # if self.selected_ball_index < (row_max * col_max) - 1:
        print(self.slot)
        if self.slot <= (row_max * col_max):
            # self.selected_ball_index += 1
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
            
            # print(self.check_meal)
            cursor.execute(query, (self.check_meal,))   
            drug_info_list = cursor.fetchall()
            print(drug_info_list)
            
            if drug_info_list:
                self.check_all = 1
             
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
                self.tableWidget.setCellWidget(self.cursor_col, self.cursor_row, circular_item)
                
                
                print(drug_info_list[0][15])
                for drug_info in drug_info_list:
                    drug_id, drug_name, drug_description, drug_remaining, drug_remaining_meal, fraction, external_drug, internal_drug, drug_eat, all_drug_recieve, day_start, drug_log, drug_new, drug_size, meal_id, meal_name, time = drug_info
                    
                    if external_drug != 0:
                        print(f"- {drug_name}")
                        
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
                    self.slot = (row_max * col_max) + 1
                else:
                    # print("ยังมียาที่ยังไม่หมด")
                    pass
                    
                # print("============================================================================")
                
                if have_drug:                                           # เช็คว่ามียาไหม
                    self.slot += 1
                    self.cursor_row += 1

                    # Update listWidget with medicine names and meal times for the current ball
                    current_drug_info = drug_info_list[current_ball_index]

                    drug_name = current_drug_info[1]

                    self.listWidget.clear()
                    self.listWidget.addItem(f"กรุณากดปุ่มถัดไปเพื่อจัดเรียงยา")
                    
                row_new = (col_max - row_max) - 1
                col_new = (row_max - col_max) - 1
                
                if self.cursor_row > row_max + row_new:                      # คำนวณตำแหน่งของ row
                    self.cursor_row = 0
                    self.cursor_col += 1
                if self.cursor_col > col_max + col_new:                      # คำนวณตำแหน่งของ col
                    self.cursor_col = 0
                self.check_meal += 1
            
            else:
                # print(f"check all:{self.check_all}")
                if self.check_all == 7:
                    # QtWidgets.QMessageBox.warning(self.centralwidget, "คำเตือน", "ไม่พบข้อมูลยา")
                    return
                    # เพิ่มกลับไปหน้า main ด้วย
                self.check_all += 1
                self.check_meal += 1
                self.move_to_next_ball()
                return
                
            if self.check_meal > 7:
                self.check_meal = 1
            
            connection.close()
            
            # print(self.selected_ball_index)
            # self.update_ball_colors()

    def setup_table_widget(self):
        # สร้างและกำหนด QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 120, 381, 251))                         
        self.tableWidget.setObjectName("tableWidget")

        # Set the background color of the table to white and text color to black
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        shadow = QGraphicsDropShadowEffect(self.tableWidget)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(0,2)
        self.tableWidget.setGraphicsEffect(shadow)


        # กำหนดหัวข้อคอลัมน์ในตาราง
        self.tableWidget.setColumnCount(col_max)
        # self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6"])
        
        # กำหนดจำนวนแถวในตารางตามจำนวนรายการยาที่ดึงมาจากฐานข้อมูล
        self.tableWidget.setRowCount(row_max)

        cell_size = 45  # You can adjust this value as needed
        for col_idx in range(col_max):
            self.tableWidget.setColumnWidth(col_idx, cell_size)
        for row_idx in range(row_max):
            self.tableWidget.setRowHeight(row_idx, cell_size)
                 
                
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

          
        connection.close()
        
        self.check_meal = 1
        self.slot = 1
        
        self.cursor_row = 0
        self.cursor_col = 0
        self.check_all = 1

    def retranslateUi(self, prepare):
        _translate = QtCore.QCoreApplication.translate
        prepare.setWindowTitle(_translate("prepare", "เตรียมบอล"))
        self.prepare_label.setText(_translate("prepare", "เตรียมบอล"))
        self.add_back_pushButton.setText(_translate("prepare", "ย้อนกลับ"))
        self.label.setText(_translate("prepare", "รายชื่อยาที่ต้องเตรียม"))
        self.label_2.setText(_translate("prepare", "วางตามช่องที่แสดง"))
        self.next_pushButton.setText(_translate("prepare", "ถัดไป"))
        self.previous_pushButton.setText(_translate("prepare", "ก่อนหน้า"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prepare = QtWidgets.QMainWindow()
    ui = Ui_prepare()
    ui.setupUi(prepare) 
    prepare.show()
    sys.exit(app.exec_())




