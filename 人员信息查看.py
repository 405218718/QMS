# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '人员信息查看.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class UI_ryxxck(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxxck()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(455, 606)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u"ICO/\u4e3b\u9898.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Text_DianHua = QLabel(Dialog)
        self.Text_DianHua.setObjectName(u"Text_DianHua")
        self.Text_DianHua.setGeometry(QRect(70, 570, 299, 31))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(12)
        self.Text_DianHua.setFont(font1)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 450, 130))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Text_GongSiMingCheng = QLabel(self.layoutWidget)
        self.Text_GongSiMingCheng.setObjectName(u"Text_GongSiMingCheng")
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        font2.setPointSize(36)
        self.Text_GongSiMingCheng.setFont(font2)

        self.gridLayout.addWidget(self.Text_GongSiMingCheng, 0, 0, 1, 1)

        self.gongzauozheng = QLabel(self.layoutWidget)
        self.gongzauozheng.setObjectName(u"gongzauozheng")

        self.gridLayout.addWidget(self.gongzauozheng, 1, 0, 1, 1)

        self.Text_DongHao = QLabel(self.layoutWidget)
        self.Text_DongHao.setObjectName(u"Text_DongHao")
        self.Text_DongHao.setFont(font1)

        self.gridLayout.addWidget(self.Text_DongHao, 2, 0, 1, 1)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 410, 301, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Text_XingMing = QLabel(self.layoutWidget1)
        self.Text_XingMing.setObjectName(u"Text_XingMing")
        self.Text_XingMing.setFont(font1)

        self.verticalLayout.addWidget(self.Text_XingMing)

        self.Text_BuMen = QLabel(self.layoutWidget1)
        self.Text_BuMen.setObjectName(u"Text_BuMen")
        self.Text_BuMen.setFont(font1)

        self.verticalLayout.addWidget(self.Text_BuMen)

        self.Text_ZhiWei = QLabel(self.layoutWidget1)
        self.Text_ZhiWei.setObjectName(u"Text_ZhiWei")
        self.Text_ZhiWei.setFont(font1)

        self.verticalLayout.addWidget(self.Text_ZhiWei)

        self.Text_RuZhi_RiQi = QLabel(self.layoutWidget1)
        self.Text_RuZhi_RiQi.setObjectName(u"Text_RuZhi_RiQi")
        self.Text_RuZhi_RiQi.setFont(font1)

        self.verticalLayout.addWidget(self.Text_RuZhi_RiQi)

        self.Text_TuPian = QLabel(Dialog)
        self.Text_TuPian.setObjectName(u"Text_TuPian")
        self.Text_TuPian.setGeometry(QRect(100, 140, 241, 261))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Text_TuPian.sizePolicy().hasHeightForWidth())
        self.Text_TuPian.setSizePolicy(sizePolicy1)
        self.Text_TuPian.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4eba\u5458\u4fe1\u606f\u67e5\u770b", None))
        self.Text_DianHua.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u7535 \u8bdd: 18820099999</span></p></body></html>", None))
        self.Text_GongSiMingCheng.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Agency FB'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">\u5e7f\u4e1c\u5929\u502c\u667a\u80fd\u88c5\u5907\u79d1\u6280\u6709\u9650\u516c\u53f8</span></p></body></html>", None))
        self.gongzauozheng.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">\u5de5\u4f5c\u8bc1</span></p></body></html>", None))
        self.Text_DongHao.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u7f16\u53f7:A00001</p></body></html>", None))
        self.Text_XingMing.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u59d3 \u540d: </span></p></body></html>", None))
        self.Text_BuMen.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u90e8 \u95e8: </span></p></body></html>", None))
        self.Text_ZhiWei.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u804c \u4f4d: </span></p></body></html>", None))
        self.Text_RuZhi_RiQi.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u5165\u804c\u65e5\u671f: </span></p></body></html>", None))
        self.Text_TuPian.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u5934\u50cf</p></body></html>", None))
    # retranslateUi

