import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from General import DuiXiang as DX, DateEdit
from 项目信息 import Ui_xiangmuxinxi
from renyuanxingxiluru import UI_ryxxlr

class UI_xmxx(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_xiangmuxinxi()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.Text_QiShi_RiQi = DateEdit(self.ui.Text_QiShi_RiQi)
        self.Text_QiShi_RiQi.resize(self.ui.Text_QiShi_RiQi.width(),
                                    self.ui.Text_QiShi_RiQi.height())
        self.Text_JieShu_RiQi = DateEdit(self.ui.Text_JieShu_RiQi)
        self.Text_JieShu_RiQi.resize(self.ui.Text_JieShu_RiQi.width(),
                                    self.ui.Text_JieShu_RiQi.height())
        # DX.DateEdit(self.ui.Text_QiShi_RiQi,self.ui.Text_JieShu_RiQi)
        self.tab = {}  # 空字典
        # # 新增选项卡（标题等同）
        self.tab['xiangmuxinxi'] = ["部门", "组别", "职位", "工号", "姓名", "性别", "联系电话", "入职日期", "出生日期",
                                    "身份证号码", "地址", "待遇", "调薪日期", "离职日期", "备注"]
        DX.add_tab(self.tab['xiangmuxinxi'], self.ui.Text_ShuJuXianShi)

    # # 新增按钮
    # @Slot(bool)
    # def on_action_xinzeng_triggered(self, clicked):
    #     dlgTableSize = UI_ryxxlr(self)
    #     dlgTableSize.show()

    # 查询按钮
    @Slot(bool)
    def on_action_chaxun_triggered(self, clicked):
        # self.ui.ryxx_chaxun.clicked.connect(self.chaxun_ryxx)   # 查询按钮
        L = []
        if self.ui.Text_BuMen.currentText() != "":
            L.append('BuMen = %s' % self.ui.Text_BuMen.currentText())
        if self.ui.Text_GongHao.text() != "":
            L.append('GongHao = %s' % self.ui.Text_GongHao.text())
        if self.ui.Text_XingMing.text() != "":
            L.append('XingMing = %s' % self.ui.Text_XingMing.text())
        if self.ui.Text_ShaiXuan.currentText() != "":
            L.append('ShaiXuan = %s' % self.ui.Text_ShaiXuan.currentText())
        if self.Text_QiShi_RiQi.text() != "" :
            L.append('RiQi >= %s ' % self.Text_QiShi_RiQi.text())
        if self.Text_JieShu_RiQi.text() != "":
            L.append('and'+' RiQi <= %s'% self.Text_JieShu_RiQi.text())
        print(L)

        # if self.ui.Text_BuMen.currentText() != "":
        #     text_x = 'BuMen = %s' % self.ui.Text_BuMen.currentText()



        text = "select * FROM 项目信息;"
        db = DX()
        DX.chaxun(db, self.ui.Text_ShuJuXianShi, text, self.tab['xiangmuxinxi'])

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_xmxx()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
