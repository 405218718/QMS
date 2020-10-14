import pymysql
import sys
from PySide2.QtWidgets import QApplication, QMessageBox, QWidget,QLineEdit
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile,Qt
from 登陆 import Ui_Form

# 加载方法二
ui_denglu =QFile("登陆.ui")
ui_zhujiemian =QFile("主界面A2.ui")
#登陆界面
class dengluUI(QWidget):
    def __init__(self, parent=None):
        #加载方法一
        # # 从文件中加载UI定义
        # # 从 UI 定义中动态 创建一个相应的窗口对象
        # # 注意：里面的控件对象也成为窗口对象的属性了
        # # 比如 self.ui.button , self.ui.textEdit
        #self.ui = QUiLoader().load("登陆.ui")

        # 加载方法二
        ui_denglu.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(ui_denglu)

        # 加载方法三
        # super().__init__(parent)  # 调用父类构造函数，创建窗体
        # self.ui = Ui_Form()  # 创建UI对象
        # self.ui.setupUi(self)  # 构造UI界面

        # 美化界面，删除原生边框，设置窗口透明度
        # self.ui.setFixedSize(self.ui.width(), self.ui.height())  # 禁止拉伸窗口大小
        # self.ui.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 禁止最大化按钮
        # self.ui.setWindowOpacity(0.95)  # 设置窗口透明度
        # self.ui.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.ui.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # # self.setStyleSheet("background-image: url(media/background.png)")  # 设置窗口背景图片
        # self.ui.tabWidget.setEnabled(QLineEdit.Password) #移动窗口

        #提取数据库连接
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
        except IOError:
            QMessageBox.about(self.ui, '提示信息', '打开文件失败')
        self.ui.fuwuqiID.setText(L[0])
        self.ui.fuwuduankou.setText(L[1])
        self.ui.fuwuqizhanghao.setText(L[2])
        self.ui.fuwuqimima.setText(L[3])
        self.ui.shujukuming.setText(L[4])

        #功能键
        self.ui.denglu_2.clicked.connect(self.denglu_clicked)
        self.ui.shezhi_2.clicked.connect(self.shezhi_clicked)
        self.ui.queren.clicked.connect(self.queren_clicked)



    def connect_db(self):
        try:
            # 建立数据库连接
            # db = pymysql.connect("localhost","root","080420","mysql",charset="utf8")
            db = pymysql.connect(
                host=self.ui.fuwuqiID.text(),  # 'localhost',  # "192.168.202.1""127.0.0.1"
                port=int(self.ui.fuwuduankou.text()),  # 3306
                user=self.ui.fuwuqizhanghao.text(),  # 'root'
                password=self.ui.fuwuqimima.text(),  # '080420'
                db=self.ui.shujukuming.text(),  # 'mysql'
                charset='utf8')  # 字体设置
            return db

        except pymysql.err.OperationalError:
            QMessageBox.about(self.ui, '提示信息', '连接数据库失败')
            exit()

    def denglu_clicked(self):
        zhanghao = self.ui.zhanghao.text()
        mima = self.ui.mima.text()
        db = self.connect_db()
        # 获取游标
        cur = db.cursor(pymysql.cursors.DictCursor)  # 使用字典类型输出
        sql_renyuan = "select * FROM 人员信息 WHERE 工号 = %s"
        rows = cur.execute(sql_renyuan, zhanghao)  # 条数
        results = cur.fetchall()  # 查询到的字典组数
        jieguo = results[rows - 1]  # 提取最后一个字典
        mm = jieguo['密码']  # 获取字典里的‘密码’对应值
        if mm == mima:
            QMessageBox.about(self.ui,'提示信息','登录成功')
            cur.close() # 关闭游标
            db.close() # 关闭连接

            self.main_window = zhujiemianUI()
            self.ui.close()
            self.main_window.ui.show()
            login_succeed = True
        else:
            QMessageBox.about(self.ui,'提示信息','用户名或密码错误')
            return

        # for (name, address) in results:
        #     print("%s家的地址是%s" % (name, address))

    def shezhi_clicked(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def queren_clicked(self):
        self.connect_db()
        try:
            file = open('my.ini', 'w')
            file.write('host = '+self.ui.fuwuqiID.text())
            file.write('\n')
            file.write('port = '+ self.ui.fuwuduankou.text())
            file.write('\n')
            file.write('user = '+self.ui.fuwuqizhanghao.text())
            file.write('\n')
            file.write('password = '+self.ui.fuwuqimima.text())
            file.write('\n')
            file.write('db = '+self.ui.shujukuming.text())
            file.write('\n')
            file.write('charset = utf8')
            file.write('\n')
            file.close()
        except IOError:
            print("保存失败")
        self.ui.tabWidget.setCurrentIndex(0)



#主界面
class zhujiemianUI(QWidget):
    def __init__(self):
        # # 从文件中加载UI定义
        # # 从 UI 定义中动态 创建一个相应的窗口对象
        # # 注意：里面的控件对象也成为窗口对象的属性了
        # # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load("主界面A2.ui")






#显示登陆界面
class denglu_ui():
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = dengluUI()  # ui是Ui_MainWindow()类的实例化对象
    form.ui.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


if __name__ == "__main__":
    denglu_ui()