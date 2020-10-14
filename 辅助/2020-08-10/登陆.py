# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登陆.ui',
# licensing of '登陆.ui' applies.
#
# Created: Tue May 26 20:16:46 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(329, 228)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(359, 359))
        Form.setMouseTracking(False)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICO/主题.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 331, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.denglu = QtWidgets.QWidget()
        self.denglu.setObjectName("denglu")
        self.label_8 = QtWidgets.QLabel(self.denglu)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.mima = QtWidgets.QLineEdit(self.denglu)
        self.mima.setGeometry(QtCore.QRect(89, 123, 201, 29))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.mima.setFont(font)
        self.mima.setStyleSheet("QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setClearButtonEnabled(True)
        self.mima.setObjectName("mima")
        self.label_2 = QtWidgets.QLabel(self.denglu)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 51, 51))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ICO/png/shell32.dll(45).png"))
        self.label_2.setObjectName("label_2")
        self.zhanghao = QtWidgets.QLineEdit(self.denglu)
        self.zhanghao.setGeometry(QtCore.QRect(89, 74, 201, 29))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.zhanghao.setFont(font)
        self.zhanghao.setStyleSheet("QLineEdit{\n"
"        border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.zhanghao.setClearButtonEnabled(True)
        self.zhanghao.setObjectName("zhanghao")
        self.label = QtWidgets.QLabel(self.denglu)
        self.label.setGeometry(QtCore.QRect(30, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("ICO/png/shell32.dll(269).png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.guanbi = QtWidgets.QPushButton(self.denglu)
        self.guanbi.setEnabled(True)
        self.guanbi.setGeometry(QtCore.QRect(236, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.guanbi.setFont(font)
        self.guanbi.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:16;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.guanbi.setObjectName("guanbi")
        self.shezhi_2 = QtWidgets.QPushButton(self.denglu)
        self.shezhi_2.setGeometry(QtCore.QRect(120, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.shezhi_2.setFont(font)
        self.shezhi_2.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.shezhi_2.setObjectName("shezhi_2")
        self.denglu_2 = QtWidgets.QPushButton(self.denglu)
        self.denglu_2.setEnabled(True)
        self.denglu_2.setGeometry(QtCore.QRect(10, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.denglu_2.setFont(font)
        self.denglu_2.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.denglu_2.setObjectName("denglu_2")
        self.tabWidget.addTab(self.denglu, "")
        self.shezhi = QtWidgets.QWidget()
        self.shezhi.setObjectName("shezhi")
        self.layoutWidget = QtWidgets.QWidget(self.shezhi)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 311, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.queren = QtWidgets.QPushButton(self.layoutWidget)
        self.queren.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.queren.setFont(font)
        self.queren.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.queren.setObjectName("queren")
        self.gridLayout_3.addWidget(self.queren, 1, 0, 1, 1)
        self.chongzhi = QtWidgets.QPushButton(self.layoutWidget)
        self.chongzhi.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.chongzhi.setFont(font)
        self.chongzhi.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.chongzhi.setObjectName("chongzhi")
        self.gridLayout_3.addWidget(self.chongzhi, 1, 1, 1, 1)
        self.tuichu = QtWidgets.QPushButton(self.layoutWidget)
        self.tuichu.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.tuichu.setFont(font)
        self.tuichu.setStyleSheet("QPushButton{\n"
"        border:1px solid gray;\n"
"        color:black;\n"
"        font-size:11;\n"
"        border-radius:10px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"        text-align:middle;\n"
"        background:LightGray;\n"
"        background-color: rgba(255, 255, 255, 0.5);\n"
"    }\n"
"    QPushButton:hover{\n"
"        color:white;\n"
"        border:1px solid #40E0D0;\n"
"        border-radius:10px;\n"
"        background:#40E0D0;\n"
"    }")
        self.tuichu.setObjectName("tuichu")
        self.gridLayout_3.addWidget(self.tuichu, 1, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.fuwuqiID = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.fuwuqiID.setFont(font)
        self.fuwuqiID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fuwuqiID.setObjectName("fuwuqiID")
        self.gridLayout_2.addWidget(self.fuwuqiID, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.shujukuming = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.shujukuming.setFont(font)
        self.shujukuming.setObjectName("shujukuming")
        self.gridLayout_2.addWidget(self.shujukuming, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.fuwuqizhanghao = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.fuwuqizhanghao.setFont(font)
        self.fuwuqizhanghao.setObjectName("fuwuqizhanghao")
        self.gridLayout_2.addWidget(self.fuwuqizhanghao, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.fuwuqimima = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.fuwuqimima.setFont(font)
        self.fuwuqimima.setInputMask("")
        self.fuwuqimima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.fuwuqimima.setCursorPosition(6)
        self.fuwuqimima.setObjectName("fuwuqimima")
        self.gridLayout_2.addWidget(self.fuwuqimima, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.fuwuduankou = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.fuwuduankou.setFont(font)
        self.fuwuduankou.setObjectName("fuwuduankou")
        self.gridLayout_2.addWidget(self.fuwuduankou, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 3)
        self.tabWidget.addTab(self.shezhi, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.guanbi, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.tuichu, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.mima, QtCore.SIGNAL("returnPressed()"), self.denglu_2.click)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.zhanghao, self.mima)
        Form.setTabOrder(self.mima, self.denglu_2)
        Form.setTabOrder(self.denglu_2, self.guanbi)
        Form.setTabOrder(self.guanbi, self.fuwuqiID)
        Form.setTabOrder(self.fuwuqiID, self.shujukuming)
        Form.setTabOrder(self.shujukuming, self.fuwuqizhanghao)
        Form.setTabOrder(self.fuwuqizhanghao, self.fuwuqimima)
        Form.setTabOrder(self.fuwuqimima, self.fuwuduankou)
        Form.setTabOrder(self.fuwuduankou, self.queren)
        Form.setTabOrder(self.queren, self.chongzhi)
        Form.setTabOrder(self.chongzhi, self.tuichu)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "登陆", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "欢迎使用飞云信息管理平台", None, -1))
        self.mima.setPlaceholderText(QtWidgets.QApplication.translate("Form", "密码", None, -1))
        self.zhanghao.setPlaceholderText(QtWidgets.QApplication.translate("Form", "工号", None, -1))
        self.guanbi.setText(QtWidgets.QApplication.translate("Form", "关闭", None, -1))
        self.shezhi_2.setText(QtWidgets.QApplication.translate("Form", "设置", None, -1))
        self.denglu_2.setText(QtWidgets.QApplication.translate("Form", "登陆", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.denglu), QtWidgets.QApplication.translate("Form", "登录", None, -1))
        self.queren.setText(QtWidgets.QApplication.translate("Form", "确认", None, -1))
        self.chongzhi.setText(QtWidgets.QApplication.translate("Form", "重置", None, -1))
        self.tuichu.setText(QtWidgets.QApplication.translate("Form", "退出", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "服务器ID：", None, -1))
        self.fuwuqiID.setInputMask(QtWidgets.QApplication.translate("Form", "999.999.999.999", None, -1))
        self.fuwuqiID.setText(QtWidgets.QApplication.translate("Form", "127.0.0.1", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "数据库名：", None, -1))
        self.shujukuming.setText(QtWidgets.QApplication.translate("Form", "mysql", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "服务账号：", None, -1))
        self.fuwuqizhanghao.setText(QtWidgets.QApplication.translate("Form", "root", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "服务密码：", None, -1))
        self.fuwuqimima.setText(QtWidgets.QApplication.translate("Form", "080420", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "服务端口：", None, -1))
        self.fuwuduankou.setText(QtWidgets.QApplication.translate("Form", "3306", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shezhi), QtWidgets.QApplication.translate("Form", "设置", None, -1))

