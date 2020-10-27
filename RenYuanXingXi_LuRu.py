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
        self.Text_RuZhi.resize(self.ui.Text_RuZhi_RiQi.width(), self.ui.Text_RuZhi_RiQi.height())
        self.Text_HeTong = DateEdit(self.ui.Text_HeTong_RiQi)
        self.Text_HeTong.resize(self.ui.Text_HeTong_RiQi.width(), self.ui.Text_HeTong_RiQi.height())
        self.Text_TiaoXin = DateEdit(self.ui.Text_TiaoXin_RiQi)
        self.Text_TiaoXin.resize(self.ui.Text_TiaoXin_RiQi.width(), self.ui.Text_TiaoXin_RiQi.height())
        self.Text_LiZhi = DateEdit(self.ui.Text_LiZhi_RiQi)
        self.Text_LiZhi.resize(self.ui.Text_LiZhi_RiQi.width(), self.ui.Text_LiZhi_RiQi.height())

    # @Slot(bool)
    # def on_Text_ShenFenZhengHaoMa_valueChanged(self,count):
    #     print(1)
    #     if len(count)<18:
    #         QMessageBox.about(self, '提示信息', '身份证号码超过18位')
    #     else:
    #         year = count[6:10] // 出生年份
    #         month = count[10:12] // 出生月份
    #         date = count[12:14] // 出生日
    #         sex = count[16:17] // 判断性别
    #         sex = int(sex)
    #         if sex % 2:
    #             self.ui.Text_XingBie.setText("男")
    #         else:
    #             self.ui.Text_XingBie.setText("女")
    #         self.ui.Text_ChuSheng_RiQi.setDate(year,month,date)


    #确认按钮
    @Slot(bool)
    def on_action_queren_clicked(self,checked):
        sql = {}
        """["部门", "组别", "职位", "工号", "姓名", "性别", "联系电话", "入职日期", "出生日期",
         "身份证号码", "地址", "待遇", "调薪日期", "离职日期", "备注"]
         """
        sql['姓名'] = self.ui.Text_XingMing.text()
        sql['性别'] = self.ui.Text_XingBie.currentText()
        sql['部门'] = self.ui.Text_BuMen.text()
        sql['工号'] = self.ui.Text_GongHao.text()
        sql['组别'] = self.ui.Text_ZuBie.text()
        sql['职位'] = self.ui.Text_ZhiWei.text()
        sql['联系电话'] = self.ui.Text_LianXiDianHua.text()
        sql['身份证号码'] = self.ui.Text_ShenFenZhengHaoMa.text()
        sql['入职日期'] = self.Text_RuZhi.text()
        sql['待遇'] = self.ui.Text_DaiYu.text()
        sql['出生日期'] = self.ui.Text_ChuSheng_RiQi.text()
        sql['合同日期'] = self.Text_HeTong.text()
        sql['调薪日期'] = self.Text_TiaoXin.text()
        sql['离职日期'] = self.Text_LiZhi.text()
        sql['备注'] = self.ui.Text_BeiZhu.text()


        sql_Table = '人员信息' + str(tuple(list(sql.keys())))  # 列表转元组转字符串
        values = tuple(list(sql.values()))  # 列表转元组
        print(sql_Table)
        print(values)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxxlr()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
