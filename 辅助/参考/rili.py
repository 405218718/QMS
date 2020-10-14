from PyQt5.QtWidgets import QDateEdit, QPushButton
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QValidator



class DateEdit(QDateEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCalendarPopup(True)
        self.clear()  # 设置初始文本为空串
        self.setDate(QDate.currentDate())  # 设置当前日期
        self.dateChanged.connect(self.onDateChanged)  # 当日期改变时触发槽函数
        # self.setDate(QDate.currentDate())  # 设置当前日期
        self.calendarWidget().clicked.connect(lambda: {
            # 选择日期后，Edit 根据内容会自动调用 textFromDateTime 设置最终的显示文本。
            self.lineEdit().setText(self.text() or " ")
        })

    def setDateTime(self, dateTime: QDate):
        """调用 super.setDateTime 后，Edit 会自动根据该 dateTime 格式设置最终的显示文本。"""
        self.lineEdit().setText(dateTime.toString())

    def validate(self, input: str, pos: int):

        """时间验证器：not input 允许接受空值"""
        if not input:
            print(1)
            return QValidator.Acceptable, '', 0
        return super().validate(input, pos)

    def textFromDateTime(self, dateTime:QDate):

        """
        每当需要显示 dateTime 时，Edit 就会使用此虚拟函数。
        如果重新实现，则可能还需要重新实现 validate()。
        :param dateTime: 当前 Edit 设置的日期，默认为 2000-1-1
        :return: dateTime 对应格式的日期字符串，如果 Edit 文本非空，则将自动设置为 Edit 的显示文本。
        """

        # self.dateTime = QDate.currentDate()
        if not self.text():
            dateTime = QDate.currentDate()
            # if self.text() == "":
            #     self.setDate(QDate.currentDate())  # 设置当前日期
            # super().setDate(QDate.currentDate())
            # self.setDateTime(QDate.currentDate())
            # print(QDate.currentDate().toString('yyyy/MM/dd'))
            # self.setDate(QDate.currentDate())
            print(dateTime)
            print(2)
            # self.clear()
            # super().textFromDateTime(QDateTime.currentDateTime())
            # super().textFromDateTime(dateTime)
            return ''


        print(dateTime)
        print(3)
        return super().textFromDateTime(dateTime)

        # def on__valueChanged:



    def clear(self):
        self.lineEdit().clear()
        print(4)
        self.setDate(QDate.currentDate())

        # 日期发生改变时执行
    def onDateChanged(self):
        if self.date() == QDate(2000, 1, 1):
            self.setDate(QDate.currentDate())  # 设置当前日期
        # print(date)


    # def close(self):
        # self.setDate(QDate.currentDate())  # 设置当前日期
        # super().textFromDateTime(QDateTime.currentDateTime())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    timeEdit = DateEdit(w)
    timeEdit.resize(150, 21)
    # timeEdit.setDateTime('2020-01-20 20:11:12', 'yyyy-MM-dd hh:mm:ss')
    btn = QPushButton('按钮', w)
    btn.move(0, 32)
    w.show()
    sys.exit(app.exec())