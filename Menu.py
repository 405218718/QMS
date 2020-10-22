import sys
from datetime import datetime
import pymysql
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, QLabel, QMainWindow, QTabBar
from PySide2.QtCore import Slot, QDate, QDateTime, Qt
from 主界面 import Ui_MainWindow
from RenYuanXingXi import UI_ryxx
from xiangmuxingxi import UI_xmxx

L = []
bt = '飞云信息管理平台'     # 窗体标题
tb = "ICO/主题.png"       # 窗体图标
class zhujiemian_UI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle(bt)  # 设置窗体标题
        self.setWindowIcon(QIcon(tb))   # 设置窗体图标
        # self.setStyleSheet("MainWindow{border-image:url(./python.jpg);}")  #设置窗口背景图片
        self.tab = {}  # 空字典

        global L
        db = self.connect_db()
        # 获取游标
        self.cur = db.cursor(pymysql.cursors.DictCursor)  # 使用字典类型输出
        # 根据” ID 字段“排序，倒叙输出 人员信息 表中的数据。备注：asc是表示升序，desc表示降序。limit 1表示输出一条记录
        sql_renyuan = "select * FROM 人员信息 WHERE 工号 = %s order by ID desc limit 1"
        rows = self.cur.execute(sql_renyuan, L[len(L) - 1])
        rows = self.cur.fetchone()
        qiye = QLabel(bt)           # 设置窗体标题
        qiye.setMinimumWidth(150)
        gonghao = QLabel("工号：%s" % L[len(L) - 1])
        gonghao.setMinimumWidth(120)
        xingming = QLabel("姓名：%s" % rows['姓名'])
        xingming.setMinimumWidth(120)
        bumen = QLabel("部门：%s" % rows['部门'])
        bumen.setMinimumWidth(120)
        zhiwei = QLabel("职位：%s" % rows['职位'])
        zhiwei.setMinimumWidth(120)

        curDateTime = QDateTime.currentDateTime()   #提取系统当前日期时间
        now = QDate.currentDate()  #获取当前日期
        week = datetime.now().isocalendar()[1]    #当前日期的三元组（年号，第几周，第几天）
        riqi0 = curDateTime.toString("yyyy年MM月dd日  dddd  " + '%s周  '%week + '第%s天  '%now.dayOfYear())     #日期与星期
        riqi = QLabel(riqi0)
        self.ui.statusBar.addPermanentWidget(riqi)      #addPermanentWidget为右侧，showMessage为左侧


        self.ui.statusBar.addWidget(qiye)  # 加到状态栏
        self.ui.statusBar.addWidget(gonghao)
        self.ui.statusBar.addWidget(xingming)
        self.ui.statusBar.addWidget(bumen)
        self.ui.statusBar.addWidget(zhiwei)
        # cur = db.cursor(pymysql.cursors.DictCursor)

        # 1.控件的上面的小tab变成透明
        # 2.选项卡部件：窗格{ 边框：1px纯灰；顶部：-1px；背景：透明；}
        # 3.突出选中的部分(改变颜色)
        # 4.设置QTabBar删除按钮图标和位置
        # 4.设置QTabBar删除按钮图标(点击前)
        # 4.设置QTabBar删除按钮图标(点击时)
        str = "QTabBar::tab{background-color:rbg(255,255,255,0);}" + \
              "QTabWidget:pane{border: 0.5px solid grey; top: -1px;background: transparent;}" + \
              "QTabBar::tab:selected{color:blue;background-color:rbg(255,255,255);} " + \
              "QTabBar::close-button{image: url(ICO/240.png);subcontrol-postion:left}" + \
              "QTabBar::close-button：hover{image:url(ICO/301.png);subcontrol-postion:left}" + \
              "QTabBar::close-button:pressed{image:url(ICO/302.png);subcontrol-postion:left}"

        self.ui.ZhuCaiDan.setStyleSheet(str)
        self.ui.ZhuCaiDan.setDocumentMode(True)
        self.ui.ZhuCaiDan.setCurrentIndex(0)  # 显示第一个选项卡
        self.ui.ZhuCaiDan.setTabsClosable(True)  # 所有选项加上关闭按钮
        self.ui.ZhuCaiDan.tabBar().setTabButton(0, QTabBar.RightSide, None)  # 第一项去掉关闭按钮
        self.ui.ZhuCaiDan.tabCloseRequested.connect(
            self.close_tab)  # ZhuCaiDan(页)关闭函数取消

        # self.setWindowState(Qt.WindowMaximized)  # 窗口最大化显示

        # # 窗体居中设置
        # deskSize = QDesktopWidget().screenGeometry()       # 获取桌面窗体参数
        # windowSize = self.geometry()    # 获取窗体本身参数
        # self.move((deskSize.width() - windowSize.width()) / 2,
        #           (deskSize.height() - windowSize.height()) / 2-30)  # 居中设置

    # ZhuCaiDan(页)关闭函数；
    def close_tab(self, index):
        currentTab = self.ui.ZhuCaiDan.widget(index)  # 获取选项卡的值
        del self.tab[currentTab.objectName()]  # 获取选项卡命名（objectName），删除对应数组
        self.ui.ZhuCaiDan.removeTab(index)  # 清除所选页面

    # 添加指定选项卡，显示按钮
    @Slot(bool)
    def on_actFont_ranyuanchaxun_triggered(self, clicked):
        if 'renyuanxinxi' in self.tab:
            self.ui.ZhuCaiDan.setCurrentIndex(self.tab['renyuanxinxi'])
        else:
            formDoc = UI_ryxx(self)
            formDoc.setAttribute(Qt.WA_DeleteOnClose)  # 关闭时自动删除
            title = "人员信息"  #选项卡的命名
            self.tab['renyuanxinxi'] = self.ui.ZhuCaiDan.count()
            curIndex = self.ui.ZhuCaiDan.addTab(formDoc, title)  # 添加选项卡formDoc，以及标题title
            self.ui.ZhuCaiDan.setCurrentIndex(curIndex)
            self.ui.ZhuCaiDan.setVisible(True)


    @Slot(bool)
    def on_actFont_xiangmuxinxi_triggered(self, clicked):
        if 'xiangmuxinxi' in self.tab:
            self.ui.ZhuCaiDan.setCurrentIndex(self.tab['xiangmuxinxi'])
        else:
            formDoc = UI_xmxx(self)
            formDoc.setAttribute(Qt.WA_DeleteOnClose)  # 关闭时自动删除
            title = "项目信息"  #选项卡的命名
            self.tab['xiangmuxinxi'] = self.ui.ZhuCaiDan.count()
            curIndex = self.ui.ZhuCaiDan.addTab(formDoc, title)  # 添加选项卡formDoc，以及标题title
            self.ui.ZhuCaiDan.setCurrentIndex(curIndex)
            self.ui.ZhuCaiDan.setVisible(True)

    # 数据库连接
    def connect_db(self):
        try:
            file = open('my.ini', 'r')
            global L
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

    # 窗口关闭提示
    def closeEvent(self, event):
        result = QMessageBox.question(
            self,
            '关闭提示框',
            '确定要退出吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.NoButton)
        if (result == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = zhujiemian_UI()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())
