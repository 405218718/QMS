# 拍照功能
import os
import sys
import time

import cv2
from PySide2.QtCore import QTimer, Slot
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QDialog, QMessageBox

from 拍照 import Ui_zhaopian


"""
备注：软件安装路径不能有中文
"""

class UI_paishe(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_zhaopian()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle('拍摄')  # 设置窗体标题
        self.timer_camera = QTimer()  # 定时器
        self.cap = cv2.VideoCapture()   # 准备获取图像
        self.CAM_NUM = 0                # 摄像头序号
        self.timer_camera.timeout.connect(self.show_camera)     # 定时器不未O时执行
        self.button_open_camera_click()
        self.resize(640, 512)


    # 打开相机
    def button_open_camera_click(self):
        if not self.timer_camera.isActive():
            flag = self.cap.open(self.CAM_NUM)
            if not flag:
                msg = QMessageBox.warning(
                    self, u"提示信息", u"请检测相机与电脑是否连接正确",
                    buttons=QMessageBox.Ok,
                    defaultButton=QMessageBox.Ok)
                # self.close()
            else:
                self.timer_camera.start(30)

    def show_camera(self):
        flag, self.image = self.cap.read()
        self.image = cv2.flip(self.image, 1, dst=None)  # 左右翻转
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.XianShi.setPixmap(QPixmap.fromImage(showImage))
        self.ui.XianShi.setScaledContents(True)

    # 确认
    @Slot(bool)
    def on_action_QueRne_clicked(self, checked):
        if self.timer_camera.isActive():
            self.now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            cv2.putText(self.image, str(self.now_time),
                        (int(self.image.shape[1] / 2 - 130), int(self.image.shape[0] - 10)),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1.0, (255, 255, 255), 1)  # 图片对象、文本、像素、字体、字体大小、颜色、字体粗细
            self.timer_camera.stop()  # 暂停定时器
            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.XianShi.setPixmap(QPixmap.fromImage(showImage))
            # self.ui.Text_TuPian.pixmap().toImage()  # 获取QLabel上的图像QImage
            self.ui.XianShi.setScaledContents(True)
            # os.getcwd()   # 工作的目录路径
            self.lujing = os.getcwd() + '\\' + str(self.now_time) + '.jpg'  # 保存路径+保存命名+图像
            cv2.imwrite(self.lujing, self.image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])  # 保存路径+图像+第三个参数针对特定的格式：
            # 对于JPEG，其表示的是图像的质量，用0-100的整数表示；从0到9,压缩级别越高，图像尺寸越小。默认级别为3
            if self.cap.isOpened():
                self.cap.release()  # 释放摄像头
        if not os.path.exists(self.lujing):
            QMessageBox.information(self, '提示信息', '拍摄失败!\n'
                                                  '备注：软件安装路径不能有中文')
            # if self.timer_camera.isActive():
            #     self.timer_camera.stop()      # 暂停定时器
        else:
            self.close()    # 关闭窗口
            return self.lujing


    # 相机选择
    @Slot(str)
    def on_action_JingTou_currentIndexChanged(self, curText):
        self.CAM_NUM = int(self.ui.action_JingTou.currentText())
        self.button_open_camera_click()

    # 尺寸
    @Slot(str)
    def on_action_LeiXing_currentIndexChanged(self, curText):
        chicun = self.ui.action_LeiXing.currentText()
        if chicun == 'default':
            self.resize(640, 512)  # 设置窗口大小
        elif chicun == 'Photo（26×32）':
            self.resize(26*20, 32*20+32)  # 设置窗口大小
        elif chicun == 'A4（297×210）':
            self.resize(297*2, 210*2+32)  # 设置窗口大小
        elif chicun == 'A4（210×297）':
            self.resize(210*2, 297*2+32)  # 设置窗口大小
        elif chicun == 'A3（420×297）':
            self.resize(420*2, 297*2+32)  # 设置窗口大小
        elif chicun == 'A3（297×420）':
            self.resize(297*2, 420*2+32)  # 设置窗口大小

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    form = UI_paishe()  # ui是Ui_MainWindow()类的实例化对象
    form.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication