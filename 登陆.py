# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '登陆.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect, QSize, Qt)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QIcon, QPalette, QPixmap)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(327, 227)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(359, 359))
        Form.setMouseTracking(False)
        Form.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/new/prefix1/ICO/\u4e3b\u9898.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 331, 261))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(170, 85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(170, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tabWidget.setPalette(palette)
        font = QFont()
        font.setFamily(u"\u65b0\u5b8b\u4f53")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.denglu = QWidget()
        self.denglu.setObjectName(u"denglu")
        self.label_8 = QLabel(self.denglu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 301, 51))
        font1 = QFont()
        font1.setFamily(u"\u534e\u6587\u5f69\u4e91")
        font1.setPointSize(18)
        self.label_8.setFont(font1)
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.mima = QLineEdit(self.denglu)
        self.mima.setObjectName(u"mima")
        self.mima.setGeometry(QRect(89, 123, 201, 29))
        self.mima.setFont(font)
        self.mima.setStyleSheet(u"QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.mima.setEchoMode(QLineEdit.Password)
        self.mima.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.denglu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 51, 51))
        font2 = QFont()
        font2.setFamily(u"\u65b0\u5b8b\u4f53")
        font2.setPointSize(18)
        self.label_2.setFont(font2)
        self.label_2.setPixmap(QPixmap(u":/new/prefix1/ICO/png/shell32.dll(45).png"))
        self.zhanghao = QLineEdit(self.denglu)
        self.zhanghao.setObjectName(u"zhanghao")
        self.zhanghao.setGeometry(QRect(89, 74, 201, 29))
        self.zhanghao.setFont(font)
        self.zhanghao.setStyleSheet(u"QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.zhanghao.setClearButtonEnabled(True)
        self.label = QLabel(self.denglu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 51, 41))
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setPixmap(QPixmap(u":/new/prefix1/ICO/png/shell32.dll(269).png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.guanbi = QPushButton(self.denglu)
        self.guanbi.setObjectName(u"guanbi")
        self.guanbi.setEnabled(True)
        self.guanbi.setGeometry(QRect(236, 180, 71, 31))
        self.guanbi.setFont(font)
        self.guanbi.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:16;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.shezhi_2 = QPushButton(self.denglu)
        self.shezhi_2.setObjectName(u"shezhi_2")
        self.shezhi_2.setGeometry(QRect(120, 180, 81, 31))
        self.shezhi_2.setFont(font)
        self.shezhi_2.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.denglu_2 = QPushButton(self.denglu)
        self.denglu_2.setObjectName(u"denglu_2")
        self.denglu_2.setEnabled(True)
        self.denglu_2.setGeometry(QRect(10, 180, 71, 31))
        self.denglu_2.setFont(font)
        self.denglu_2.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.tabWidget.addTab(self.denglu, "")
        self.shezhi = QWidget()
        self.shezhi.setObjectName(u"shezhi")
        self.layoutWidget = QWidget(self.shezhi)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 311, 221))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.queren = QPushButton(self.layoutWidget)
        self.queren.setObjectName(u"queren")
        self.queren.setMinimumSize(QSize(0, 30))
        self.queren.setFont(font)
        self.queren.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")

        self.gridLayout_3.addWidget(self.queren, 1, 0, 1, 1)

        self.chongzhi = QPushButton(self.layoutWidget)
        self.chongzhi.setObjectName(u"chongzhi")
        self.chongzhi.setMinimumSize(QSize(0, 30))
        self.chongzhi.setFont(font)
        self.chongzhi.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")

        self.gridLayout_3.addWidget(self.chongzhi, 1, 1, 1, 1)

        self.tuichu = QPushButton(self.layoutWidget)
        self.tuichu.setObjectName(u"tuichu")
        self.tuichu.setMinimumSize(QSize(0, 30))
        self.tuichu.setFont(font)
        self.tuichu.setStyleSheet(u"QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"		border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"		background:LightGray;\n"
"		background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")

        self.gridLayout_3.addWidget(self.tuichu, 1, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.fuwuqiID = QLineEdit(self.layoutWidget)
        self.fuwuqiID.setObjectName(u"fuwuqiID")
        self.fuwuqiID.setFont(font)
        self.fuwuqiID.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.fuwuqiID, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.shujukuming = QLineEdit(self.layoutWidget)
        self.shujukuming.setObjectName(u"shujukuming")
        self.shujukuming.setFont(font)

        self.gridLayout_2.addWidget(self.shujukuming, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.fuwuqizhanghao = QLineEdit(self.layoutWidget)
        self.fuwuqizhanghao.setObjectName(u"fuwuqizhanghao")
        self.fuwuqizhanghao.setFont(font)

        self.gridLayout_2.addWidget(self.fuwuqizhanghao, 2, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.fuwuqimima = QLineEdit(self.layoutWidget)
        self.fuwuqimima.setObjectName(u"fuwuqimima")
        self.fuwuqimima.setFont(font)
        self.fuwuqimima.setEchoMode(QLineEdit.Password)
        self.fuwuqimima.setCursorPosition(6)

        self.gridLayout_2.addWidget(self.fuwuqimima, 3, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.fuwuduankou = QLineEdit(self.layoutWidget)
        self.fuwuduankou.setObjectName(u"fuwuduankou")
        self.fuwuduankou.setFont(font)

        self.gridLayout_2.addWidget(self.fuwuduankou, 4, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 3)

        self.tabWidget.addTab(self.shezhi, "")
        QWidget.setTabOrder(self.zhanghao, self.mima)
        QWidget.setTabOrder(self.mima, self.denglu_2)
        QWidget.setTabOrder(self.denglu_2, self.guanbi)
        QWidget.setTabOrder(self.guanbi, self.fuwuqiID)
        QWidget.setTabOrder(self.fuwuqiID, self.shujukuming)
        QWidget.setTabOrder(self.shujukuming, self.fuwuqizhanghao)
        QWidget.setTabOrder(self.fuwuqizhanghao, self.fuwuqimima)
        QWidget.setTabOrder(self.fuwuqimima, self.fuwuduankou)
        QWidget.setTabOrder(self.fuwuduankou, self.queren)
        QWidget.setTabOrder(self.queren, self.chongzhi)
        QWidget.setTabOrder(self.chongzhi, self.tuichu)

        self.retranslateUi(Form)
        self.guanbi.clicked.connect(Form.close)
        self.tuichu.clicked.connect(Form.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u9646", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u4f7f\u7528\u98de\u4e91\u4fe1\u606f\u7ba1\u7406\u5e73\u53f0", None))
        self.mima.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.label_2.setText("")
        self.zhanghao.setPlaceholderText(QCoreApplication.translate("Form", u"\u5de5\u53f7", None))
        self.label.setText("")
        self.guanbi.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.shezhi_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.denglu_2.setText(QCoreApplication.translate("Form", u"\u767b\u9646", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.denglu), QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.queren.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.chongzhi.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.tuichu.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u5668ID\uff1a", None))
        self.fuwuqiID.setInputMask(QCoreApplication.translate("Form", u"999.999.999.999", None))
        self.fuwuqiID.setText(QCoreApplication.translate("Form", u"127.0.0.1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u540d\uff1a", None))
        self.shujukuming.setText(QCoreApplication.translate("Form", u"mysql", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u8d26\u53f7\uff1a", None))
        self.fuwuqizhanghao.setText(QCoreApplication.translate("Form", u"root", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u5bc6\u7801\uff1a", None))
        self.fuwuqimima.setInputMask("")
        self.fuwuqimima.setText(QCoreApplication.translate("Form", u"080420", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u7aef\u53e3\uff1a", None))
        self.fuwuduankou.setText(QCoreApplication.translate("Form", u"3306", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shezhi), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

