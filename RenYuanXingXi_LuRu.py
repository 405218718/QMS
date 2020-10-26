import pymysql
import sys
from PySide2.QtCore import Qt, QDate, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from General import DuiXiang as DX, DateEdit
from 人员信息录入 import Ui_Dialog



class UI_ryxxlr(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle('人员信息录入')  # 设置窗体标题
        self.Text_RuZhi = DateEdit(self.ui.Text_RuZhi_RiQi)
        self.Text_RuZhi.resize(self.ui.Text_RuZhi_RiQi.width(),self.ui.Text_RuZhi_RiQi.height())
        self.Text_LiZhi = DateEdit(self.ui.Text_HeTong_RiQi)
        self.Text_LiZhi.resize(self.ui.Text_HeTong_RiQi.width(), self.ui.Text_HeTong_RiQi.height())
        self.Text_LiZhi = DateEdit(self.ui.Text_TiaoXin_RiQi)
        self.Text_LiZhi.resize(self.ui.Text_TiaoXin_RiQi.width(), self.ui.Text_TiaoXin_RiQi.height())
        self.Text_LiZhi = DateEdit(self.ui.Text_LiZhi_RiQi)
        self.Text_LiZhi.resize(self.ui.Text_LiZhi_RiQi.width(), self.ui.Text_LiZhi_RiQi.height())
        # self.ui.Text_XingBie.set


    @Slot(bool)
    def on_Text_ShenFenZhengHaoMa_valueChanged(self,count):
        print(1)
        if len(count)>18:
            QMessageBox.about(self, '提示信息', '身份证号码超过18位')
        else:
            year = count[6:10] // 出生年份
            month = count[10:12] // 出生月份
            date = count[12:14] // 出生日
            sex = count[16:17] // 判断性别
            sex = int(sex)
            if sex % 2:
                self.ui.Text_XingBie.setText("男")
            else:
                self.ui.Text_XingBie.setText("女")
            self.ui.Text_ChuSheng_RiQi.setDate(year,month,date)


        #
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxxlr()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication