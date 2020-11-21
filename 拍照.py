# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '拍照.ui'
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


class Ui_zhaopian(object):
    def setupUi(self, zhaopian):
        if not zhaopian.objectName():
            zhaopian.setObjectName(u"zhaopian")
        zhaopian.resize(640, 512)
        self.gridLayout_3 = QGridLayout(zhaopian)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(zhaopian)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setEditable(False)

        self.gridLayout.addWidget(self.comboBox, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(12)
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 0, 6, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.openGLWidget = QOpenGLWidget(zhaopian)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout_3.addWidget(self.openGLWidget, 1, 0, 1, 1)


        self.retranslateUi(zhaopian)

        QMetaObject.connectSlotsByName(zhaopian)
    # setupUi

    def retranslateUi(self, zhaopian):
        zhaopian.setWindowTitle(QCoreApplication.translate("zhaopian", u"Form", None))
        self.groupBox.setTitle("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("zhaopian", u"0", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("zhaopian", u"1", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("zhaopian", u"2", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("zhaopian", u"default", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("zhaopian", u"Photo\uff0826\u00d732\uff09", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("zhaopian", u"A4\uff08297\u00d7210\uff09", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("zhaopian", u"A4\uff08210\u00d7297\uff09", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("zhaopian", u"A3\uff08420\u00d7297\uff09", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("zhaopian", u"A3\uff08297\u00d7420\uff09", None))

        self.pushButton.setText(QCoreApplication.translate("zhaopian", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("zhaopian", u"\u7c7b\u578b\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("zhaopian", u"\u6444\u50cf\u5934\u9009\u62e9\uff1a", None))
    # retranslateUi

