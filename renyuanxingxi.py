import os
import sys

import cv2
import pymysql
import xlwings as xw
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from ShuJuKuCaoZuo import DuiXiang as DX, DateEdit, GongSiMing
from 人员信息 import Ui_renyuanxinxi
from 人员信息查看 import UI_ryxxck
from RenYuanXingXi_LuRu import UI_ryxxlr

# 数据库切换 connect_db.select_db('库名')
class UI_ryxx(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_renyuanxinxi()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.Text_QiShi_RiQi = DateEdit(self.ui.Text_QiShi_RiQi)
        self.Text_QiShi_RiQi.resize(self.ui.Text_QiShi_RiQi.width(),
                                    self.ui.Text_QiShi_RiQi.height())
        self.Text_JieShu_RiQi = DateEdit(self.ui.Text_JieShu_RiQi)
        self.Text_JieShu_RiQi.resize(self.ui.Text_JieShu_RiQi.width(),
                                    self.ui.Text_JieShu_RiQi.height())

        self.ui.Text_ShaiXuan.clear()
        provinces = ["在职人员", "全部人员", "离职人员", "入职日期", "生日日期"]  # 列表数据
        self.ui.Text_ShaiXuan.addItems(provinces)  # 直接添加列表，但无法加图标

        self.tab = {}  # 空字典
        # # 新增选项卡（标题等同）
        self.tab['renyuanxinxi'] = ["部门", "组别", "职位", "工号", "姓名", "性别", "联系电话", "入职日期", "出生日期",
                                    "身份证号码", "地址", "待遇", "调薪日期", "离职日期", "备注"]
        DX.add_tab(self.tab['renyuanxinxi'], self.ui.Text_ShuJuXianShi)

    # 查询按钮
    @Slot(bool)
    def on_action_chaxun_triggered(self, clicked):
        # self.ui.ryxx_chaxun.clicked.connect(self.chaxun_ryxx)   # 查询按钮
        L = []
        if self.ui.Text_BuMen.currentText().strip() != "":
            L.append('部门 =\'%s\'' % self.ui.Text_BuMen.currentText().strip())
        if self.ui.Text_GongHao.text().strip() != "":
            L.append('工号 = \'%s\'' % self.ui.Text_GongHao.text().strip())
        if self.ui.Text_XingMing.text().strip() != "":
            L.append('姓名 = \'%s\'' % self.ui.Text_XingMing.text().strip())
        if self.ui.Text_ShaiXuan.currentText() != "全部人员":
            LiZhi = 'STR_TO_DATE(离职日期,\'%Y/%m/%d\')'
            RuZhi = 'STR_TO_DATE(入职日期,\'%Y/%m/%d\')'
            if self.ui.Text_ShaiXuan.currentText() == "在职人员":
                if self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() != "":
                    # 'STR_TO_DATE(离职日期, \'%Y-%m-%d\') BETWEEN STR_TO_DATE(起始时间, \'%Y-%m-%d\')'
                    L.append('(离职日期 = "" or ' + LiZhi + ' >= \'%s\')' % self.Text_QiShi_RiQi.text())
                    L.append(RuZhi + ' <= \'%s\'' % self.Text_JieShu_RiQi.text())
                elif self.Text_QiShi_RiQi.text() == "" and self.Text_JieShu_RiQi.text() == "":
                    L.append('离职日期 = ""')
                else:
                    QMessageBox.about(self, '提示信息', '日期范围不能只填一个')
                    return
            if self.ui.Text_ShaiXuan.currentText() == "离职人员":
                if self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('离职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text().strip())
                    L.append('离职日期 <= \'%s\'' % self.Text_JieShu_RiQi.text().strip())
                elif self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() == "":
                    L.append('离职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text().strip())
                elif self.Text_QiShi_RiQi.text() == "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('离职日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                else:
                    L.append('离职日期 != ""')
            if self.ui.Text_ShaiXuan.currentText() == "入职日期":
                if self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('入职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
                    L.append('入职日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                elif self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() == "":
                    L.append('入职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
                elif self.Text_QiShi_RiQi.text() == "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('入职日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                else:
                    QMessageBox.about(self, '提示信息', '日期范围不能为空')
                    return
            if self.ui.Text_ShaiXuan.currentText() == "生日日期":
                if self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('出生日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
                    L.append('出生日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                elif self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() == "":
                    L.append('出生日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
                elif self.Text_QiShi_RiQi.text() == "" and self.Text_JieShu_RiQi.text() != "":
                    L.append('出生日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                else:
                    QMessageBox.critical(self, '提示信息', '日期范围不能为空')
                    return
            s = "select * FROM 人员信息 WHERE " + " and ".join(L) + 'order by ID desc'
            # select * from AAAA order by BBBB desc limit 10   查询AAAA字段依据BBBB字段asc是表示升序，desc表示降序,查询10条记录
        else:
            s = 'select * FROM 人员信息;'
            # L.append('ShaiXuan = %s' % self.ui.Text_ShaiXuan.currentText())
        # if self.Text_QiShi_RiQi.text() != "" :
        #     L.append('RiQi >= %s' % self.Text_QiShi_RiQi.text())
        # if self.Text_JieShu_RiQi.text() != "":
        #     L.append('RiQi <= %s'% self.Text_JieShu_RiQi.text())

        # print(s)
        # if self.ui.Text_BuMen.currentText() != "":
        #     text_x = 'BuMen = %s' % self.ui.Text_BuMen.currentText()
        # text = 'select * FROM 人员信息;'
        DX().chaxun(self.ui.Text_ShuJuXianShi, s, self.tab['renyuanxinxi'])

    # 新增按钮
    @Slot(bool)
    def on_action_xinzeng_triggered(self, clicked):
        XinZeng = UI_ryxxlr(self)
        XinZeng.ZhuangTai = 0
        XinZeng.exec_()

    # 修改按钮
    @Slot(bool)
    def on_action_xiugai_triggered(self, clicked):
        row = self.ui.Text_ShuJuXianShi.currentRow()    # currentRow当前行号,currentColumn当前列号
        if row == -1:
            QMessageBox.information(self, '提示信息', '未选择需要的修改信息!')

        else:
            text = self.ui.Text_ShuJuXianShi.item(row, 3).text()   # 读取表格相对位置文本
            db = DX().connect_db()
            cur = db.cursor(pymysql.cursors.DictCursor)     # 使用字典类型输出
            sql_update = "select * FROM 人员信息 WHERE 工号 = %s order by ID desc limit 1"
            rows = cur.execute(sql_update, text)  # 查找对应的数据
            results = cur.fetchall()  # 查询到的字典组数
            jieguo = results[rows - 1]  # 提取最后一个字典
            UI_ryxxlr().xiugai(jieguo)

    # 删除按钮
    @Slot(bool)
    def on_action_shanchu_triggered(self, clicked):
        row = self.ui.Text_ShuJuXianShi.currentRow()    # currentRow当前行号,currentColumn当前列号
        if row == -1:
            QMessageBox.information(self, '提示信息', '未选择需要的删除信息!')
        else:
            text = self.ui.Text_ShuJuXianShi.item(row, 3).text()   # 读取表格相对位置文本
            text1 = self.ui.Text_ShuJuXianShi.item(row, 4).text()  # 读取表格相对位置文本
            # ret = QMessageBox.warning(self, '提示信息', '确定重置吗？？？!', QStringLiteral("确定"),QStringLiteral("取消"))
            msgbox = QMessageBox(self)  # 指定父窗口控件
            msgbox.setWindowTitle('提示信息')  # 对话框标题
            msgbox.setText("确定要删除  %s  %s   吗？？？" % (text, text1))  # 设置文本
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # 设置对话框有几个按钮
            msgbox.button(QMessageBox.Yes).setText("确定")    # 设置按钮文本
            msgbox.button(QMessageBox.No).setText("取消")     # 设置按钮文本
            # msgbox.button(QMessageBox.Cancel).setText("结束")   #还有abort,retry,ignore按钮
            # msgbox.setGeometry(500,500,0,0)     #消息框位置、大小设置
            msgbox.setIcon(QMessageBox.Warning)  # 图标图片：QMessageBox.Information信息框，QMessageBox.Question问答框，
            # QMessageBox.Warning警告框，QMessageBox.Ctitical危险框，QMessageBox.About关于框
            result = msgbox.exec() # 执行对话框，并获取返回值
            if result == QMessageBox.Yes:
                db = DX().connect_db()
                cur = db.cursor()
                sql_update = "delete FROM 人员信息 WHERE 工号 = %s order by ID desc limit 1"
                sql_updats = "select 入职照片 FROM 人员信息 WHERE 工号 = %s order by ID desc "
                try:
                    # 向sql语句传递参数
                    rows = cur.execute(sql_updats, text)  # 查找对应的数据
                    if rows == 1:
                        results = cur.fetchone()  # 查询结果（元组）
                        os.remove(results[0])  # 删除指定路径文件


                    cur.execute(sql_update, text)   # 查找对应的数据
                    # # 提交
                    db.commit()
                    self.ui.action_chaxun.trigger()     # 触发查询按钮,设置触发功能：triggered.connect(lambda:print("退出"))

                except Exception as e:
                    # 错误回滚
                    db.rollback()
                    QMessageBox.information(self, '提示信息', '操作失败!')

    # 查看功能
    @Slot(bool)
    def on_action_chakan_triggered(self, clicked):
        """
        在’人员信息查看‘内加入以下语句：
        class UI_ryxxck(QDialog):
            def __init__(self, parent=None):
                super().__init__(parent)  # 调用父类构造函数，创建窗体
                self.ui = Ui_Dialog()  # 创建UI对象
                self.ui.setupUi(self)  # 构造UI界面
        if __name__ == "__main__":
            app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
            form = UI_ryxxck()  # ui是Ui_MainWindow()类的实例化对象
            form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
            sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication

        :param clicked:
        :return:
        """
        row = self.ui.Text_ShuJuXianShi.currentRow()    # currentRow当前行号,currentColumn当前列号
        if row == -1:
            QMessageBox.information(self, '提示信息', '未选择需要的查看信息!')
        else:
            text = self.ui.Text_ShuJuXianShi.item(row, 3).text()   # 读取表格相对位置文本
            db = DX().connect_db()
            cur = db.cursor(pymysql.cursors.DictCursor)     # 使用字典类型输出
            sql_update = "select * FROM 人员信息 WHERE 工号 = %s order by ID desc limit 1"
            rows = cur.execute(sql_update, text)  # 查找对应的数据
            results = cur.fetchall()  # 查询到的字典组数
            sql = results[rows - 1]  # 提取最后一个字典

            dlgTableSize = UI_ryxxck(self)
            dlgTableSize.ui.Text_GongSiMingCheng.setText(GongSiMing)
            dlgTableSize.ui.Text_GongSiMingCheng.setAlignment(Qt.AlignCenter)   # AlignLeft 居左，AlignCenter居中，AlignRight居右

            # color: rgb()中的四个参数, 前三个是控制颜色, 第四个控制透明度
            # font - size: 设置字体大小
            # font - weight: bold可设置字体加粗
            # font - family: 选择自己想要的颜色
            dlgTableSize.ui.Text_GongSiMingCheng.setStyleSheet("QLabel{color:rgb(225,22,173,255);font-size:25px;font-weight:normal;font-family:Arial;}")
            dlgTableSize.ui.Text_GongSiMingCheng.adjustSize()  # 自适应函数->adjustSize()是继承于QWidget中
            dlgTableSize.ui.Text_DongHao.setText('编号：' + sql['工号'])
            dlgTableSize.ui.Text_DongHao.setAlignment(Qt.AlignCenter)

            dlgTableSize.ui.Text_XingMing.setText('姓 名：' + sql['姓名'])
            dlgTableSize.ui.Text_BuMen.setText('部 门：'+sql['部门'])
            dlgTableSize.ui.Text_ZhiWei.setText('职 位：' + sql['职位'])
            dlgTableSize.ui.Text_RuZhi_RiQi.setText('入职日期：' + sql['入职日期'])
            dlgTableSize.ui.Text_DianHua.setText('电 话：' + sql['联系电话'])

            Image = cv2.imread(sql['入职照片'])
            show = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            dlgTableSize.ui.Text_TuPian.setPixmap(QPixmap.fromImage(showImage))
            dlgTableSize.ui.Text_TuPian.setScaledContents(True)    # 入职照片
            dlgTableSize.exec_()

    # 导出数据
    @Slot(bool)
    def on_action_daochu_triggered(self, clicked):
        db = DX().connect_db()  # 获取游标
        cur = db.cursor(pymysql.cursors.DictCursor)  # 使用字典类型输出
        rows = cur.execute('select * FROM 人员信息;')   # 获取数组
        results = cur.fetchall()  # 查询到的字典组数
        titles = list(results[0].keys())   # 写入表头
        app = xw.App(visible=False, add_book=False)  # 创建应用
        # visible=True   显示Excel工作簿；False  不显示工作簿
        # add_book=False   不再新建一个工作簿;True  另外再新建一个工作簿
        # app.screen_updating = False
        # :屏幕更新，就是说代码对于excel的操作你可以看见，关闭实时更新可以加快脚本运行。默认是True。
        wb = app.books.add()    # 创建新的工作薄
        sht = wb.sheets.add("test")  # 新建工作表
        sht.range('a1').value = titles  # 写入表头
        info_list = []
        if rows != 0:
            n = 0
            while n < rows:
                info_list.append(list(results[n].values()))  # 保存的数据
                n = n+1
        sht.range('a2').value = info_list    # 写入数据
        wb.save(r'C:\Users\fanwei\Desktop\Track.xlsx')   # 保存工作簿
        wb.close()  # 关闭工作簿
        app.kill()  # 终止进程，强制退出。
        # quit()  # 在不保存的情况下，退出excel程序。
        # del info_list

    # 表头设置
    @Slot(bool)
    def on_action_biaotoushezhi_triggered(self, clicked):
        """
        ['ID', '部门', '组别', '职位', '工号', '姓名', '性别', '联系电话', '入职日期', '入职工龄', '合同日期', '离职日期',
         '待遇', '出生日期', '身份证号码', '地址', '密码', '紧急联系人', '紧急联系人电话', '调薪日期', '入职照片', '备注']
        库名：CREATE TABLE `人员信息` (
        ID自动递增：`id` bigint(100) NOT NULL AUTO_INCREMENT COMMENT '唯一不重复',PRIMARY KEY (`id`)
        其它内容设置：`部门` varchar(255) COLLATE utf8_estonian_ci DEFAULT NULL,
        结尾：) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci ROW_FORMAT=DYNAMIC;
        :param clicked:
        :return:
        """
        sql = 'select * FROM 人员信息;'
        biaotou = DX.HuoQuZiDuan(DX(), sql)

        print(biaotou)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxx()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
