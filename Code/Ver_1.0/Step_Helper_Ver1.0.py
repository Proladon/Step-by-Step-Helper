# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'N.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)
        self.show()  

current_step = 0
hints = {
        "STEP  0": "Ver 1.0 By Proladon",
        "STEP  1": "總務 " " → " "系統採購 " " → " "許言 ",
        "STEP  2": "支付證明採購 " " → " "支付證明申請 " " → " "新增",
        "STEP  3": "預算來源 " " → " "國科會 " " → " "工作計畫",
        "STEP  4": "整筆儲存 " " → " "明細檔資料 ",
        "STEP  5": "品名 " " → " "數量:1 " " → " "預估單價" " → " "期限:今天",
        "STEP  6": "用途:研究用 " " → " "交貨地點:研究室 " " → " "其他:無",
        "STEP  7": "預算科目:業務 " " → " "新增儲存 " " → " "(複製所有)送出",
        "STEP  8": "直接採購登入 " " → " "新增 " " → " "查詢",
        "STEP  9": "√一個 " " → " "廠商:自行採購 " " → " "整筆儲存",
        "STEP  10": "採購數量:1 " " → " "儲存"  " → " "整筆儲存",
        "STEP  11": "確定 " " → " "新增 " " → " "....",
        "STEP  12": "各單位憑證資料輸入 " " → " "新增 ",
        "STEP  13": "經費來源 " " → " "國科會 " " → " "查詢",
        "STEP  14": "√一個 " " → " "下一步 " " → " "發票or收據(no key)",
        "STEP  15": "日期:今天 " " → " "編號 " " → " "金額" " → " "未付款",
        "STEP  16": "新增 " " → " "..... " " → " "支付證明書列印",
        "STEP  17": "釘上發票影本 " " → " "桌面 " " → " "會計文件表單",
        "STEP  18": "填寫憑證黏存單" " → " "發票影印2份 ",
        "STEP  19": "1份留存" " → " "1份給會計" " → " "填寫預控表 ",
        "STEP  20": "##待補##",       
        }



#--------------Button--------------#        
class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(450, 200)
        MainWin.setMinimumSize(QtCore.QSize(450, 200))
        MainWin.setMaximumSize(QtCore.QSize(450, 200))
        MainWin.setWindowOpacity(1)
        MainWin.setStyleSheet("background-color: rgb(60, 67, 79);")
        MainWin.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


 





#--------------Button--------------#        
        self.back_btn = QtWidgets.QPushButton(MainWin)
        self.back_btn.setGeometry(QtCore.QRect(30, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("DisposableDroid BB")
        font.setPointSize(15)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("QPushButton{\n"
        "font: 15pt \"DisposableDroid BB\";\n"
        "color: rgb(255, 255, 255);\n"
        "border: 1px solid rgb(174, 209, 227);\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color: rgb(174, 209, 227)\n"
        "}")
        self.back_btn.setObjectName("back_btn")

        self.back_btn.clicked.connect(self.back_step)

#--------------Button--------------#
        self.next_btn = QtWidgets.QPushButton(MainWin)
        self.next_btn.setGeometry(QtCore.QRect(270, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("DisposableDroid BB")
        font.setPointSize(15)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("QPushButton{\n"
        "font: 15pt \"DisposableDroid BB\";\n"
        "color: rgb(255, 255, 255);\n"
        "border: 1px solid rgb(174, 209, 227);\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color: rgb(174, 209, 227)\n"
        "}")
        self.next_btn.setObjectName("next_btn")

        self.next_btn.clicked.connect(self.next_step)


#--------------步驟顯示--------------#        
        self.show_step = QtWidgets.QLabel(MainWin)
        self.show_step.setGeometry(QtCore.QRect(170, 20, 111, 31))
        self.show_step.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_step.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 15pt \"DisposableDroid BB\";")
        self.show_step.setAlignment(QtCore.Qt.AlignCenter)
        self.show_step.setObjectName("show_step")


#--------------文字顯示--------------#        
        self.show_text = QtWidgets.QLabel(MainWin)
        self.show_text.setGeometry(QtCore.QRect(0, 80, 450, 31))
        self.show_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_text.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 15pt \"DisposableDroid BB\";")
        self.show_text.setAlignment(QtCore.Qt.AlignCenter)
        self.show_text.setObjectName("show_text")

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)


#--------------Button--------------#
    def next_step(self):
        global current_step
        if current_step < 20:
            current_step += 1    
            step = "STEP  " + str(current_step)
            step2 = "STEP  " + str(current_step)
            self.show_step.setText(step)
            self.show_text.setText(hints[step2])
            

    def back_step(self):
        global current_step
        if current_step > 0:
            current_step -= 1    
            step = "STEP  " + str(current_step)
            step2 = "STEP  " + str(current_step)
            self.show_step.setText(step)
            self.show_text.setText(hints[step2])
        if current_step == 0:
            self.show_step.setText("Welcome!")
            self.show_text.setText("Ver 1.0 By Proladon")                

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "Step by Step Helper"))
        self.back_btn.setText(_translate("MainWin", "Back"))
        self.next_btn.setText(_translate("MainWin", "Next"))
        self.show_step.setText(_translate("MainWin", "Welcom!"))
        self.show_text.setText(_translate("MainWin", "Ver 1.0 By Proladon"))

app = QApplication(sys.argv)
a = App()
a.show()
sys.exit(app.exec_())
