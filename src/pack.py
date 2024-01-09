from Utils import *
from UI_Generate import *
width, height = Scale_Width_Height()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from resources_rc import *

class Ui_med_pack(object):
    def setupUi(self, med_pack):
        UI_instance.Set(med_pack)
        show_widget_fullscreen(med_pack)
        
        med_pack.setObjectName("med_pack")
        med_pack.resize(int(683 * width), int(400 * height))
        med_pack.setStyleSheet("\n"
"background-color: rgb(23, 73, 110);")
        self.centralwidget = QtWidgets.QWidget(med_pack)
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
        self.img_label_4 = QtWidgets.QLabel(self.frame)
        self.img_label_4.setGeometry(QtCore.QRect(int(246 * width), int(80 * height), int(33 * width), int(31 * height)))
        self.img_label_4.setText("")
        self.img_label_4.setPixmap(QtGui.QPixmap(":/icons/ball.png"))
        self.img_label_4.setScaledContents(True)
        self.img_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label_4.setObjectName("img_label_4")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(int(40 * width), int(130 * height), int(181 * width), int(61 * height)))
        self.frame_11.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(170, 203, 223);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_1 = QtWidgets.QLabel(self.frame_11)
        self.label_1.setGeometry(QtCore.QRect(0, 0, int(181 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(int(40 * width), int(270 * height), int(181 * width), int(41 * height)))
        self.frame_13.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_13)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_13.setGraphicsEffect(shadow)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(int(40 * width), int(170 * height), int(181 * width), int(121 * height)))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.img_label = QtWidgets.QLabel(self.frame_12)
        self.img_label.setGeometry(QtCore.QRect(int(15 * width), int(0 * height), int(151 * width), int(131 * height)))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/image/pack1_img.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.frame_14 = QtWidgets.QFrame(self.centralwidget)
        self.frame_14.setGeometry(QtCore.QRect(int(250 * width), int(270 * height), int(181 * width), int(41 * height)))
        self.frame_14.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_14)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_14.setGraphicsEffect(shadow)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setGeometry(QtCore.QRect(int(250 * width), int(170 * height), int(181 * width), int(121 * height)))
        self.frame_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.img_label_2 = QtWidgets.QLabel(self.frame_15)
        self.img_label_2.setGeometry(QtCore.QRect(int(5 * width), int(0 * height), int(171 * width), int(121 * height)))
        self.img_label_2.setText("")
        self.img_label_2.setPixmap(QtGui.QPixmap(":/image/newpack2_img.png"))
        self.img_label_2.setScaledContents(True)
        self.img_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label_2.setObjectName("img_label_2")
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        self.frame_16.setGeometry(QtCore.QRect(int(250 * width), int(130 * height), int(181 * width), int(61 * height)))
        self.frame_16.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(244, 212, 99);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_2 = QtWidgets.QLabel(self.frame_16)
        self.label_2.setGeometry(QtCore.QRect(int(0 * width), int(0 * height), int(181 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        self.frame_17.setGeometry(QtCore.QRect(int(460 * width), int(270 * height), int(181 * width), int(41 * height)))
        self.frame_17.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(255, 255, 255);")
        # Add drop shadow effect to the button
        shadow = QGraphicsDropShadowEffect(self.frame_17)
        shadow.setBlurRadius(int(8 * width))
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        shadow.setOffset(int(0 * width), int(2 * height))
        self.frame_17.setGraphicsEffect(shadow)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setGeometry(QtCore.QRect(int(460 * width), int(170 * height), int(181 * width), int(121 * height)))
        self.frame_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.img_label_3 = QtWidgets.QLabel(self.frame_18)
        self.img_label_3.setGeometry(QtCore.QRect(int(5 * width), int(0 * height), int(161 * width), int(131 * height)))
        self.img_label_3.setText("")
        self.img_label_3.setPixmap(QtGui.QPixmap(":/image/newpack3_img.png"))
        self.img_label_3.setScaledContents(True)
        self.img_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label_3.setObjectName("img_label_3")
        self.frame_19 = QtWidgets.QFrame(self.centralwidget)
        self.frame_19.setGeometry(QtCore.QRect(int(460 * width), int(130 * height), int(181 * width), int(61 * height)))
        self.frame_19.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(115, 172, 131);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_3 = QtWidgets.QLabel(self.frame_19)
        self.label_3.setGeometry(QtCore.QRect(int(0 * width), int(0 * height), int(181 * width), int(41 * height)))
        font = QtGui.QFont()
        font.setPointSize(int(12 * height))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_19.raise_()
        self.frame_17.raise_()
        self.frame_18.raise_()
        self.frame_16.raise_()
        self.frame.raise_()
        self.frame_11.raise_()
        self.frame_13.raise_()
        self.frame_12.raise_()
        self.frame_14.raise_()
        self.frame_15.raise_()
        med_pack.setCentralWidget(self.centralwidget)

        self.retranslateUi(med_pack)
        QtCore.QMetaObject.connectSlotsByName(med_pack)

        self.add_back_pushButton.clicked.connect(self.backpage)

      
        self.add_back_pushButton.pressed.connect(lambda: self.set_button_pressed_style(self.add_back_pushButton))

        
    def set_button_pressed_style(self, button):
        button.setStyleSheet(
            "border-radius: 9px;\n"
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(200, 200, 200);"  # Change color when pressed
        )
    def backpage(self):
        from main import Ui_Medicine_App
        backpage_form = UI_Genarate()
        backpage_form.widgetSet(UI_instance.Get(), Ui_Medicine_App)

    def retranslateUi(self, med_pack):
        _translate = QtCore.QCoreApplication.translate
        med_pack.setWindowTitle(_translate("med_pack", "วิธีการใส่ยา"))
        self.label.setText(_translate("med_pack", "        คำแนะนำการใส่ยา"))
        self.add_back_pushButton.setText(_translate("med_pack", "ย้อนกลับ"))
        self.label_1.setText(_translate("med_pack", "1.นำยาใส่ในซองสีชา"))
        self.label_2.setText(_translate("med_pack", "2.นำซองสีชาใส่ในลูกบอล"))
        self.label_3.setText(_translate("med_pack", "3.เตรียมใส่ในเครื่องต่อไป"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    med_pack = QtWidgets.QMainWindow()
    ui = Ui_med_pack()
    ui.setupUi(med_pack)
    med_pack.show()
    sys.exit(app.exec_())
