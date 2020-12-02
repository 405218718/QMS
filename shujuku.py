import pymysql

# DB = {}
# DB["host"] = L[0],  # 'localhost',  # "192.168.202.1""127.0.0.1"
# port = int(L[1]),  # 3306
# DB["user"] = L[2],  # 'root'
# DB["password"] = L[3],  # '080420'
# DB["db"] = L[4],  # 'mysql'
# DB["charset"] = str(L[5])  # 字体设置"utf8"

class jianli:

    def __init__(self):
        DB = {}
        DB["host"] = '127.0.0.1'  # input('host:')  # 'localhost',  # "192.168.202.1""127.0.0.1"
        # port = input('port:')   # 3306
        DB["user"] = 'root'     # input('user:')   # 'root'
        DB["password"] = '080420'   # input('password:')   # '080420'
        DB["db"] = input('db:')   # 'mysql'
        DB["charset"] = 'utf8'  # input('charset:')  # 字体设置"utf8"
        conn, cursor = self.get_sql_conn(DB)    # 创建、连接库
        renshixitong = ['ID', '部门', '组别', '职位', '工号', '姓名', '性别', '联系电话', '入职日期', '入职工龄', '合同日期', '离职日期',
                        '待遇', '出生日期', '身份证号码', '地址', '密码', '紧急联系人', '紧急联系人电话', '调薪日期', '入职照片', '备注']

        self.create_sql_tb(conn, cursor, '人员信息', renshixitong)



    # 连接
    def get_sql_conn(self, DB):
        """
        通过字典的方式连接,有一点好处,就是需要连接多个库、表的时候,可以创建多个字典,好区分.
        :return: 返回mysql数据库的连接与游标
        """
        try:
            conn = pymysql.connect(host=DB["host"], user=DB["user"], password=DB["password"], db=DB["db"], charset=DB["charset"])
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


    # # 创建《人员信息》表库
    # def create_sql_db(self, conn, cursor):
    #     sql = 'CREATE TABLE `人员信息`(`id` varchar(100) COLLATE utf8_estonian_ci NOT NULL COMMENT '唯一不重复', ' \
    #             '`部门` varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL, ' \
    #             'PRIMARY KEY(`id`)' \
    #             ') ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_estonian_ci ROW_FORMAT = DYNAMIC;'
    #     cursor.execute(sql)
    #     conn.commit()


    # 创建tablename表
    def create_sql_tb(self, conn, cursor, tablename, dataframe:list):
        """
        :param conn: 连接符
        :param cursor: 游标
        :param tablename: 创建的表名
        :param dataframe: 按照数据框的情况,创建列名、列的长度
        :return: 创建情况
        """
        print(' varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL,'.join(dataframe))
        # conn, cursor = get_sql_conn(DB)   # 数据库连接

        # list_Type, list_Len = find_dfm_cols_most(dataframe)
        # print(list_Type, list_Len)
        # list_colname = list(dataframe.columns)  # 新表的列名为数据框的列名
        # list_col_desc = []  # 列描述,sql语言
        # for i in range(len(list_colname)):
        #     print('正创建列:\t{} '.format(list_colname[i]))
        #     # col_limit = input('Please enter the limits of the column:\t')
        #     col_desc = list_colname[i] + ' ' + list_Type[i] + '(' + str(list_Len[i]) + ')' + col_limit
        #     list_col_desc.append(col_desc)
        sql = 'CREATE TABLE %s' % tablename + '(`ID` varchar(100) COLLATE utf8_estonian_ci NOT NULL COMMENT,' + \
              ' varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL,'.join(dataframe) + \
              ') ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_estonian_ci ROW_FORMAT = DYNAMIC;'  # 用于执行的sql语句
        # sql = sql.replace('datetime(0)', 'datetime')
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


jianli()