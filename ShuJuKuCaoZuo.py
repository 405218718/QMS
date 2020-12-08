import pymysql
from PySide2.QtCore import QDate
from PySide2.QtGui import QValidator
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QDateEdit

GongSiMing = '广东天倬智能装备科技有限公司'  # 公司名称
image = "E:\\QMS\\"  # 文件存储
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
            QMessageBox.about(self, '提示信息', '服务器链接失败')      # 图标图片：QMessageBox.information信息框，QMessageBox.question问答框，
        # QMessageBox.warning警告框，QMessageBox.ctitical危险框，QMessageBox.about关于框

    #获取MySql某个表所有字段名
    def HuoQuZiDuan(self, sql):
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
    def XinZeng(self, sql_Table, values):
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
            cur.execute(sql % (sql_Table, values))    # 执行sql语句
            db.commit()     # 提交
            return 'ok'
        except Exception as e:
            db.rollback()   # 错误回滚
        finally:
            db.close()

    #修改表记录
    def XiuGgai(self, sql_Table, values, condition):
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
    def ShanChu(self, sql_Table, condition):
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
            cur.execute(sql_delete, (sql_Table, condition))
            # 提交
            db.commit()
            return 'OK'
        except Exception as e:
            # 错误回滚
            db.rollback()
        finally:
            db.close()


class jianli:
    def __init__(self):
        DB = {}
        DB["host"] = '127.0.0.1'  # input('host:')  # 'localhost',  # "192.168.202.1""127.0.0.1"
        # port = input('port:')   # 3306
        DB["user"] = 'root'  # input('user:')   # 'root'
        DB["password"] = '080420'  # input('password:')   # '080420'
        DB["db"] = input('db:')  # 'mysql'
        DB["charset"] = 'utf8'  # input('charset:')  # 字体设置"utf8"
        conn, cursor = self.get_sql_conn(DB)  # 创建、连接库
        # renshixitong = ['部门', '组别', '职位', '工号', '姓名', '性别', '联系电话', '入职日期', '入职工龄', '合同日期', '离职日期',
        #                 '待遇', '出生日期', '身份证号码', '地址', '密码', '紧急联系人', '紧急联系人电话', '调薪日期', '入职照片', '备注']
        # self.create_sql_tb(conn, cursor, '人员信息', renshixitong)
        xiangmuxitong = ['项目编号', '产品编码', '类型', '等级', '尺寸', '业务担当', '项目担当', '设计担当', '装配担当', '下单日期',
                         '出货日期', '出货状态', '备注']
        self.create_sql_tb(conn, cursor, '项目信息', xiangmuxitong)
        # 项目计划 = ['厂内编号', '料条阶段', '结构阶段', '拆图阶段', '采购阶段', '加工阶段', '拼锣阶段', '首次试模', '全模样', 'OK样', '客户验收', '移模', '备注']
        # 外协记录 = ['送货单号', '申请单编码', '申请人', '模具编号', '页码', '工件名称', '工件规格', '材质', '数量', '单位', '加工方式', '加工种类', '加工商', '重量', '金额(含税)', '税率', '金额(未含税)', '创建日期', '要求交期', '出厂日期', '回厂日期', '是否结算', '对账月份', '付款日期', '审核人', '审核时间', '备注']

    # 连接
    def get_sql_conn(self, DB):
        """
        通过字典的方式连接,有一点好处,就是需要连接多个库、表的时候,可以创建多个字典,好区分.
        :return: 返回mysql数据库的连接与游标
        """
        try:
            conn = pymysql.connect(host=DB["host"], user=DB["user"], password=DB["password"], db=DB["db"],
                                   charset=DB["charset"])
            cursor = conn.cursor()
            # QMessageBox.about(self, '提示信息', '此数据库存在，已连接Mysql库成功.')      # 图标图片：QMessageBox.information信息框，QMessageBox.question问答框，
            # # QMessageBox.warning警告框，QMessageBox.ctitical危险框，QMessageBox.about关于框
            print("此数据库存在，已连接Mysql库成功.")
        except Exception as e:
            conn = pymysql.connect(host=DB["host"], user=DB["user"], password=DB["password"], charset=DB["charset"])
            cursor = conn.cursor()
            print("连接Mysql库失败:", e)
            self.create_sql_db(conn, cursor, DB["db"])
        return conn, cursor

    # 创建dbname库
    def create_sql_db(self, conn, cursor, dbname):
        """
        :param conn: 连接符
        :param cursor: 游标
        :param dbname: 需要创建的库名,str
        :return: 打印创建成果
        """
        # conn, cursor = get_sql_conn(DB)   # 数据库连接
        try:
            sql = 'CREATE DATABASE %s default character set utf8 collate utf8_general_ci ' % dbname
            cursor.execute(sql)
            print('创建库:\t{},成功.'.format(dbname))
            sql = 'USE %s' % dbname
            cursor.execute(sql)
            print('使用当前库：\t{}.'.format(dbname))
        except Exception as e:
            print("库:\t'{}'已经存在.\t{}".format(dbname, e))
            sql = 'USE %s' % dbname
            cursor.execute(sql)
            print('使用当前库:\t{}.'.format(dbname))
        finally:
            conn.commit()  # 提交事务
            print('\n\n')

    # 创建tablename表
    def create_sql_tb(self, conn, cursor, tablename, dataframe: list):
        """
        :param conn: 连接符
        :param cursor: 游标
        :param tablename: 创建的表名
        :param dataframe: 按照数据框的情况,创建列名、列的长度
        :return: 创建情况
        """
        list_col_desc = []
        for i in range(len(dataframe)):
            # print('正创建列:\t{} '.format(dataframe[i]))
            col_desc = '`' + dataframe[i] + '`' + ' varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL,'

            list_col_desc.append(col_desc)
        sql = 'CREATE TABLE `' + tablename + '` (`ID` varchar(100) COLLATE utf8_estonian_ci NOT NULL, ' + \
              ' '.join(list_col_desc) + \
              'PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci ROW_FORMAT=DYNAMIC;'
        try:
            cursor.execute(sql)
        except Exception as e:
            print('表名:{}已存在.'.format(e))
            select = input('选择是否覆盖建立该表(Y/N):')
            if select == 'Y' or 'y':
                sql1 = 'drop table if exists {}'.format(tablename)  # 删除表
                cursor.execute(sql1)
                sql = 'CREATE TABLE %s' % tablename + '(`ID` varchar(100) COLLATE utf8_estonian_ci NOT NULL COMMENT,' + \
                      'varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL,'.join(dataframe) + \
                      ') ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_estonian_ci ROW_FORMAT = DYNAMIC;'  # 用于执行的sql语句
                cursor.execute(sql)
                print('Rebuild table:\t{}'.format(tablename))
            elif select == 'N' or 'n':
                print('Opt out.')
        finally:
            conn.commit()


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

