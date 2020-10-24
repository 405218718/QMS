import pymysql
from PySide2.QtGui import QValidator
from PySide2.QtWidgets import QMessageBox,QTableWidgetItem, QAbstractItemView,QDateEdit,QLineEdit
from PySide2.QtCore import QDate



class DuiXiang:
    def __init__(self):
        db = self.connect_db()
        # 获取游标
        self.cur = db.cursor(pymysql.cursors.DictCursor)  # 使用字典类型输出

    # 添加选项卡通用函数
    def add_tab(biao_tou: list,tableWidgetX: QTableWidgetItem):
        """
        列表控件项设置
        :param tableWidgetX:
        :return:
        """
        tableWidgetX.setColumnCount(len(biao_tou))  # 设置列数
        tableWidgetX.setRowCount(0)                 # 设置数据区行数
        tableWidgetX.setHorizontalHeaderLabels(biao_tou)  # 设置列命名biao_tou
        tableWidgetX.setAlternatingRowColors(True)  # 交替行颜色
        selMode = QAbstractItemView.SelectRows
        tableWidgetX.setSelectionBehavior(selMode)  # 选择行为：行选择
        tableWidgetX.setSortingEnabled(False)  # 设置排序关闭

    # 添加tableWidget内容通用函数
    def chaxun(self, tableWidgetX: QTableWidgetItem, text: str, headerText: list):
        """
        查询显示显示对应数据，并清空列表控件项
        :param tableWidgetX: 列表控件项名称
        :param text: 使用的MySQL语句
        :param headerText: 需要显示的内容
        """
        tableWidgetX.setSortingEnabled(False)  # 设置排序关闭
        tableWidgetX.clearContents()   # 清空表格内容
        tableWidgetX.setRowCount(0)    # 设置数据区行数
        rows = self.cur.execute(text)
        for i in range(rows):
            item = self.cur.fetchone()                  # 获取一组数组
            row = tableWidgetX.rowCount()   # 获得QTableWidget表格控件的行数
            tableWidgetX.insertRow(row)     # 插入行
            for j in range(len(headerText)):
                if item[headerText[j]] is not None:
                    items = QTableWidgetItem(item[headerText[j]])
                    tableWidgetX.setItem(i, j, items)
                else:
                    pass
        # tableWidgetX.resizeRowsToContents()  # 自动行高
        # tableWidgetX.resizeColumnsToContents()  # 自动列宽

        #设置表格头的伸缩模式，也就是让表格铺满整个QTableWidget控件
        # self.ui.ryxx_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        str="QHeaderView::up-arrow { subcontrol-position: center right; padding-right: 1px;" \
            "image: url(ICO/ico/247.ico);}" + \
            "QHeaderView::down-arrow { subcontrol-position: center right; padding-right: 1px;" \
            "image: url(ICO/ico/248.ico);}"
        tableWidgetX.horizontalHeader().setStyleSheet(str)         #修改排序图标的展现方式（修改图标、位置）
        tableWidgetX.horizontalHeader().setSortIndicatorShown(True)        # 显示排序图标
        tableWidgetX.setSortingEnabled(True)            # 设置排序已启用
        self.cur.close()


    # 数据库连接
    def connect_db(self):
        """
        MySQL数据库连接
        """
        try:
            file = open('my.ini', 'r')
            L = []
            while True:
                d = file.readline()
                if not d:
                    file.close()  # 关闭文件
                    break
                cc = d.split('=')[1].strip()
                L.append(cc)
            # # 建立数据库连接
            db = pymysql.connect(
                host=L[0],  # 'localhost',  # "192.168.202.1""127.0.0.1"
                port=int(L[1]),  # 3306
                user=L[2],  # 'root'
                password=L[3],  # '080420'
                db=L[4],  # 'mysql'
                charset=str(L[5]))  # 字体设置"utf8"
            return db
        except IOError:
            QMessageBox.about(self, '提示信息', '服务器链接失败')


    #获取MySql某个表所有字段名
    def description(self,sql):
        """
        获取MySql某个表所有字段名
        sql = 'select * FROM 人员信息;'
        """
        result = self.cur.execute(sql)      #sql = 'select * FROM 人员信息;'
        desc = self.cur.description
        for field in desc:
            print(field[0])
        self.cur.close()

        #举例
        # db = DuiXiang().connect_db()
        # cursor = db.cursor()
        # sql = 'select * FROM 人员信息;'
        # # result = cursor.execute(sql)
        # desc = cursor.description
        # for field in desc:
        #     print(field[0])
        # cursor.close()



# QLineEdit日期显示
class DateEdit(QDateEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCalendarPopup(True)
        self.clear()  # 设置初始文本为空串
        self.dateChanged.connect(self.onDateChanged)  # 当日期改变时触发槽函数
        self.setDate(QDate.currentDate())
        self.calendarWidget().clicked.connect(lambda: {
            # 选择日期后，Edit 根据内容会自动调用 textFromDateTime 设置最终的显示文本。
            self.lineEdit().setText(self.text() or " ")
        })

    def setDateTime(self, dateTime: QDate):
        """调用 super.setDateTime 后，Edit 会自动根据该 dateTime 格式设置最终的显示文本。"""
        self.lineEdit().setText(dateTime.toString())
        super().setDateTime(dateTime)

    def validate(self, input: str, pos: int):
        """时间验证器：not input 允许接受空值"""
        if not input:
            return QValidator.Acceptable, '', 0
        return super().validate(input, pos)

    def textFromDateTime(self, dateTime: QDate):
        """
        每当需要显示 dateTime 时，Edit 就会使用此虚拟函数。
        如果重新实现，则可能还需要重新实现 validate()。
        :param dateTime: 当前 Edit 设置的日期，默认为 2000-1-1
        :return: dateTime 对应格式的日期字符串，如果 Edit 文本非空，则将自动设置为 Edit 的显示文本。
        """
        if not self.text():
            return ''
        return super().textFromDateTime(dateTime)

    def clear(self):
        self.lineEdit().clear()


    def onDateChanged(self):
        # 日期发生改变时执行
        if self.date() == QDate(2000, 1, 1):
            self.setDate(QDate.currentDate())  # 设置当前日期


