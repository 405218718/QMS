import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from General import DuiXiang as DX, DateEdit
from 人员信息 import Ui_renyuanxinxi
from renyuanxingxiluru import UI_ryxxlr

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
        # DX.DateEdit(self.ui.Text_QiShi_RiQi,self.ui.Text_JieShu_RiQi)

        self.ui.Text_ShaiXuan.clear()
        provinces = ["在职人员", "全部人员", "离职人员", "入职日期", "生日日期"]  # 列表数据
        self.ui.Text_ShaiXuan.addItems(provinces)  # 直接添加列表，但无法加图标

        self.tab = {}  # 空字典
        # # 新增选项卡（标题等同）
        self.tab['renyuanxinxi'] = ["部门", "组别", "职位", "工号", "姓名", "性别", "联系电话", "入职日期", "出生日期",
                                    "身份证号码", "地址", "待遇", "调薪日期", "离职日期", "备注"]
        DX.add_tab(self.tab['renyuanxinxi'], self.ui.Text_ShuJuXianShi)

    # 新增按钮
    @Slot(bool)
    def on_action_xinzeng_triggered(self, clicked):
        dlgTableSize = UI_ryxxlr(self)
        dlgTableSize.show()

    # 查询按钮
    @Slot(bool)
    def on_action_chaxun_triggered(self, clicked):
        # self.ui.ryxx_chaxun.clicked.connect(self.chaxun_ryxx)   # 查询按钮
        L = []
        if self.ui.Text_BuMen.currentText() != "":
            L.append('部门 =\'%s\'' % self.ui.Text_BuMen.currentText())
        if self.ui.Text_GongHao.text() != "":
            L.append('工号 = \'%s\'' % self.ui.Text_GongHao.text())
        if self.ui.Text_XingMing.text() != "":
            L.append('姓名 = \'%s\'' % self.ui.Text_XingMing.text())
        if self.ui.Text_ShaiXuan.currentText() != "全部人员":
            LiZhi = 'STR_TO_DATE(离职日期,\'%Y/%m/%d\')'
            RuZhi = 'STR_TO_DATE(入职日期,\'%Y/%m/%d\')'
                    # if self.ui.Text_ShaiXuan.currentText() == "在职人员":
                    #     if self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() != "":
                    #         # 'STR_TO_DATE(离职日期, \'%Y-%m-%d\') BETWEEN STR_TO_DATE(起始时间, \'%Y-%m-%d\')'
                    #         L.append(LiZhi + ' = "" or ' + LiZhi + '>= \'%s\'' % self.Text_QiShi_RiQi.text())
                    #         L.append(RuZhi + ' <= \'%s\'' % self.Text_JieShu_RiQi.text())
                    #     elif self.Text_QiShi_RiQi.text() == "" and self.Text_JieShu_RiQi.text() == "":
                    #         L.append(LiZhi + ' = ""')
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
                    L.append('离职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
                    L.append('离职日期 <= \'%s\'' % self.Text_JieShu_RiQi.text())
                elif self.Text_QiShi_RiQi.text() != "" and self.Text_JieShu_RiQi.text() == "":
                    L.append('离职日期 >= \'%s\'' % self.Text_QiShi_RiQi.text())
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
                    QMessageBox.about(self, '提示信息', '日期范围不能为空')
                    return
            s = "select * FROM 人员信息 WHERE " + " and ".join(L)
        else:
            s = 'select * FROM 人员信息;'
            # L.append('ShaiXuan = %s' % self.ui.Text_ShaiXuan.currentText())
        # if self.Text_QiShi_RiQi.text() != "" :
        #     L.append('RiQi >= %s' % self.Text_QiShi_RiQi.text())
        # if self.Text_JieShu_RiQi.text() != "":
        #     L.append('RiQi <= %s'% self.Text_JieShu_RiQi.text())

        print(s)
        # if self.ui.Text_BuMen.currentText() != "":
        #     text_x = 'BuMen = %s' % self.ui.Text_BuMen.currentText()

        # text = 'select * FROM 人员信息;'
        db = DX()
        DX.chaxun(db, self.ui.Text_ShuJuXianShi, s, self.tab['renyuanxinxi'])

    # 表头设置
    @Slot(bool)
    def on_action_biaotoushezhi_triggered(self, clicked):
        s = "select * FROM 人员信息; "
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxx()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
