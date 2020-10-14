from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class Ui_Dialog(QtWidgets.QDialog):
    # inp_text_signal = QtCore.pyqtSignal(str)   #定义信号
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.l2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit.setFocusPolicy(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 133, 20))
        self.lineEdit.setText("请输入用户名")
        self.l2.setGeometry(QtCore.QRect(100, 80, 123, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.installEventFilter(self)

        # self.retranslateUi(Dialog)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)
        # # self.inp_text_signal.connect(self.prn)

    # def prn(self, str):
    #     print(str)
    #
    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def mousePressEvent(self, event):  # 鼠标左键按下
        # 根据当前点击的坐标获取子控件

        if not self.lineEdit.hasFocus():
            self.lineEdit.setText("请输入用户名")
            print("ok3")
        else:
            pass
        return False


    def eventFilter(self, obj, event):

        if obj == self.lineEdit:
            if event.type() == QEvent.FocusIn:
                # self.inp_text_signal.emit("已进")
                # if self.lineEdit.text().strip() == '请输入用户名':
                self.lineEdit.clear()

                print("ok1")
            elif event.type() == QEvent.FocusOut:
                # if self.lineEdit.text().strip() == '':
                self.lineEdit.setText("请输入用户名")
                print("ok2")
            else:
                pass
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())