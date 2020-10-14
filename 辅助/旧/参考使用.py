import pymysql
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

# 登陆
# 从文件中加载UI定义
# 从 UI 定义中动态 创建一个相应的窗口对象
# 注意：里面的控件对象也成为窗口对象的属性了
# 比如 self.ui.button , self.ui.textEdit
denglu_ui = QUiLoader().load("登陆.ui")


class denglu(QApplication, denglu_ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)  # 该方法派生自UI类
        # 定义拖拽窗口标记
        self.m_flag = False
        self.m_Position = None
        # 处理按钮逻辑
        self.handle_buttons()
        # 设置程序图标
        # self.setWindowIcon(QIcon("media/workbench.ico"))
        # 美化界面，删除原生边框，设置窗口透明度
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸窗口大小
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁止最大化按钮
        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setStyleSheet("background-image: url(media/background.png)")  # 设置窗口背景图片
        # 设置密码输入框
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    def lianjie(self):
        # 建立数据库连接
        # db = pymysql.connect("localhost","root","080420","mysql",charset="utf8")
        db = pymysql.connect(
            host='localhost',  # "192.168.202.1""127.0.0.1"
            port=3306,
            user='root',
            password='080420',
            db='mysql',
            charset='utf8')

        # 获取游标
        cur = db.cursor(pymysql.cursors.DictCursor)
        sql_renyuan = "select * from 人员信息;"
        rows = cur.execute(sql_renyuan)
        results = cur.fetchall()
        print(rows)  # 条数
        # for (name, address) in results:
        #     print("%s家的地址是%s" % (name, address))
        print(cur.fetchone())
        print(cur.fetchone())
        print(cur.fetchone())
        print(cur.fetchone())
        # 关闭游标
        cur.close()

        # 关闭连接
        db.close()
        print(rows)


# 创建实例
app = QApplication([])
Denglu = denglu()
Denglu.ui.show()
app.exec_()
