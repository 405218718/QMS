import os
import shutil
import sys
import time

import cv2
from PySide2.QtCore import Slot
from PySide2.QtGui import QRegExpValidator, QImage, QPixmap
from PySide2.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit

from PaiShe import UI_paishe
from ShuJuKuCaoZuo import DuiXiang as DX, DateEdit
from 人员信息录入 import Ui_Dialog

"""
使用此界面需先在ShuJuKuCaoZuo设置公共路径
"""


class UI_ryxxlr(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle('人员信息录入')  # 设置窗体标题
        # self.timer_camera = QTimer()  # 定时器
        # self.cap = cv2.VideoCapture()   # 准备获取图像
        # self.CAM_NUM = 0                # 摄像头序号
        # self.timer_camera.timeout.connect(self.show_camera)     # 定时器不未O时执行

        # os.getcwd()   # 工作的目录路径
        self.MuLu = DX.image + "image_rs"    # 存放路径
        if not os.path.exists(self.MuLu):       # 检查路径是否存在
            os.mkdir(DX.image + "image_rs")  # 创建目录
        self.Text_RuZhi = DateEdit(self.ui.Text_RuZhi_RiQi)
        self.Text_RuZhi.resize(self.ui.Text_RuZhi_RiQi.width(), self.ui.Text_RuZhi_RiQi.height())
        self.Text_HeTong = DateEdit(self.ui.Text_HeTong_RiQi)
        self.Text_HeTong.resize(self.ui.Text_HeTong_RiQi.width(), self.ui.Text_HeTong_RiQi.height())
        self.Text_TiaoXin = DateEdit(self.ui.Text_TiaoXin_RiQi)
        self.Text_TiaoXin.resize(self.ui.Text_TiaoXin_RiQi.width(), self.ui.Text_TiaoXin_RiQi.height())
        self.Text_LiZhi = DateEdit(self.ui.Text_LiZhi_RiQi)
        self.Text_LiZhi.resize(self.ui.Text_LiZhi_RiQi.width(), self.ui.Text_LiZhi_RiQi.height())
        self.ZhuangTai = 0     # 0为新增功能 ， 1为修改功能
        #限制输入
        regx1 = ("[a-zA-Z0-9.-]+$")  #限制输入数值+字母+"."+"-"
        # regx2 = ("[0-9.]+$")  # 限制输入数值+“.”
        regx3 = ("[0-9]+$")  # 限制输入数值
        regx4 = ("[X0-9]+$")  # 限制输入数值+字母"X"
        # self.ui.Text_GongHao.setMaxLength(128)  #限制输入长度, 最大为128
        self.ui.Text_GongHao.setValidator(QRegExpValidator(regx1, self.ui.Text_GongHao))
        self.ui.Text_GongZuoNianFen.setValidator(QRegExpValidator(regx3, self.ui.Text_GongHao))
        self.ui.Text_LianXiDianHua.setValidator(QRegExpValidator(regx3,  self.ui.Text_GongHao))
        self.ui.Text_JinJiLianXiHaoMa.setValidator(QRegExpValidator(regx3,  self.ui.Text_GongHao))
        self.ui.Text_ShenFenZhengHaoMa.setValidator(QRegExpValidator(regx4,  self.ui.Text_GongHao))

    # 隐藏
    def yincang(self):
        self.ui.Text_ShenFenZhengHaoMa.setEchoMode(QLineEdit.NoEcho)    #NoEcho任何输入都看不见,Normal默认，Password密码,
        # PasswordEchoOnEdit编辑时输入字符显示输入内容,否则用小黑点代替,NoEcho任何输入都看不见（只是看不见，不是不能输入）

    # 身份证号码变更触发
    @Slot()
    def on_Text_ShenFenZhengHaoMa_editingFinished(self):
        # if self.ui.Text_ShenFenZhengHaoMa.hasFocus():
        #     return
        # else:
        #     print(2)
            # self.ui.Text_ShenFenZhengHaoMa.setFocus()  # 获取焦点
        count = self.ui.Text_ShenFenZhengHaoMa.text()
        if len(count) < 18:
            QMessageBox.about(self, '提示信息', '身份证号码需要18位！！！')
            self.ui.Text_ShenFenZhengHaoMa.setFocus()   # 获取焦点
        else:
            year = count[6:10]   # 出生年份
            month = count[10:12]     # 出生月份
            date = count[12:14]     # 出生日
            sex = count[16:17]  # 判断性别
            sex = int(sex)
            if sex % 2 == 0:
                self.ui.Text_XingBie.setEditText('女')
            else:
                self.ui.Text_XingBie.setEditText('男')
            self.ui.Text_ChuSheng_RiQi.setText(year+'/'+month+'/'+date)

    # 确认按钮
    @Slot(bool)
    def on_action_queren_clicked(self, checked):
        sql = {}
        """['ID', '部门', '组别', '职位', '工号', '姓名', '性别', '联系电话', '入职日期', '入职工龄', '离职日期', '待遇',
         '出生日期', '身份证号码', '地址', '密码', '紧急联系人', '紧急联系人电话', '调薪日期', '入职照片', '备注']
         """
        sql['姓名'] = self.ui.Text_XingMing.text().strip()
        sql['性别'] = self.ui.Text_XingBie.currentText().strip()
        sql['部门'] = self.ui.Text_BuMen.text().strip()
        sql['工号'] = self.ui.Text_GongHao.text().strip()
        sql['组别'] = self.ui.Text_ZuBie.text().strip()
        sql['职位'] = self.ui.Text_ZhiWei.text().strip()
        sql['联系电话'] = self.ui.Text_LianXiDianHua.text().strip()
        sql['身份证号码'] = self.ui.Text_ShenFenZhengHaoMa.text().strip()
        sql['入职日期'] = self.Text_RuZhi.text().strip()
        sql['入职工龄'] = self.ui.Text_GongZuoNianFen.text().strip()
        DaiYu = self.ui.Text_DaiYu.text().find(' ')
        sql['待遇'] = self.ui.Text_DaiYu.text()[DaiYu + 1:].strip()
        sql['密码'] = self.ui.Text_GongHao.text().strip()
        sql['地址'] = self.ui.Text_DiZhi.text().strip()
        sql['紧急联系人'] = self.ui.Text_JinJiLianXiRen.text().strip()
        sql['紧急联系人电话'] = self.ui.Text_JinJiLianXiHaoMa.text().strip()
        sql['出生日期'] = self.ui.Text_ChuSheng_RiQi.text().strip()
        sql['合同日期'] = self.Text_HeTong.text().strip()

        lujing = self.MuLu + "\\" + time.strftime('%Y')  # 目录路径+文件夹=存放路径
        if not os.path.exists(lujing):  # 检查路径是否存在
            os.mkdir(self.MuLu + "\\" + time.strftime('%Y'))  # 创建目录
        if self.ZhuangTai == 0:
            sql['入职照片'] = lujing+'\\'+self.newName
            # sql['入职照片'] = lujing + '\\QMS_rs_' + str(self.now_time) + '.jpg'
        else:
            sql['入职照片'] = self.ZhuangTai

        for key in list(sql.keys()):
            if not sql.get(key):
                QMessageBox.warning(self, '提示信息', key+'不能为空')
                break
        else:
            sql['调薪日期'] = self.Text_TiaoXin.text().strip()
            sql['离职日期'] = self.Text_LiZhi.text().strip()
            sql['备注'] = self.ui.Text_BeiZhu.text().strip()
            sql_Table = '人员信息' + str(tuple(list(sql.keys()))).replace('\'', '')  # 列表转元组转字符串，再删除引号
            values = tuple(list(sql.values()))   # 列表转元组
            if DX.XinZeng(DX(), sql_Table, values) == 'ok':       #数据添加成功
                # os.remove(sql['入职照片'])    # 删除指定路径文件
                if self.ZhuangTai == 0:
                    shutil.move(self.lujing, lujing+'\\'+self.newName)    # 移动到指定路径
                    # cv2.imwrite(lujing + '\\QMS_rs_' + str(self.now_time) + '.jpg', self.ZhaoPian)  # 保存路径+保存命名+图像
                QMessageBox.information(self, '提示信息', '操作成功!')
                sql.clear()
                self.close()
            else:
                # os.remove(sql['入职照片'])  # 删除指定路径文件
                QMessageBox.information(self, '提示信息', '操作失败!')

    # 重置按钮
    @Slot(bool)
    def on_action_chongzhi_clicked(self, checked ):
        # ret = QMessageBox.warning(self, '提示信息', '确定重置吗？？？!', QStringLiteral("确定"),QStringLiteral("取消"))
        msgbox = QMessageBox(self)  # 指定父窗口控件
        msgbox.setWindowTitle('提示信息')  # 对话框标题
        msgbox.setText("确定重置吗？？？")  # 设置文本
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # 设置对话框有几个按钮
        msgbox.button(QMessageBox.Yes).setText("确定")    # 设置按钮文本
        msgbox.button(QMessageBox.No).setText("取消")     # 设置按钮文本
        # msgbox.button(QMessageBox.Cancel).setText("结束")   #还有abort,retry,ignore按钮
        # msgbox.setGeometry(500,500,0,0)     #消息框位置、大小设置
        msgbox.setIcon(QMessageBox.Question)  # 图标图片：QMessageBox.information信息框，QMessageBox.question问答框，
        # QMessageBox.warning警告框，QMessageBox.ctitical危险框，QMessageBox.about关于框
        result = msgbox.exec() # 执行对话框，并获取返回值

        if result == QMessageBox.Yes:
            self.ui.Text_XingMing.setText('')
            self.ui.Text_XingBie.setCurrentText('')
            self.ui.Text_BuMen.setText('')
            self.ui.Text_GongHao.setText('')
            self.ui.Text_ZuBie.setText('')
            self.ui.Text_ZhiWei.setText('')
            self.ui.Text_LianXiDianHua.setText('')
            self.ui.Text_ShenFenZhengHaoMa.setText('')
            self.ui.Text_GongZuoNianFen.setText('')
            self.ui.Text_ChuSheng_RiQi.setText('')
            self.Text_RuZhi.clear()
            self.ui.Text_DaiYu.clear()
            self.ui.Text_GongHao.setText('')
            self.ui.Text_DiZhi.clear()
            self.ui.Text_JinJiLianXiRen.clear()
            self.ui.Text_JinJiLianXiHaoMa.clear()
            # self.Text_ChuSheng.clear()
            self.Text_HeTong.clear()
            self.Text_TiaoXin.clear()
            self.Text_LiZhi.clear()
            self.ui.Text_BeiZhu.clear()
            self.ui.Text_TuPian.clear()

        else:
            pass

    # 修改功能
    def xiugai(self, sql: dict):
        xiugai_ui = UI_ryxxlr(self)
        xiugai_ui.ui.Text_XingMing.setText(sql['姓名'])
        xiugai_ui.ui.Text_XingBie.setCurrentText(sql['性别'])
        xiugai_ui.ui.Text_BuMen.setText(sql['部门'])
        xiugai_ui.ui.Text_GongHao.setText(sql['工号'])
        xiugai_ui.ui.Text_ZuBie.setText(sql['组别'])
        xiugai_ui.ui.Text_ZhiWei.setText(sql['职位'])
        xiugai_ui.ui.Text_LianXiDianHua.setText(sql['联系电话'])
        xiugai_ui.ui.Text_ShenFenZhengHaoMa.setText(sql['身份证号码'])
        xiugai_ui.ui.Text_GongZuoNianFen.setText(sql['入职工龄'])
        xiugai_ui.Text_RuZhi.date_str(sql['入职日期'])
        xiugai_ui.ui.Text_DaiYu.setSpecialValueText(sql['待遇'])
        xiugai_ui.ui.Text_GongHao.setText(sql['密码'])
        xiugai_ui.ui.Text_DiZhi.setText(sql['地址'])
        xiugai_ui.ui.Text_JinJiLianXiRen.setText(sql['紧急联系人'])
        xiugai_ui.ui.Text_JinJiLianXiHaoMa.setText(sql['紧急联系人电话'])
        xiugai_ui.ui.Text_ChuSheng_RiQi.setText(sql['出生日期'])
        xiugai_ui.Text_HeTong.date_str(sql['合同日期'])
        xiugai_ui.Text_TiaoXin.date_str(sql['调薪日期'])
        xiugai_ui.Text_LiZhi.date_str(sql['离职日期'])
        xiugai_ui.ZhuangTai = sql['入职照片']
        Image = cv2.imread(sql['入职照片'])
        show = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        xiugai_ui.ui.Text_TuPian.setPixmap(QPixmap.fromImage(showImage))
        xiugai_ui.ui.Text_TuPian.setScaledContents(True)    # 入职照片
        xiugai_ui.ui.Text_BeiZhu.setText(sql['备注'])
        xiugai_ui.Text_TiaoXin.setFocus()       # 调薪日期获得焦点
        # xiugai_ui.action_queren.trigger()  # 触发确认按钮
        self.ZhuangTai = 1
        xiugai_ui.exec_()




    # 拍照
    @Slot(bool)
    def on_action_paizhao_clicked(self, checked):
        paishe = UI_paishe(self)
        paishe.exec_()
        filePath = os.path.dirname(paishe.lujing)   # 获取路径
        name = os.path.basename(paishe.lujing)    # 旧文件名
        self.newName = 'QMS_rs_' + name               # 新命名
        os.rename(paishe.lujing, filePath + '\\' + self.newName)     # 修改文件名称
        # lujing = paishe.on_action_QueRne_clicked()
        self.lujing = filePath + '\\' + self.newName  # 获取路径+文件名
        Image = cv2.imread(self.lujing)
        show = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.Text_TuPian.setPixmap(QPixmap.fromImage(showImage))
        self.ui.Text_TuPian.setScaledContents(True)  # 入职照片





if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_ryxxlr()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
