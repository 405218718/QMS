import pymysql
from PySide2.QtGui import QValidator
from PySide2.QtWidgets import QMessageBox,QTableWidgetItem, QAbstractItemView,QDateEdit,QLineEdit
from PySide2.QtCore import QDate



class DuiXiang:
    GongSiMing = '飞云科技有限公司'  # 公司名称
    image = "E:\\QMS\\"  # 文件存储

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
    def HuoQuZiDuan(self,sql):
        """
        获取MySql某个表所有字段名
        sql = 'select * FROM 人员信息;'
        """
        biaotou = []
        result = self.cur.execute(sql)      #sql = 'select * FROM 人员信息;'
        desc = self.cur.description
        for field in desc:
            biaotou.append(field[0])
            # print(field[0])
        self.cur.close()
        return biaotou

        #举例
        # db = DuiXiang().connect_db()
        # cursor = db.cursor()
        # sql = 'select * FROM 人员信息;'
        # # result = cursor.execute(sql)
        # desc = cursor.description
        # for field in desc:
        #     print(field[0])
        # cursor.close()

    #新增表记录
    def XinZeng(self,sql_Table,values):
        """
        新增数据\n
        insert into 表名(字段名列表) values(值1),...(值N);
        \n param sql_Table: 表名(字段名列表)
           param values: (值1),...(值N)
        \n return:
        单条新增：rows=cursor.execute(sql,('4','qzcsbj4'))   \n
        多条新增：rows=cursor.executemany(sql,[('5','qzcsbj5'),('6','qzcsbj6'),('7','qzcsbj7')]) \n
        大批量新增\n
        values=[]\n
        for i in range(100, 201):\n
        values.append((i, 'qzcsbj'+str(i)))\n
        sql='insert into test(id,name) values(%s,%s)'\n
        rows=cursor.executemany(sql,values)
        """
        db = self.connect_db()
        cur = db.cursor()
        sql = "insert into %s values %s;"
        try:
            cur.execute(sql%(sql_Table,values)) # 执行sql语句
            db.commit() # 提交
            return 'ok'
        except Exception as e:
            db.rollback()   # 错误回滚
        finally:
            db.close()

    #修改表记录
    def XiuGgai(self,sql_Table,values,condition):
        """
        更新表记录
        1、update 表名 set 字段名1=值1,字段名2=值2,... where 条件;\n
        2、注意:update语句后如果不加where条件子句会将表中所有记录全部更改；
        \n param sql_Table: 表名
           param values: 字段名=值
           param condition: 条件
       \n return:
        sql='update test set name = %s where id = %s'
        rows=cursor.executemany(sql,[('全栈测试笔记5','5'),('全栈测试笔记6','6')])
        """
        db = self.connect_db()
        cur = db.cursor()
        sql_update = "update %s set %s where %s"
        try:
            cur.execute(sql_update%(sql_Table,sql_Table,values))
            # 提交
            db.commit()
            return 'OK'
        except Exception as e:
            # 错误回滚
            db.rollback()
        finally:
            db.close()

    #删除表记录
    def ShanChu(self,sql_Table,condition):
        """
        删除表记录
        1、delete from 表名 where 条件;\n
        2、注意:	delete语句后如果不佳where条件子句,会将表中所有记录全部删除
        \n param sql_Table:表名
           param condition:条件
        \n return:
        sql='delete from test where id = %s' \n
        单条删除：rows=cursor.execute(sql,('1',)) \n
        多条删除：rows=cursor.executemany(sql,[('2'),('3')])
        """
        # 使用cursor()获取操作游标
        db = self.connect_db()
        cur = db.cursor()
        sql_delete = "delete from %s where %s"
        try:
            # 向sql语句传递参数
            cur.execute(sql_delete,(sql_Table,condition))
            # 提交
            db.commit()
            return 'OK'
        except Exception as e:
            # 错误回滚
            db.rollback()
        finally:
            db.close()




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

    def setDateTime(self, date: QDate):
        """调用 super.setDateTime 后，Edit 会自动根据该 dateTime 格式设置最终的显示文本。"""
        self.lineEdit().setText(date.toString())
        super().setDate(date)

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

    def date_str(self, sql: str):
        """
        此函数只运用于字符串转日期
        :param sql: 日期字符串2020/01/01
        :return:
        """
        if sql != "":
            date = QDate(int(sql.split('/')[0]), int(sql.split('/')[1]), int(sql.split('/')[2]))
            self.lineEdit().setText(date.toString())
            super().setDate(date)
        else:
            self.clear()

    def onDateChanged(self):
        # 日期发生改变时执行
        if self.date() == QDate(2000, 1, 1):
            self.setDate(QDate.currentDate())  # 设置当前日期


