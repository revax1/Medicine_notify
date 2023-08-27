from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_setting(object):
    def setupUi(self, setting):
        self.setting = setting  # Store the setting object as an instance variable
        setting.setObjectName("setting")
        setting.resize(1124, 855)
        setting.setStyleSheet("background-color: rgb(217, 244, 255)")
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        
        self.setting_label = QtWidgets.QLabel(self.centralwidget)
        self.setting_label.setGeometry(QtCore.QRect(360, 50, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.setting_label.setFont(font)
        self.setting_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setting_label.setFrameShape(QtWidgets.QFrame.Box)
        self.setting_label.setLineWidth(1)
        self.setting_label.setTextFormat(QtCore.Qt.AutoText)
        self.setting_label.setScaledContents(True)
        self.setting_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setting_label.setWordWrap(True)
        self.setting_label.setObjectName("setting_label")
        
        self.setting_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.setting_icon_label.setGeometry(QtCore.QRect(390, 70, 41, 41))
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
        self.line.setGeometry(QtCore.QRect(-20, 180, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.bb_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bb_checkBox.setGeometry(QtCore.QRect(60, 330, 61, 71))
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
        self.bb_checkBox.setStyleSheet("")
        self.bb_checkBox.setTristate(False)
        self.bb_checkBox.setObjectName("bb_checkBox")
        
        self.ab_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ab_checkBox.setGeometry(QtCore.QRect(60, 480, 61, 71))
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
        
        self.bl_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bl_checkBox.setGeometry(QtCore.QRect(440, 330, 61, 71))
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
        
        self.al_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.al_checkBox.setGeometry(QtCore.QRect(440, 480, 61, 71))
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
        
        self.bd_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bd_checkBox.setGeometry(QtCore.QRect(820, 330, 61, 71))
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
        
        self.ad_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ad_checkBox.setGeometry(QtCore.QRect(820, 480, 61, 71))
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
        
        self.bbed_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bbed_checkBox.setGeometry(QtCore.QRect(440, 700, 61, 71))
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
                width: 30px;
                height: 30px;
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
        self.line_2.setGeometry(QtCore.QRect(-30, 630, 1201, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(360, 190, 20, 441))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(740, 190, 20, 441))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        
        self.bb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bb_pushButton.setEnabled(False)
        self.bb_pushButton.setGeometry(QtCore.QRect(100, 330, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bb_pushButton.setFont(font)
        self.bb_pushButton.setAutoFillBackground(False)
        self.bb_pushButton.setStyleSheet("background-color: rgb(255, 198, 199);border: 1px solid rgb(255, 198, 199); border-radius: 10px;")
        self.bb_pushButton.setObjectName("bb_pushButton")
        
        self.ab_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ab_pushButton.setEnabled(False)
        self.ab_pushButton.setGeometry(QtCore.QRect(100, 480, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ab_pushButton.setFont(font)
        self.ab_pushButton.setStyleSheet("background-color: rgb(255, 232, 194);border: 1px solid rgb(255, 232, 194); border-radius: 10px;")
        self.ab_pushButton.setObjectName("ab_pushButton")
        
        self.bl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bl_pushButton.setEnabled(False)
        self.bl_pushButton.setGeometry(QtCore.QRect(480, 330, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bl_pushButton.setFont(font)
        self.bl_pushButton.setStyleSheet("background-color: rgb(255, 254, 202);border: 1px solid rgb(255, 254, 202); border-radius: 10px;")
        self.bl_pushButton.setObjectName("bl_pushButton")
        
        self.al_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.al_pushButton.setEnabled(False)
        self.al_pushButton.setGeometry(QtCore.QRect(480, 480, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.al_pushButton.setFont(font)
        self.al_pushButton.setStyleSheet("background-color: rgb(219, 255, 199);border: 1px solid rgb(219, 255, 199); border-radius: 10px;")
        self.al_pushButton.setObjectName("al_pushButton")
        
        self.bd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bd_pushButton.setEnabled(False)
        self.bd_pushButton.setGeometry(QtCore.QRect(860, 330, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bd_pushButton.setFont(font)
        self.bd_pushButton.setStyleSheet("background-color: rgb(185, 227, 255);border: 1px solid rgb(185, 227, 255); border-radius: 10px;")
        self.bd_pushButton.setObjectName("bd_pushButton")
        
        self.ad_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ad_pushButton.setEnabled(False)
        self.ad_pushButton.setGeometry(QtCore.QRect(860, 480, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ad_pushButton.setFont(font)
        self.ad_pushButton.setStyleSheet("background-color: rgb(201, 205, 255);border: 1px solid rgb(201, 205, 255); border-radius: 10px;")
        self.ad_pushButton.setObjectName("ad_pushButton")
        
        self.bbed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.bbed_pushButton.setEnabled(False)
        self.bbed_pushButton.setGeometry(QtCore.QRect(480, 700, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bbed_pushButton.setFont(font)
        self.bbed_pushButton.setStyleSheet("background-color: rgb(250, 211, 255);border: 1px solid rgb(250, 211, 255); border-radius: 10px;")
        self.bbed_pushButton.setObjectName("bbed_pushButton")
        
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(120, 240, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.b_label.setFont(font)
        self.b_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_label.setObjectName("b_label")
        
        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(500, 240, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.l_label.setFont(font)
        self.l_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_label.setObjectName("l_label")
        
        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(880, 240, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.d_label.setFont(font)
        self.d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d_label.setObjectName("d_label")
        
        self.setting_back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.setting_back_pushButton.setGeometry(QtCore.QRect(50, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setting_back_pushButton.setFont(font)
        self.setting_back_pushButton.setStyleSheet("color: rgb(255, 255, 255);border: 1px solid rgb(166, 0, 0); border-radius: 10px;\n"
"background-color: rgb(166, 0, 0)")
        self.setting_back_pushButton.setObjectName("setting_back_pushButton")
        self.bb_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bb_cr_label.setEnabled(False)
        self.bb_cr_label.setGeometry(QtCore.QRect(80, 290, 31, 31))
        self.bb_cr_label.setText("")
        self.bb_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bb_cr_label.setScaledContents(True)
        self.bb_cr_label.setObjectName("bb_cr_label")
        
        self.ab_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.ab_cr_label.setEnabled(False)
        self.ab_cr_label.setGeometry(QtCore.QRect(80, 440, 31, 31))
        self.ab_cr_label.setText("")
        self.ab_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.ab_cr_label.setScaledContents(True)
        self.ab_cr_label.setObjectName("ab_cr_label")
        
        self.bl_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bl_cr_label.setEnabled(False)
        self.bl_cr_label.setGeometry(QtCore.QRect(470, 290, 31, 31))
        self.bl_cr_label.setText("")
        self.bl_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bl_cr_label.setScaledContents(True)
        self.bl_cr_label.setObjectName("bl_cr_label")
        
        self.al_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.al_cr_label.setEnabled(False)
        self.al_cr_label.setGeometry(QtCore.QRect(470, 440, 31, 31))
        self.al_cr_label.setText("")
        self.al_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.al_cr_label.setScaledContents(True)
        self.al_cr_label.setObjectName("al_cr_label")
        
        self.bd_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bd_cr_label.setEnabled(False)
        self.bd_cr_label.setGeometry(QtCore.QRect(850, 290, 31, 31))
        self.bd_cr_label.setText("")
        self.bd_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.bd_cr_label.setScaledContents(True)
        self.bd_cr_label.setObjectName("bd_cr_label")
        
        self.ad_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.ad_cr_label.setEnabled(False)
        self.ad_cr_label.setGeometry(QtCore.QRect(850, 440, 31, 31))
        self.ad_cr_label.setText("")
        self.ad_cr_label.setPixmap(QtGui.QPixmap(":/icons/Flat_tick_icon.svg.png"))
        self.ad_cr_label.setScaledContents(True)
        self.ad_cr_label.setObjectName("ad_cr_label")
        
        self.bbed_cr_label = QtWidgets.QLabel(self.centralwidget)
        self.bbed_cr_label.setEnabled(False)
        self.bbed_cr_label.setGeometry(QtCore.QRect(470, 660, 31, 31))
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
        
        setting.showFullScreen()
        
        # ในส่วนนี้เราเพิ่มการเชื่อมต่อกับเมธอด save_checkbox_states ในปุ่มย้อนกลับ
        self.setting_back_pushButton.clicked.connect(self.save_checkbox_states_and_close)
        
        # เพิ่มส่วนการเชื่อมต่อ MongoDB
        self.mongo_client = pymongo.MongoClient()
        self.db = self.mongo_client['Medicine-Notify']
        self.collection = self.db['checkbox_states']
        self.load_checkbox_states()  # ดึงค่าสถานะของ checkbox และกำหนดให้
        
        QtCore.QMetaObject.connectSlotsByName(setting)
        
    
    def save_checkbox_states_and_close(self):
        self.save_checkbox_states()
        self.setting.close()  # ปิดหน้าต่างรอบๆ ของ setting
        
    def load_checkbox_states(self):
        checkbox_states = self.collection.find_one({"_id": "checkbox_states"})
        if checkbox_states:
            for checkbox_name, state in checkbox_states.items():
                checkbox = getattr(self, checkbox_name, None)
                if isinstance(checkbox, QtWidgets.QCheckBox):
                    checkbox.setChecked(state)
                    if checkbox_name == "bb_checkBox":
                        self.bb_pushButton.setEnabled(state)
                        self.bb_cr_label.setEnabled(state)
                    if checkbox_name == "ab_checkBox":
                        self.ab_pushButton.setEnabled(state)
                        self.ab_cr_label.setEnabled(state)
                    if checkbox_name == "bl_checkBox":
                        self.bl_pushButton.setEnabled(state)
                        self.bl_cr_label.setEnabled(state)
                    if checkbox_name == "al_checkBox":
                        self.al_pushButton.setEnabled(state)
                        self.al_cr_label.setEnabled(state)
                    if checkbox_name == "bd_checkBox":
                        self.bd_pushButton.setEnabled(state)
                        self.bd_cr_label.setEnabled(state)
                    if checkbox_name == "ad_checkBox":
                        self.ad_pushButton.setEnabled(state)
                        self.ad_cr_label.setEnabled(state)
                    if checkbox_name == "bbed_checkBox":
                        self.ad_pushButton.setEnabled(state)
                        self.ad_cr_label.setEnabled(state)
                    
    def save_checkbox_states(self):
        checkbox_states = {}
        for checkbox_name in dir(self):
            checkbox = getattr(self, checkbox_name, None)
            if isinstance(checkbox, QtWidgets.QCheckBox):
                checkbox_states[checkbox_name] = checkbox.isChecked()

        self.collection.update_one({"_id": "checkbox_states"}, {"$set": checkbox_states}, upsert=True)

    
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
        self.setting_back_pushButton.setText(_translate("setting", "ย้อนกลับ"))
        self.bb_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.ab_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.bl_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.al_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.bd_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.ad_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
        # self.bbed_cr_label.setEnabled(False)  # เพิ่มบรรทัดนี้
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setting = QtWidgets.QMainWindow()
    ui = Ui_setting()
    ui.setupUi(setting)
    
    setting.show()
    sys.exit(app.exec_())