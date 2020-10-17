import pymysql
import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtCore import Qt
from 登陆 import Ui_Form
from zhujiemian import zhujiemian


class dengluUI(QMainWindow):
    def __init__(self, parent=None):
        # 加载方法三
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面


        # #美化界面，删除原生边框，设置窗口透明度
        # elf.setFixedSize(self.ui.width(), self.ui.height())  # 禁止拉伸窗口大小
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 禁止最大化按钮
        self.setWindowOpacity(0.90)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # self.setStyleSheet("background-image: url(media/background.png)")  #
        # 设置窗口背景图片

        # 提取数据库连接
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
            self.ui.fuwuqiID.setText(L[0])
            self.ui.fuwuduankou.setText(L[1])
            self.ui.fuwuqizhanghao.setText(L[2])
            self.ui.fuwuqimima.setText(L[3])
            self.ui.shujukuming.setText(L[4])
            self.ui.zhanghao.setText(L[len(L) - 1])
        except IOError:
            # self.ui.shezhi_2.clicked.connect(self.shezhi_clicked)
            QMessageBox.about(self, '提示信息', '服务器设置错误')
            self.ui.tabWidget.setCurrentIndex(1)

        #pane 指整个tab组件 ，border-width 组件的外框宽度， border-color 外框颜色， border-style外框风格，
        #比如outset就是凸出立体感，border-radius  外框的圆角像素。而本示例是无外框，无背景图的。
        str = "QTabWidget::pane{border-width: 0px;border-color:white;border-" \
              "style:outset;background-color: rgb(250, 250, 250);border-radius: 3px;}"
        self.ui.tabWidget.setStyleSheet(str)


        # 功能键
        self.ui.denglu_2.clicked.connect(self.denglu_clicked)
        self.ui.shezhi_2.clicked.connect(self.shezhi_clicked)
        self.ui.queren.clicked.connect(self.queren_clicked)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

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
            self.ui.tabWidget.setCurrentIndex(0)
            return db

        except pymysql.err.OperationalError:
            QMessageBox.about(self, '提示信息', '连接数据库失败')
            # exit()

    def denglu_clicked(self):
        zhanghao = self.ui.zhanghao.text()
        mima = self.ui.mima.text()
        db = self.connect_db()
        # 获取游标
        cur = db.cursor(pymysql.cursors.DictCursor)  # 使用字典类型输出
        sql_renyuan = "select * FROM 人员信息 WHERE 工号 = %s"
        rows = cur.execute(sql_renyuan, zhanghao)  # 条数
        if rows == 0:
            QMessageBox.about(self, '提示信息', '用户名或密码错误')
            return
        else:
            results = cur.fetchall()  # 查询到的字典组数
            jieguo = results[rows - 1]  # 提取最后一个字典
            mm = jieguo['密码']  # 获取字典里的‘密码’对应值
            if mm == mima:
                QMessageBox.about(self, '提示信息', '登录成功')
                cur.close()  # 关闭游标
                db.close()  # 关闭连接

                data = ''
                with open('my.ini', 'r+') as file:
                    for line in file.readlines():
                        if (line.find('工号') == 0):
                            line = '工号 = %s' % self.ui.zhanghao.text() + '\n'
                        data += line

                with open('my.ini', 'r+') as file:
                    file.writelines(data)
                file.close()
                self.main_window = zhujiemian()
                self.close()
                self.main_window.show()

            else:
                QMessageBox.about(self, '提示信息', '用户名或密码错误')
                return

    def shezhi_clicked(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def queren_clicked(self):
        try:
            self.connect_db()
            file = open('my.ini', 'w')
            file.write('host = ' + self.ui.fuwuqiID.text())
            file.write('\n')
            file.write('port = ' + self.ui.fuwuduankou.text())
            file.write('\n')
            file.write('user = ' + self.ui.fuwuqizhanghao.text())
            file.write('\n')
            file.write('password = ' + self.ui.fuwuqimima.text())
            file.write('\n')
            file.write('db = ' + self.ui.shujukuming.text())
            file.write('\n')
            file.write('charset = utf8')
            file.write('\n')
            file.write('工号 = 123456')
            file.write('\n')
            file.close()

        except IOError:
            QMessageBox.about(self, '提示信息', "保存失败")
            print("保存失败")

# 显示登陆界面


class denglu_ui():
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = dengluUI()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication


if __name__ == "__main__":
    denglu_ui()
