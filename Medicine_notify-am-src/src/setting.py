from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_setting(object):
    def setupUi(self, setting):
        self.setting = setting  # Store the setting object as an instance variable
        setting.setObjectName("setting")
        setting.resize(531, 401)
        setting.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        self.setting_label = QtWidgets.QLabel(self.centralwidget)
        self.setting_label.setGeometry(QtCore.QRect(170, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.setting_label.setFont(font)
        self.setting_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setting_label.setFrameShape(QtWidgets.QFrame.Box)
        self.setting_label.setLineWidth(1)
        self.setting_label.setTextFormat(QtCore.Qt.AutoText)
        self.setting_label.setScaledContents(False)
        self.setting_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setting_label.setWordWrap(True)
        self.setting_label.setObjectName("setting_label")
        self.setting_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.setting_icon_label.setGeometry(QtCore.QRect(180, 30, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.setting_icon_label.setFont(font)
        self.setting_icon_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setting_icon_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setting_icon_label.setLineWidth(1)
        self.setting_icon_label.setText("")
        self.setting_icon_label.setTextFormat(QtCore.Qt.AutoText)
        self.setting_icon_label.setPixmap(QtGui.QPixmap(":/icons/setting_icon.png"))
        self.setting_icon_label.setScaledContents(True)
        self.setting_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setting_icon_label.setWordWrap(True)
        self.setting_icon_label.setObjectName("setting_icon_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 90, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.bb_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bb_checkBox.setGeometry(QtCore.QRect(20, 160, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_checkBox.sizePolicy().hasHeightForWidth())
        self.bb_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bb_checkBox.setFont(font)
        self.bb_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bb_checkBox.setText("")
        self.bb_checkBox.setTristate(False)
        self.bb_checkBox.setObjectName("bb_checkBox")
        self.ad_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ad_checkBox.setGeometry(QtCore.QRect(370, 250, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_checkBox.sizePolicy().hasHeightForWidth())
        self.ad_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ad_checkBox.setFont(font)
        self.ad_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ad_checkBox.setText("")
        self.ad_checkBox.setTristate(False)
        self.ad_checkBox.setObjectName("ad_checkBox")
        self.bd_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bd_checkBox.setGeometry(QtCore.QRect(370, 170, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bd_checkBox.sizePolicy().hasHeightForWidth())
        self.bd_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bd_checkBox.setFont(font)
        self.bd_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bd_checkBox.setText("")
        self.bd_checkBox.setTristate(False)
        self.bd_checkBox.setObjectName("bd_checkBox")
        self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.al_checkBox.setGeometry(QtCore.QRect(200, 240, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.al_checkBox.sizePolicy().hasHeightForWidth())
        self.al_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.al_checkBox.setFont(font)
        self.al_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.al_checkBox.setText("")
        self.al_checkBox.setTristate(False)
        self.al_checkBox.setObjectName("al_checkBox")
        self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bl_checkBox.setGeometry(QtCore.QRect(200, 160, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bl_checkBox.sizePolicy().hasHeightForWidth())
        self.bl_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bl_checkBox.setFont(font)
        self.bl_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bl_checkBox.setText("")
        self.bl_checkBox.setTristate(False)
        self.bl_checkBox.setObjectName("bl_checkBox")
        self.ab_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ab_checkBox.setGeometry(QtCore.QRect(20, 240, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ab_checkBox.sizePolicy().hasHeightForWidth())
        self.ab_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ab_checkBox.setFont(font)
        self.ab_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ab_checkBox.setText("")
        self.ab_checkBox.setTristate(False)
        self.ab_checkBox.setObjectName("ab_checkBox")
        self.bbed_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bbed_checkBox.setGeometry(QtCore.QRect(200, 340, 61, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbed_checkBox.sizePolicy().hasHeightForWidth())
        self.bbed_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bbed_checkBox.setFont(font)
        self.bbed_checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.bbed_checkBox.setText("")
        self.bbed_checkBox.setTristate(False)
        self.bbed_checkBox.setObjectName("bbed_checkBox")
        
        checkbox_style = """
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """

        # ใช้ StyleSheet ที่กำหนดไว้สำหรับทุก QCheckBox ที่มีอยู่ใน UI
        self.bb_checkBox.setStyleSheet(checkbox_style)
        self.ab_checkBox.setStyleSheet(checkbox_style)
        self.bl_checkBox.setStyleSheet(checkbox_style)
        self.al_checkBox.setStyleSheet(checkbox_style)
        self.bd_checkBox.setStyleSheet(checkbox_style)
        self.ad_checkBox.setStyleSheet(checkbox_style)
        self.bbed_checkBox.setStyleSheet(checkbox_style)
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 1201, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(170, 100, 20, 201))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 100, 20, 201))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.bb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bb_pushButton.setEnabled(False)
        self.bb_pushButton.setGeometry(QtCore.QRect(50, 180, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bb_pushButton.sizePolicy().hasHeightForWidth())
        self.bb_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setAutoFillBackground(False)
        self.bb_pushButton.setStyleSheet("background-color: rgb(255, 198, 199);")
        self.bb_pushButton.setObjectName("bb_pushButton")
        self.ab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ab_pushButton.setEnabled(False)
        self.ab_pushButton.setGeometry(QtCore.QRect(50, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("background-color: rgb(255, 232, 194);")
        self.ab_pushButton.setObjectName("ab_pushButton")
        self.bl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bl_pushButton.setEnabled(False)
        self.bl_pushButton.setGeometry(QtCore.QRect(230, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("background-color: rgb(255, 254, 202);")
        self.bl_pushButton.setObjectName("bl_pushButton")
        self.al_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.al_pushButton.setEnabled(False)
        self.al_pushButton.setGeometry(QtCore.QRect(230, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("background-color: rgb(219, 255, 199);")
        self.al_pushButton.setObjectName("al_pushButton")
        self.bd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bd_pushButton.setEnabled(False)
        self.bd_pushButton.setGeometry(QtCore.QRect(410, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("background-color: rgb(185, 227, 255);")
        self.bd_pushButton.setObjectName("bd_pushButton")
        self.ad_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ad_pushButton.setEnabled(False)
        self.ad_pushButton.setGeometry(QtCore.QRect(410, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("background-color: rgb(201, 205, 255);")
        self.ad_pushButton.setObjectName("ad_pushButton")
        self.bbed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bbed_pushButton.setEnabled(False)
        self.bbed_pushButton.setGeometry(QtCore.QRect(230, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("background-color: rgb(250, 211, 255);")
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(210, 100, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(390, 100, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(30, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.back_pushButton.setObjectName("back_pushButton")
        self.bb_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bb_cr_label.setEnabled(False)
        self.bb_cr_label.setGeometry(QtCore.QRect(40, 140, 31, 31))
        self.bb_cr_label.setText("")
        self.bb_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bb_cr_label.setScaledContents(True)
        self.bb_cr_label.setObjectName("bb_cr_label")
        self.ab_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.ab_cr_label.setEnabled(False)
        self.ab_cr_label.setGeometry(QtCore.QRect(40, 220, 31, 31))
        self.ab_cr_label.setText("")
        self.ab_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.ab_cr_label.setScaledContents(True)
        self.ab_cr_label.setObjectName("ab_cr_label")
        self.bl_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bl_cr_label.setEnabled(False)
        self.bl_cr_label.setGeometry(QtCore.QRect(220, 140, 31, 31))
        self.bl_cr_label.setText("")
        self.bl_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bl_cr_label.setScaledContents(True)
        self.bl_cr_label.setObjectName("bl_cr_label")
        self.al_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.al_cr_label.setEnabled(False)
        self.al_cr_label.setGeometry(QtCore.QRect(220, 220, 31, 31))
        self.al_cr_label.setText("")
        self.al_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.al_cr_label.setScaledContents(True)
        self.al_cr_label.setObjectName("al_cr_label")
        self.bd_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bd_cr_label.setEnabled(False)
        self.bd_cr_label.setGeometry(QtCore.QRect(400, 150, 31, 31))
        self.bd_cr_label.setText("")
        self.bd_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bd_cr_label.setScaledContents(True)
        self.bd_cr_label.setObjectName("bd_cr_label")
        self.ad_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.ad_cr_label.setEnabled(False)
        self.ad_cr_label.setGeometry(QtCore.QRect(410, 230, 31, 31))
        self.ad_cr_label.setText("")
        self.ad_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.ad_cr_label.setScaledContents(True)
        self.ad_cr_label.setObjectName("ad_cr_label")
        self.bbed_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bbed_cr_label.setEnabled(False)
        self.bbed_cr_label.setGeometry(QtCore.QRect(220, 320, 31, 31))
        self.bbed_cr_label.setText("")
        self.bbed_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bbed_cr_label.setScaledContents(True)
        self.bbed_cr_label.setObjectName("bbed_cr_label")
        
        setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(setting)
        self.bb_checkBox.clicked['bool'].connect(self.bb_pushButton.setEnabled) # type: ignore
        self.ab_checkBox.clicked['bool'].connect(self.ab_pushButton.setEnabled) # type: ignore
        self.bl_checkBox.clicked['bool'].connect(self.bl_pushButton.setEnabled) # type: ignore
        self.al_checkBox.clicked['bool'].connect(self.al_pushButton.setEnabled) # type: ignore
        self.bd_checkBox.clicked['bool'].connect(self.bd_pushButton.setEnabled) # type: ignore
        self.ad_checkBox.clicked['bool'].connect(self.ad_pushButton.setEnabled) # type: ignore
        self.bbed_checkBox.clicked['bool'].connect(self.bbed_pushButton.setEnabled) # type: ignore
        self.bb_checkBox.clicked['bool'].connect(self.bb_cr_label.setEnabled) # type: ignore
        self.bl_checkBox.clicked['bool'].connect(self.bl_cr_label.setEnabled) # type: ignore
        self.bd_checkBox.clicked['bool'].connect(self.bd_cr_label.setEnabled) # type: ignore
        self.ab_checkBox.clicked['bool'].connect(self.ab_cr_label.setEnabled) # type: ignore
        self.al_checkBox.clicked['bool'].connect(self.al_cr_label.setEnabled) # type: ignore
        self.ad_checkBox.clicked['bool'].connect(self.ad_cr_label.setEnabled) # type: ignore
        self.bbed_checkBox.clicked['bool'].connect(self.bbed_cr_label.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(setting)
        
         # เพิ่มการเชื่อมต่อปุ่มกับฟังก์ชันเพื่อเปิดหน้าต่างที่ถูกต้อง
        self.bb_pushButton.clicked.connect(lambda: self.open_drug_timing_page("ก่อนอาหาร", "มื้อเช้า"))
        self.ab_pushButton.clicked.connect(lambda: self.open_drug_timing_page("หลังอาหาร", "มื้อเช้า"))
        self.bl_pushButton.clicked.connect(lambda: self.open_drug_timing_page("ก่อนอาหาร", "มื้อเที่ยง"))
        self.al_pushButton.clicked.connect(lambda: self.open_drug_timing_page("หลังอาหาร", "มื้อเที่ยง"))
        self.bd_pushButton.clicked.connect(lambda: self.open_drug_timing_page("ก่อนอาหาร", "มื้อเย็น"))
        self.ad_pushButton.clicked.connect(lambda: self.open_drug_timing_page("หลังอาหาร", "มื้อเย็น"))
        self.bbed_pushButton.clicked.connect(lambda: self.open_drug_timing_page("", "มื้อก่อนนอน"))
        
        # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
        self.back_pushButton.clicked.connect(self.save_checkbox_states_and_close)
        
        # เพิ่มการเชื่อมต่อฐานข้อมูล SQLite3
        self.conn = sqlite3.connect("medicine.db")
        self.cursor = self.conn.cursor()
        
        # สร้างตาราง Meal ถ้ายังไม่มี
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Meal (
                meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                meal_name TEXT
            )
        ''')
    
        
        # เช็คว่ามีข้อมูลในตาราง Meal หรือยัง
        self.cursor.execute('SELECT COUNT(*) FROM Meal')
        count = self.cursor.fetchone()[0]

        if count == 0:
            # สร้างรายชื่อของมื้อ
            meal_names = [
                "มื้อเช้า ก่อนอาหาร",
                "มื้อเช้า หลังอาหาร",
                "มื้อเที่ยง ก่อนอาหาร",
                "มื้อเที่ยง หลังอาหาร",
                "มื้อเย็น ก่อนอาหาร",
                "มื้อเย็น หลังอาหาร",
                "มื้อก่อนนอน"
            ]

            # เพิ่มรายชื่อมื้อลงในตาราง Meal
            for meal_name in meal_names:
                self.cursor.execute('INSERT INTO Meal (meal_name) VALUES (?)', (meal_name,))

            self.conn.commit()
        
        self.load_checkbox_states()  # โหลดค่า checkbox_states จากฐานข้อมูล
        
        QtCore.QMetaObject.connectSlotsByName(setting)
        
    
    def save_checkbox_states_and_close(self):
        self.save_checkbox_states()
        self.setting.close()  # ปิดหน้าต่างรอบๆ ของ setting
        
    def load_checkbox_states(self):
        # โหลด checkbox_states จากฐานข้อมูล SQLite3
        self.cursor.execute('SELECT meal_id, checkbox_state FROM Meal')
        data = self.cursor.fetchall()

        for meal_id, state in data:
            if meal_id == 1:
                self.bb_checkBox.setChecked(state)
                self.bb_pushButton.setEnabled(bool(state))
                self.bb_cr_label.setEnabled(bool(state))
            elif meal_id == 2:
                self.ab_checkBox.setChecked(state)
                self.ab_pushButton.setEnabled(bool(state))
                self.ab_cr_label.setEnabled(bool(state))
            elif meal_id == 3:
                self.bl_checkBox.setChecked(state)
                self.bl_pushButton.setEnabled(bool(state))
                self.bl_cr_label.setEnabled(bool(state))
            elif meal_id == 4:
                self.al_checkBox.setChecked(state)
                self.al_pushButton.setEnabled(bool(state))
                self.al_cr_label.setEnabled(bool(state))
            elif meal_id == 5:
                self.bd_checkBox.setChecked(state)
                self.bd_pushButton.setEnabled(bool(state))
                self.bd_cr_label.setEnabled(bool(state))
            elif meal_id == 6:
                self.ad_checkBox.setChecked(state)
                self.ad_pushButton.setEnabled(bool(state))
                self.ad_cr_label.setEnabled(bool(state))
            elif meal_id == 7:
                self.bbed_checkBox.setChecked(state)
                self.bbed_pushButton.setEnabled(bool(state))
                self.bbed_cr_label.setEnabled(bool(state))

    def save_checkbox_states(self):
        checkbox_states = {
            "bb_checkBox": self.bb_checkBox.isChecked(),
            "ab_checkBox": self.ab_checkBox.isChecked(),
            "bl_checkBox": self.bl_checkBox.isChecked(),
            "al_checkBox": self.al_checkBox.isChecked(),
            "bd_checkBox": self.bd_checkBox.isChecked(),
            "ad_checkBox": self.ad_checkBox.isChecked(),
            "bbed_checkBox": self.bbed_checkBox.isChecked()
        }

        # บันทึก checkbox_states ลงในฐานข้อมูล SQLite3
        for checkbox_name, state in checkbox_states.items():
            meal_id = None
            if "bb_checkBox" in checkbox_name:
                meal_id = 1
            elif "ab_checkBox" in checkbox_name:
                meal_id = 2
            elif "bl_checkBox" in checkbox_name:
                meal_id = 3
            elif "al_checkBox" in checkbox_name:
                meal_id = 4
            elif "bd_checkBox" in checkbox_name:
                meal_id = 5
            elif "ad_checkBox" in checkbox_name:
                meal_id = 6
            elif "bbed_checkBox" in checkbox_name:
                meal_id = 7

            # ตรวจสอบว่ามีข้อมูลในฐานข้อมูลหรือไม่
            self.cursor.execute('SELECT * FROM Meal WHERE meal_id = ?', (meal_id,))
            existing_data = self.cursor.fetchone()

            if existing_data:
                # อัปเดตข้อมูล
                self.cursor.execute('''
                    UPDATE Meal
                    SET checkbox_state = ?
                    WHERE meal_id = ?
                ''', (state, meal_id))
            else:
                # ถ้าไม่มีข้อมูล ให้เพิ่มข้อมูลใหม่
                self.cursor.execute('''
                    INSERT INTO Meal (meal_id, checkbox_state, time)
                    VALUES (?, ?, ?)
                ''', (meal_id, state, ""))

        self.conn.commit()

    def open_drug_timing_page(self, timing, meal):
        from select_drug import Ui_select_drug
        self.drug_timing_window = QtWidgets.QMainWindow()
        self.drug_timing_ui = Ui_select_drug()
        self.drug_timing_ui.setupUi(self.drug_timing_window)
        self.drug_timing_ui.set_drug_timing(f"{meal} {timing}")
        
        self.drug_timing_window.show()

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "เลือกมื้อของยา"))
        self.setting_label.setText(_translate("setting", "   เลือกมื้อของยา"))
        self.bb_pushButton.setText(_translate("setting", "ก่อน อาหาร"))
        self.ab_pushButton.setText(_translate("setting", "หลัง อาหาร"))
        self.bl_pushButton.setText(_translate("setting", "ก่อน อาหาร"))
        self.al_pushButton.setText(_translate("setting", "หลัง อาหาร"))
        self.bd_pushButton.setText(_translate("setting", "ก่อน อาหาร"))
        self.ad_pushButton.setText(_translate("setting", "หลัง อาหาร"))
        self.bbed_pushButton.setText(_translate("setting", "ก่อนนอน"))
        self.b_label.setText(_translate("setting", "มื้อเช้า"))
        self.l_label.setText(_translate("setting", "มื้อเที่ยง"))
        self.d_label.setText(_translate("setting", "มื้อเย็น"))
        self.back_pushButton.setText(_translate("setting", "ย้อนกลับ"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setting = QtWidgets.QMainWindow()
    ui = Ui_setting()
    ui.setupUi(setting)
    
    setting.show()
    sys.exit(app.exec_())