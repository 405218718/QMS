# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '人员信息录入.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(634, 363)
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 21))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.Text_XingMing = QLineEdit(Dialog)
        self.Text_XingMing.setObjectName(u"Text_XingMing")
        self.Text_XingMing.setGeometry(QRect(50, 10, 81, 21))
        self.Text_XingMing.setLayoutDirection(Qt.LeftToRight)
        self.Text_XingMing.setAutoFillBackground(False)
        self.Text_XingMing.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 10, 41, 21))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 41, 21))
        self.label_3.setFont(font1)
        self.Text_BuMen = QLineEdit(Dialog)
        self.Text_BuMen.setObjectName(u"Text_BuMen")
        self.Text_BuMen.setGeometry(QRect(50, 40, 121, 21))
        self.Text_BuMen.setLayoutDirection(Qt.LeftToRight)
        self.Text_BuMen.setAutoFillBackground(False)
        self.Text_BuMen.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_ZhiWei = QLineEdit(Dialog)
        self.Text_ZhiWei.setObjectName(u"Text_ZhiWei")
        self.Text_ZhiWei.setGeometry(QRect(50, 70, 91, 21))
        self.Text_ZhiWei.setLayoutDirection(Qt.LeftToRight)
        self.Text_ZhiWei.setAutoFillBackground(False)
        self.Text_ZhiWei.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 41, 21))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 70, 41, 21))
        self.label_5.setFont(font1)
        self.Text_GongHao = QLineEdit(Dialog)
        self.Text_GongHao.setObjectName(u"Text_GongHao")
        self.Text_GongHao.setGeometry(QRect(190, 70, 71, 21))
        self.Text_GongHao.setLayoutDirection(Qt.LeftToRight)
        self.Text_GongHao.setAutoFillBackground(False)
        self.Text_GongHao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 160, 41, 21))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 40, 41, 21))
        self.label_7.setFont(font1)
        self.Text_ZuBie = QLineEdit(Dialog)
        self.Text_ZuBie.setObjectName(u"Text_ZuBie")
        self.Text_ZuBie.setGeometry(QRect(220, 40, 171, 21))
        self.Text_ZuBie.setLayoutDirection(Qt.LeftToRight)
        self.Text_ZuBie.setAutoFillBackground(False)
        self.Text_ZuBie.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 10, 71, 21))
        self.label_8.setFont(font1)
        self.Text_RuZhi_RiQi = QLineEdit(Dialog)
        self.Text_RuZhi_RiQi.setObjectName(u"Text_RuZhi_RiQi")
        self.Text_RuZhi_RiQi.setGeometry(QRect(280, 10, 111, 21))
        self.Text_RuZhi_RiQi.setLayoutDirection(Qt.LeftToRight)
        self.Text_RuZhi_RiQi.setAutoFillBackground(False)
        self.Text_RuZhi_RiQi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_LianXiDianHua = QLineEdit(Dialog)
        self.Text_LianXiDianHua.setObjectName(u"Text_LianXiDianHua")
        self.Text_LianXiDianHua.setGeometry(QRect(80, 100, 121, 21))
        self.Text_LianXiDianHua.setLayoutDirection(Qt.LeftToRight)
        self.Text_LianXiDianHua.setAutoFillBackground(False)
        self.Text_LianXiDianHua.setMaxLength(11)
        self.Text_LianXiDianHua.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 100, 71, 21))
        self.label_9.setFont(font1)
        self.Text_XingBie = QComboBox(Dialog)
        self.Text_XingBie.addItem("")
        self.Text_XingBie.addItem("")
        self.Text_XingBie.addItem("")
        self.Text_XingBie.setObjectName(u"Text_XingBie")
        self.Text_XingBie.setEnabled(True)
        self.Text_XingBie.setGeometry(QRect(170, 10, 41, 22))
        self.Text_XingBie.setEditable(True)
        self.Text_XingBie.setFrame(True)
        self.Text_JinJiLianXiHaoMa = QLineEdit(Dialog)
        self.Text_JinJiLianXiHaoMa.setObjectName(u"Text_JinJiLianXiHaoMa")
        self.Text_JinJiLianXiHaoMa.setGeometry(QRect(270, 130, 121, 21))
        self.Text_JinJiLianXiHaoMa.setLayoutDirection(Qt.LeftToRight)
        self.Text_JinJiLianXiHaoMa.setAutoFillBackground(False)
        self.Text_JinJiLianXiHaoMa.setMaxLength(11)
        self.Text_JinJiLianXiHaoMa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 130, 101, 21))
        self.label_10.setFont(font1)
        self.Text_JinJiLianXiRen = QLineEdit(Dialog)
        self.Text_JinJiLianXiRen.setObjectName(u"Text_JinJiLianXiRen")
        self.Text_JinJiLianXiRen.setGeometry(QRect(100, 130, 71, 21))
        self.Text_JinJiLianXiRen.setLayoutDirection(Qt.LeftToRight)
        self.Text_JinJiLianXiRen.setAutoFillBackground(False)
        self.Text_JinJiLianXiRen.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 130, 91, 21))
        self.label_11.setFont(font1)
        self.Text_ChuSheng_RiQi = QLineEdit(Dialog)
        self.Text_ChuSheng_RiQi.setObjectName(u"Text_ChuSheng_RiQi")
        self.Text_ChuSheng_RiQi.setGeometry(QRect(290, 100, 101, 21))
        self.Text_ChuSheng_RiQi.setLayoutDirection(Qt.LeftToRight)
        self.Text_ChuSheng_RiQi.setAutoFillBackground(False)
        self.Text_ChuSheng_RiQi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_ChuSheng_RiQi.setReadOnly(True)
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 100, 71, 21))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 190, 91, 21))
        self.Text_ShenFenZhengHaoMa = QLineEdit(Dialog)
        self.Text_ShenFenZhengHaoMa.setObjectName(u"Text_ShenFenZhengHaoMa")
        self.Text_ShenFenZhengHaoMa.setGeometry(QRect(100, 190, 291, 21))
        self.Text_ShenFenZhengHaoMa.setLayoutDirection(Qt.LeftToRight)
        self.Text_ShenFenZhengHaoMa.setAutoFillBackground(False)
        self.Text_ShenFenZhengHaoMa.setMaxLength(18)
        self.Text_ShenFenZhengHaoMa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_DiZhi = QLineEdit(Dialog)
        self.Text_DiZhi.setObjectName(u"Text_DiZhi")
        self.Text_DiZhi.setGeometry(QRect(50, 220, 341, 21))
        self.Text_DiZhi.setLayoutDirection(Qt.LeftToRight)
        self.Text_DiZhi.setAutoFillBackground(False)
        self.Text_DiZhi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 220, 41, 21))
        self.label_16.setFont(font1)
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(270, 70, 71, 21))
        self.label_12.setFont(font1)
        self.Text_GongZuoNianFen = QLineEdit(Dialog)
        self.Text_GongZuoNianFen.setObjectName(u"Text_GongZuoNianFen")
        self.Text_GongZuoNianFen.setGeometry(QRect(340, 70, 51, 21))
        self.Text_GongZuoNianFen.setLayoutDirection(Qt.LeftToRight)
        self.Text_GongZuoNianFen.setAutoFillBackground(False)
        self.Text_GongZuoNianFen.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_TiaoXin_RiQi = QLineEdit(Dialog)
        self.Text_TiaoXin_RiQi.setObjectName(u"Text_TiaoXin_RiQi")
        self.Text_TiaoXin_RiQi.setGeometry(QRect(270, 160, 121, 21))
        self.Text_TiaoXin_RiQi.setLayoutDirection(Qt.LeftToRight)
        self.Text_TiaoXin_RiQi.setAutoFillBackground(False)
        self.Text_TiaoXin_RiQi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(200, 160, 71, 21))
        self.label_15.setFont(font1)
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 280, 41, 21))
        self.label_17.setFont(font1)
        self.Text_BeiZhu = QLineEdit(Dialog)
        self.Text_BeiZhu.setObjectName(u"Text_BeiZhu")
        self.Text_BeiZhu.setGeometry(QRect(50, 280, 341, 81))
        self.Text_BeiZhu.setLayoutDirection(Qt.LeftToRight)
        self.Text_BeiZhu.setAutoFillBackground(False)
        self.Text_BeiZhu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.action_queren = QPushButton(Dialog)
        self.action_queren.setObjectName(u"action_queren")
        self.action_queren.setGeometry(QRect(400, 290, 231, 31))
        self.action_chongzhi = QPushButton(Dialog)
        self.action_chongzhi.setObjectName(u"action_chongzhi")
        self.action_chongzhi.setGeometry(QRect(400, 330, 231, 31))
        self.action_paizhao = QPushButton(Dialog)
        self.action_paizhao.setObjectName(u"action_paizhao")
        self.action_paizhao.setGeometry(QRect(550, 250, 81, 31))
        self.action_dakaixiangji = QPushButton(Dialog)
        self.action_dakaixiangji.setObjectName(u"action_dakaixiangji")
        self.action_dakaixiangji.setGeometry(QRect(410, 250, 81, 31))
        self.Text_DaiYu = QDoubleSpinBox(Dialog)
        self.Text_DaiYu.setObjectName(u"Text_DaiYu")
        self.Text_DaiYu.setGeometry(QRect(50, 160, 121, 22))
        self.Text_DaiYu.setDecimals(2)
        self.Text_DaiYu.setMaximum(999999999.990000009536743)
        self.Text_LiZhi_RiQi = QLineEdit(Dialog)
        self.Text_LiZhi_RiQi.setObjectName(u"Text_LiZhi_RiQi")
        self.Text_LiZhi_RiQi.setGeometry(QRect(270, 250, 121, 21))
        self.Text_LiZhi_RiQi.setLayoutDirection(Qt.LeftToRight)
        self.Text_LiZhi_RiQi.setAutoFillBackground(False)
        self.Text_LiZhi_RiQi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Text_LiZhi_RiQi.setReadOnly(True)
        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 250, 71, 21))
        self.label_18.setFont(font1)
        self.Text_HeTong_RiQi = QLineEdit(Dialog)
        self.Text_HeTong_RiQi.setObjectName(u"Text_HeTong_RiQi")
        self.Text_HeTong_RiQi.setGeometry(QRect(80, 250, 111, 21))
        self.Text_HeTong_RiQi.setLayoutDirection(Qt.LeftToRight)
        self.Text_HeTong_RiQi.setAutoFillBackground(False)
        self.Text_HeTong_RiQi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(200, 250, 71, 21))
        self.label_19.setFont(font1)
        self.Text_TuPian = QLabel(Dialog)
        self.Text_TuPian.setObjectName(u"Text_TuPian")
        self.Text_TuPian.setGeometry(QRect(400, 10, 231, 231))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Text_TuPian.sizePolicy().hasHeightForWidth())
        self.Text_TuPian.setSizePolicy(sizePolicy1)
        self.Text_TuPian.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        QWidget.setTabOrder(self.Text_XingMing, self.Text_RuZhi_RiQi)
        QWidget.setTabOrder(self.Text_RuZhi_RiQi, self.Text_BuMen)
        QWidget.setTabOrder(self.Text_BuMen, self.Text_ZuBie)
        QWidget.setTabOrder(self.Text_ZuBie, self.Text_ZhiWei)
        QWidget.setTabOrder(self.Text_ZhiWei, self.Text_GongHao)
        QWidget.setTabOrder(self.Text_GongHao, self.Text_GongZuoNianFen)
        QWidget.setTabOrder(self.Text_GongZuoNianFen, self.Text_LianXiDianHua)
        QWidget.setTabOrder(self.Text_LianXiDianHua, self.Text_JinJiLianXiRen)
        QWidget.setTabOrder(self.Text_JinJiLianXiRen, self.Text_JinJiLianXiHaoMa)
        QWidget.setTabOrder(self.Text_JinJiLianXiHaoMa, self.Text_DaiYu)
        QWidget.setTabOrder(self.Text_DaiYu, self.Text_ShenFenZhengHaoMa)
        QWidget.setTabOrder(self.Text_ShenFenZhengHaoMa, self.Text_DiZhi)
        QWidget.setTabOrder(self.Text_DiZhi, self.Text_BeiZhu)
        QWidget.setTabOrder(self.Text_BeiZhu, self.action_dakaixiangji)
        QWidget.setTabOrder(self.action_dakaixiangji, self.action_paizhao)
        QWidget.setTabOrder(self.action_paizhao, self.action_queren)
        QWidget.setTabOrder(self.action_queren, self.action_chongzhi)
        QWidget.setTabOrder(self.action_chongzhi, self.Text_TiaoXin_RiQi)
        QWidget.setTabOrder(self.Text_TiaoXin_RiQi, self.Text_ChuSheng_RiQi)
        QWidget.setTabOrder(self.Text_ChuSheng_RiQi, self.Text_XingBie)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4eba\u5458\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d:", None))
        self.Text_XingMing.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6027\u522b:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u90e8\u95e8:", None))
        self.Text_BuMen.setInputMask("")
        self.Text_ZhiWei.setInputMask("")
        self.Text_ZhiWei.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u804c\u4f4d:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5de5\u53f7:", None))
        self.Text_GongHao.setInputMask("")
        self.Text_GongHao.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u5f85\u9047:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7ec4\u522b:", None))
        self.Text_ZuBie.setInputMask("")
        self.Text_ZuBie.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u5165\u804c\u65e5\u671f:", None))
        self.Text_RuZhi_RiQi.setInputMask("")
        self.Text_RuZhi_RiQi.setText("")
        self.Text_LianXiDianHua.setInputMask("")
        self.Text_LianXiDianHua.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8054\u7cfb\u7535\u8bdd:", None))
        self.Text_XingBie.setItemText(0, "")
        self.Text_XingBie.setItemText(1, QCoreApplication.translate("Dialog", u"\u7537", None))
        self.Text_XingBie.setItemText(2, QCoreApplication.translate("Dialog", u"\u5973", None))

        self.Text_JinJiLianXiHaoMa.setInputMask("")
        self.Text_JinJiLianXiHaoMa.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u7d27\u6025\u8054\u7cfb\u7535\u8bdd:", None))
        self.Text_JinJiLianXiRen.setInputMask("")
        self.Text_JinJiLianXiRen.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u7d27\u6025\u8054\u7cfb\u4eba:", None))
        self.Text_ChuSheng_RiQi.setInputMask("")
        self.Text_ChuSheng_RiQi.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u51fa\u751f\u65e5\u671f:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u8eab\u4efd\u8bc1\u53f7\u7801\uff1a", None))
        self.Text_ShenFenZhengHaoMa.setInputMask("")
        self.Text_ShenFenZhengHaoMa.setText("")
        self.Text_DiZhi.setInputMask("")
        self.Text_DiZhi.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u5730\u5740:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5de5\u4f5c\u5e74\u4efd:", None))
        self.Text_GongZuoNianFen.setInputMask("")
        self.Text_GongZuoNianFen.setText("")
        self.Text_TiaoXin_RiQi.setInputMask("")
        self.Text_TiaoXin_RiQi.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u8c03\u85aa\u65e5\u671f:", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8:", None))
        self.Text_BeiZhu.setInputMask("")
        self.Text_BeiZhu.setText("")
        self.action_queren.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.action_chongzhi.setText(QCoreApplication.translate("Dialog", u"\u91cd\u7f6e", None))
        self.action_paizhao.setText(QCoreApplication.translate("Dialog", u"\u62cd\u7167", None))
        self.action_dakaixiangji.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u76f8\u673a", None))
        self.Text_DaiYu.setPrefix(QCoreApplication.translate("Dialog", u"$ ", None))
        self.Text_LiZhi_RiQi.setInputMask("")
        self.Text_LiZhi_RiQi.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u5408\u540c\u65e5\u671f:", None))
        self.Text_HeTong_RiQi.setInputMask("")
        self.Text_HeTong_RiQi.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u79bb\u804c\u65e5\u671f:", None))
        self.Text_TuPian.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u70b9\u51fb\u6253\u5f00\u6444\u50cf\u5934</span></p></body></html>", None))
    # retranslateUi

