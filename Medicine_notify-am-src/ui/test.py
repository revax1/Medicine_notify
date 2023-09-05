# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicine_packing2Copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_med_pack2(object):
    def setupUi(self, med_pack2):
        med_pack2.setObjectName("med_pack2")
        med_pack2.resize(531, 401)
        font = QtGui.QFont()
        font.setPointSize(10)
        med_pack2.setFont(font)
        med_pack2.setStyleSheet("background-color: rgb(217, 244, 255)")
        med_pack2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget2 = QtWidgets.QWidget(med_pack2)
        self.centralwidget2.setObjectName("centralwidget2")
        self.packMed2_label = QtWidgets.QLabel(self.centralwidget2)
        self.packMed2_label.setGeometry(QtCore.QRect(100, 30, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.packMed2_label.setFont(font)
        self.packMed2_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.packMed2_label.setFrameShape(QtWidgets.QFrame.Box)
        self.packMed2_label.setLineWidth(1)
        self.packMed2_label.setTextFormat(QtCore.Qt.AutoText)
        self.packMed2_label.setScaledContents(False)
        self.packMed2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.packMed2_label.setWordWrap(True)
        self.packMed2_label.setObjectName("packMed2_label")
        self.pack_icon2_label = QtWidgets.QLabel(self.centralwidget2)
        self.pack_icon2_label.setGeometry(QtCore.QRect(110, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pack_icon2_label.setFont(font)
        self.pack_icon2_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pack_icon2_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pack_icon2_label.setLineWidth(1)
        self.pack_icon2_label.setText("")
        self.pack_icon2_label.setTextFormat(QtCore.Qt.AutoText)
        self.pack_icon2_label.setPixmap(QtGui.QPixmap(":/icons/istockphoto-1263011147-170667a.jpg"))
        self.pack_icon2_label.setScaledContents(True)
        self.pack_icon2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pack_icon2_label.setWordWrap(True)
        self.pack_icon2_label.setObjectName("pack_icon2_label")
        self.line2 = QtWidgets.QFrame(self.centralwidget2)
        self.line2.setGeometry(QtCore.QRect(-10, 100, 541, 20))
        self.line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line2.setLineWidth(3)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        self.pack_back2_pushButton = QtWidgets.QPushButton(self.centralwidget2)
        self.pack_back2_pushButton.setGeometry(QtCore.QRect(20, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pack_back2_pushButton.setFont(font)
        self.pack_back2_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 0, 0)")
        self.pack_back2_pushButton.setObjectName("pack_back2_pushButton")
        self.frame2 = QtWidgets.QFrame(self.centralwidget2)
        self.frame2.setGeometry(QtCore.QRect(70, 130, 391, 201))
        self.frame2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setObjectName("frame2")
        self.step2_label = QtWidgets.QLabel(self.frame2)
        self.step2_label.setGeometry(QtCore.QRect(10, 10, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.step2_label.setFont(font)
        self.step2_label.setObjectName("step2_label")
        self.img2_label = QtWidgets.QLabel(self.frame2)
        self.img2_label.setGeometry(QtCore.QRect(100, 80, 171, 91))
        self.img2_label.setText("")
        self.img2_label.setPixmap(QtGui.QPixmap(":/image/med_pack2_img.png"))
        self.img2_label.setScaledContents(True)
        self.img2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img2_label.setObjectName("img2_label")
        self.next2_pushButton = QtWidgets.QPushButton(self.centralwidget2)
        self.next2_pushButton.setGeometry(QtCore.QRect(350, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.next2_pushButton.setFont(font)
        self.next2_pushButton.setStyleSheet("background-color: rgb(206, 255, 197);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/next_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next2_pushButton.setIcon(icon)
        self.next2_pushButton.setIconSize(QtCore.QSize(20, 30))
        self.next2_pushButton.setObjectName("next2_pushButton")
        med_pack2.setCentralWidget(self.centralwidget2)

        self.retranslateUi(med_pack2)
        QtCore.QMetaObject.connectSlotsByName(med_pack2)

    def retranslateUi(self, med_pack2):
        _translate = QtCore.QCoreApplication.translate
        med_pack2.setWindowTitle(_translate("med_pack2", "วิธีการใส่ยา"))
        self.packMed2_label.setText(_translate("med_pack2", "     วิธีการใส่ยาในกล่องบรรจุยา"))
        self.pack_back2_pushButton.setText(_translate("med_pack2", "ย้อนกลับ"))
        self.step2_label.setText(_translate("med_pack2", "2. นำซองยาสีชาใส่ในกล่องบรรจุยา"))
        self.next2_pushButton.setText(_translate("med_pack2", " เข้าใจแล้ว"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    med_pack2 = QtWidgets.QMainWindow()
    ui = Ui_med_pack2()
    ui.setupUi(med_pack2)
    med_pack2.show()
    sys.exit(app.exec_())
