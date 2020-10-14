import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import QDate, Signal
from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget,\
    QLineEdit, QAction


class MyDateEdit(QLineEdit):
    check_signal = Signal(bool)  # 验证输入日期是否正确信号
    show_signal = Signal()  # 点击下拉框发送信号

    def __init__(self, init_date=QDate(), parent=None):
        super(MyDateEdit, self).__init__(parent=parent)
        self.my_date = init_date

        # 初始化外观
        self.resize(150, 20)
        # self.setInputMask(r'9999/99/99;_')
        self.setText(self.my_date.toString('yyyy/MM/dd'))

        self.show_action = QAction(self)
        self.show_action.setIcon(QIcon('aa.ico'))
        self.addAction(self.show_action, QLineEdit.TrailingPosition)

        # 信号和槽连接
        self.show_action.triggered.connect(self.show_signal)

    # def _show_calendar_func(self):
    #     """
    #     发射显示日历信号
    #     :return: None
    #     """
    #     self.show_signal.emit()

    # def _check_input_func(self, year, month, day):
    #     """
    #     判断日期是否正确
    #     :param year:
    #     :param month:
    #     :param day:
    #     :return: True or False
    #     """
    #     # 年部分必须填满四个数
    #     if len(year) != 4:
    #         return False
    #
    #     # 月部分必须填满两个数
    #     if len(month) != 2:
    #         return False
    #     else:
    #         # 填满的话必须小于12
    #         if int(month) > 12:
    #             return False
    #
    #     # 日部分必须填满两个数
    #     if len(day) != 2:
    #         return False
    #     else:
    #         # 填满的话必须小于31
    #         if int(day) > 31:
    #             return False
    #
    #     # 上面如果都符合，则用QDate.isValid()方法判断日期是否合理
    #     if not QDate.isValid(int(year), int(month), int(day)):
    #         return False
    #     return True
    #
    # def date(self):
    #     """
    #     获取日期
    #     :return:self.my_date(QDate类型)
    #     """
    #     # 获取日期中的年月日部分
    #     year = self.text().split('/')[0]
    #     month = self.text().split('/')[1]
    #     day = self.text().split('/')[2]
    #
    #     # 进行判断，合理则发送日期，不合理发送信号
    #     check_result = self._check_input_func(year, month, day)
    #     if check_result:
    #         self.my_date = QDate(int(year), int(month), int(day))
    #         self.check_signal.emit(True)
    #         return self.my_date
    #     else:
    #         self.check_signal.emit(False)
    #
    # def setDate(self, QDate):
    #     """
    #     设置日期
    #     :param QDate: QDate类型参数
    #     :return: None
    #     """
    #     self.setText(QDate.toString(self.display_format))


class MyCalendar(QCalendarWidget):
    date_signal = Signal(str)  # 发送日期信号

    def __init__(self, parent=None):
        super(MyCalendar, self).__init__(parent=parent)
        self.clicked.connect(self._set_calendar_date_func)
        self.hide()

    def _set_calendar_date_func(self):
        """
        将输入框文本设置为日历上选择的日期，并将日历隐藏
        :return: None
        """
        my_date = self.selectedDate().toString('yyyy/MM/dd')
        self.date_signal.emit(my_date)
        self.hide()


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)
        self.my_date = MyDateEdit(QDate(), self)
        self.my_date.show_signal.connect(self.show_calendar_func)
        self.calendar = MyCalendar(self)
        self.calendar.date_signal.connect(self.set_calendar_date_func)

    def show_calendar_func(self):
        if self.calendar.isHidden():
            self.calendar.show()
            self.calendar.setGeometry(self.my_date.x(), self.my_date.height(), 240, 200)
        else:
            self.calendar.hide()



    def set_calendar_date_func(self, date):
        self.my_date.setText(date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())



#
# #QCalendar日历控件使用
# from PyQt5.QtWidgets import QCalendarWidget, QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel
# from PyQt5.QtCore import QDir
# from PyQt5.QtGui import QIcon,QPixmap,QFont
# from PyQt5.QtCore import  QDate
#
# import sys
#
# class WindowClass(QWidget):
#
#     def __init__(self,parent=None):
#
#        super(WindowClass, self).__init__(parent)
#        self.btn=QPushButton(self)#self参数则让该按钮显示当前窗体中
#        self.btn.setText("选择日期")
#        self.btn.move(0,0)
#        self.btn.clicked.connect(self.openCalendar)
#        self.le=QLabel(self)
#        self.cal=QCalendarWidget(self)
#        # self.cal.setMinimumDate(QDate(2017,1,1))#设置日期最小范围
#        # self.cal.setMaximumDate(QDate(2019,12,30))#设置日期最大范围
#        self.cal.setGridVisible(False)#是否显示日期之间的网格
#        self.cal.move(5,30)
#        self.cal.hide()#隐藏日期控件
#        self.cal.clicked[QDate].connect(self.showDate)#clicked[参数]，即定义showDate是传入的参数类型设置
#        date=self.cal.selectedDate()#获取选中日期，默认当前系统时间
#        self.le.setText(date.toString('yyyy-MM-dd'))
#        self.le.move(100,20)
#        self.setGeometry(100,100,400,350)#设置当前窗体位置和大小
#        self.setWindowTitle("日历控件使用")
#
#     def showDate(self,date):
#         self.le.setText(date.toString("yyyy-MM-dd dddd"))
#         self.cal.close()#关闭日期控件
#     def openCalendar(self):
#         self.cal.show()#显示日期控件
#
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     win=WindowClass()
#     win.show()
#     sys.exit(app.exec_())
#
#




 #QDateEdit和QTimeEdit控件使用
