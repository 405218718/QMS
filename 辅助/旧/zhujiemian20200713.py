import sys
from datetime import datetime

import pymysql
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QMainWindow, QTabBar, \
    QTableWidgetItem, QAbstractItemView, QLineEdit, QAction, QHeaderView, QCalendarWidget, QDesktopWidget
from 主界面 import Ui_MainWindow
from PySide2.QtCore import Slot, QDate, QDateTime

L = []
bt = '飞云信息管理平台'     # 窗体标题
tb = "ICO/主题.png"       # 窗体图标
class zhujiemian(QMainWindow):
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
        week = datetime.now().isocalendar()[1]    #当前日期的三元组（年号，第几周，第几天）
        riqi0 = curDateTime.toString("yyyy年MM月dd日  dddd  " + '%s周'%week)     #日期与星期
        riqi = QLabel(riqi0)
        self.ui.statusBar.addPermanentWidget(riqi)      #addPermanentWidget为右侧，showMessage为左侧


        self.ui.statusBar.addWidget(qiye)  # 加到状态栏
        self.ui.statusBar.addWidget(gonghao)
        self.ui.statusBar.addWidget(xingming)
        self.ui.statusBar.addWidget(bumen)
        self.ui.statusBar.addWidget(zhiwei)
        cur = db.cursor(pymysql.cursors.DictCursor)

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

        # 使用父级构造一个空的日期编辑器。日期设置为date。
        sty = "QDateEdit :: QDateEdit（const QDate＆date，QWidget * parent = nullptr）"
        self.ui.xmxx_Q_riqi.setStyleSheet(sty)

        self.ui.ZhuCaiDan.setCurrentIndex(0)  # 显示第一个选项卡
        self.ui.ZhuCaiDan.setTabsClosable(True)  # 所有选项加上关闭按钮
        self.ui.ZhuCaiDan.tabBar().setTabButton(0, QTabBar.RightSide, None)  # 第一项去掉关闭按钮
        # self.ui.ZhuCaiDan.tabBar().setTabButton(1, QTabBar.RightSide, None)
        # # 第二项去掉关闭按钮
        u = self.ui.ZhuCaiDan.count()  # 获取选项卡数量
        # 删除多余选项卡
        while u > 0:
            self.ui.ZhuCaiDan.removeTab(u)
            u = u - 1
        self.ui.ZhuCaiDan.tabCloseRequested.connect(
            self.close_tab)  # ZhuCaiDan(页)关闭函数取消

        # 窗体居中设置
        deskSize = QDesktopWidget().screenGeometry()       # 获取桌面窗体参数
        windowSize = self.geometry()    # 获取窗体本身参数
        self.move((deskSize.width() - windowSize.width()) / 2,
                  (deskSize.height() - windowSize.height()) / 2-30)  # 居中设置


        # self.LineEdit_Date()
        self.riqikuangxuanxiang(self.ui.ryxx_Q_riqi, self.ui.renyuanxinxi)  # 创建日历控件
        self.riqikuangxuanxiang(self.ui.ryxx_J_riqi, self.ui.renyuanxinxi)

    # ZhuCaiDan(页)关闭函数；
    def close_tab(self, index):
        # currentTab = self.ui.ZhuCaiDan.currentWidget()
        currentTab = self.ui.ZhuCaiDan.widget(index)  # 获取选项卡的值

        del self.tab[currentTab.objectName()]  # 获取选项卡命名（objectName），删除对应数组
        self.ui.ZhuCaiDan.removeTab(index)  # 隐藏选项卡

    # 添加日期控件
    def LineEdit_Date(self):
        self.show_action = QAction(self)  # 创建控件
        self.show_action.setIcon(QIcon('ICO/png/1234864.png'))  # 设置控件图标
        self.ui.ryxx_Q_riqi.addAction(self.show_action, QLineEdit.TrailingPosition)  # 控件放置位置
        self.ui.ryxx_J_riqi.addAction(self.show_action, QLineEdit.TrailingPosition)  # 控件放置位置

    # 添加指定选项卡，显示按钮
    @Slot(bool)
    def on_actFont_ranyuanchaxun_triggered(self, clicked):
        # self.ui.actFont_ranyuanchaxun.triggered.connect(self.add_tab_renyuanxinxi)
        # # 新增选项卡（标题等同）
        self.tab['renyuanxinxi'] = [
            "部门",
            "组别",
            "职位",
            "工号",
            "姓名",
            "性别",
            "联系电话",
            "入职日期",
            "出生日期",
            "身份证号码",
            "地址",
            "待遇",
            "调薪日期",
            "离职日期",
            "备注"]
        self.add_tab(
            self.ui.renyuanxinxi,
            '人员信息',
            self.tab['renyuanxinxi'],
            self.ui.ryxx_tableWidget)

    # 添加tableWidgetn内容，查询按钮
    @Slot()
    def on_ryxx_chaxun_clicked(self):
        # self.ui.ryxx_chaxun.clicked.connect(self.chaxun_ryxx)   # 查询按钮
        text = "select * FROM 人员信息;"
        self.chaxun(self.ui.ryxx_tableWidget, text, self.tab['renyuanxinxi'])

    # 退出按钮
    @Slot()
    def on_ryxx_tuichu_clicked(self):
        index = self.ui.ZhuCaiDan.currentIndex()   # 获取当前选项卡的值
        self.ui.ZhuCaiDan.removeTab(index)  # 隐藏选项卡



    @Slot(bool)
    def on_actFont_xiangmuxinxi_triggered(self, clicked):
        # self.ui.actFont_xiangmuxinxi.triggered.connect(self.add_tab_xiangmuxingxi)
        # # 新增选项卡
        self.tab['xiangmuxinxi'] = [
            "内部编号",
            "客户编号",
            "模具等级",
            "业务担当",
            "项目担当",
            "设计担当",
            "钳工担当",
            "钳工组别",
            "下单日期",
            "首样日期",
            "预验日期",
            "复验日期",
            "终验日期",
            "要求移模日期",
            "实际移模日期",
            "出货判定",
            "备注"]
        self.add_tab(
            self.ui.xiangmuxinxi,
            '项目信息',
            self.tab['xiangmuxinxi'],
            self.ui.xmxx_tableWidget)

    @Slot()
    def on_xmxx_chaxun_clicked(self):
        text = "select * FROM 项目信息;"
        self.chaxun(self.ui.xmxx_tableWidget, text, self.tab['xiangmuxinxi'])

    @Slot()
    def on_xmxx_tuichu_clicked(self):
        index = self.ui.ZhuCaiDan.currentIndex()   # 获取当前选项卡的值
        self.ui.ZhuCaiDan.removeTab(index)  # 隐藏选项卡

    # 添加选项卡通用函数
    def add_tab(self,tab: QWidget,biao_ti: str,biao_tou: list,tableWidgetX: QTableWidgetItem):
        # self.add_tab(self.ui.xiangmuxinxi, '项目信息', headerText, self.ui.tableWidget_xm)
        while self.ui.ZhuCaiDan.indexOf(tab) < 0:
            self.ui.ZhuCaiDan.addTab(tab, biao_ti)      # 添加选项卡tab，以及标题biao_ti
            tableWidgetX.setColumnCount(len(biao_tou))  # 设置列数
            tableWidgetX.setRowCount(0)                 # 设置数据区行数
            tableWidgetX.setHorizontalHeaderLabels(biao_tou)  # 设置列命名biao_tou
            tableWidgetX.setAlternatingRowColors(True)  # 交替行颜色
            selMode = QAbstractItemView.SelectRows
            tableWidgetX.setSelectionBehavior(selMode)  # 选择行为：行选择
            # selMode = QAbstractItemView.SelectItems
            # self.ui.ryxx_tableWidget.setSelectionBehavior(selMode)
            # ##选择行为：单元格选择

        w = self.ui.ZhuCaiDan.indexOf(tab)
        self.ui.ZhuCaiDan.setCurrentIndex(w)
        tableWidgetX.setSortingEnabled(False)  # 设置排序关闭

    # 添加tableWidget内容通用函数
    def chaxun(self,tableWidgetX: QTableWidgetItem,text: str,headerText: list):
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
        tableWidgetX.resizeRowsToContents()  # 自动行高
        # tableWidgetX.resizeColumnsToContents()  # 自动列宽

        #设置表格头的伸缩模式，也就是让表格铺满整个QTableWidget控件
        # self.ui.ryxx_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        str="QHeaderView::up-arrow { subcontrol-position: center right; padding-right: 1px;" \
            "image: url(ICO/ico/247.ico);}" + \
            "QHeaderView::down-arrow { subcontrol-position: center right; padding-right: 1px;" \
            "image: url(ICO/ico/248.ico);}"
        tableWidgetX.horizontalHeader().setStyleSheet(str)         #修改排序图标的展现方式（修改图标、位置）
        # tableWidgetX.setSortIndicatorShown(bool show)
        # connect(tableWidgetX.horizontalHeader(), SIGNAL(sectionClicked(int)),
        #         tableWidgetX, SLOT(sortByColumn(int)))  # 连接信号与槽
        # tableWidgetX.horizontalHeader().setSortIndicator(0, AscendingOrder)
        # tableWidgetX.horizontalHeader().setClickable(true)
        tableWidgetX.horizontalHeader().setSortIndicatorShown(True)        # 显示排序图标
        tableWidgetX.setSortingEnabled(True)            # 设置排序已启用
        # tableWidgetX.sortItems(2,Qt.DescendingOrder)    # Qt.AscEndingOrder升序,Qt.DescendingOrder降序

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


    # QLineEdit日期显示
    def riqikuangxuanxiang(self,zujian:QLineEdit,jiemian:QWidget):
        # zujian.setInputMask("0000-00-00")   #格式限制

        # for i in range(4):
        #     name = zujian.objectName() + str(i)
        #     # locals()['v' + str(i)] = i
        #     print(name)



        # self.show_action = zujian.objectName()
        # self.rili = jiemian.objectName()
        # print(self.show_action)
        # print(self.rili)
        zj = zujian.objectName()
        jm = jiemian.objectName()
        self.show_action = locals()  #为了生成多个变量
        self.rili = locals()

        self.show_action[zj] = QAction(self)                        #创建控件
        self.show_action[zj].setIcon(QIcon('ICO/png/1234864.png'))  #设置控件图标
        zujian.addAction(self.show_action[zj], QLineEdit.TrailingPosition)  #控件放置位置
        self.show_action[zj].triggered.connect(self.openCalendar)    # 信号和槽连接
        self.rili[jm] = QCalendarWidget(jiemian)
        self.rili[jm].selectedDate()  # 获取选中日期，默认当前系统时间
        self.rili[jm].setGridVisible(True)  # 是否显示日期之间的网格
        self.rili[jm].setGeometry(zujian.x(),zujian.y()+zujian.height()+62, 280, 200)     #日历控件位置
        self.rili[jm].hide()  # 隐藏日期控件
        # date = self.rili.selectedDate()#获取选中日期，默认当前系统时间
        self.rili[jm].clicked[QDate].connect(self.showDate)#clicked[参数]，即定义showDate是传入的参数类型设置
        self.rili = self.rili[jm]

        # self.show_action.triggered.connect(self.showDate(date,zujian))

    def showDate(self,date):
        self.ui.ryxx_J_riqi.setText(date.toString("yyyy/MM/dd"))
        # self.rili.close()#关闭日期控件
        self.rili.hide()  # 隐藏日期控件
    def openCalendar(self):
        if self.rili.isHidden():
            self.rili.show()  # 显示日期控件
        else:
            # self.rili.close()  # 关闭日期控件
            self.rili.hide()  # 隐藏日期控件
class rili(QCalendarWidget):
    def __init__(self, parent=None):
        super(rili, self).__init__(parent=parent)
        self.ui = Ui_MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = zhujiemian()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())
