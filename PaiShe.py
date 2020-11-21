# 拍照功能
import time

import cv2
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap


class Camera:
    def __init__(self):
        self.timer_camera = QTimer()  # 定时器
        self.cap = cv2.VideoCapture()   # 准备获取图像
        self.CAM_NUM = 0                # 摄像头序号
        self.timer_camera.timeout.connect(self.show_camera)     # 定时器不未O时执行

    # 打开相机
    def button_open_camera_click(self):
        if not self.timer_camera.isActive():
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QMessageBox.warning(
                    self, u"提示信息", u"请检测相机与电脑是否连接正确",
                    buttons=QMessageBox.Ok,
                    defaultButton=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)

    def show_camera(self):
        flag, self.image = self.cap.read()
        self.image = cv2.flip(self.image, 1, dst=None)  # 左右翻转
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.ui.Text_TuPian.setPixmap(QPixmap.fromImage(showImage))
        self.ui.Text_TuPian.setScaledContents(True)

    # 拍照
    def takePhoto(self):
        if self.timer_camera.isActive():
            self.now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            cv2.putText(self.image, str(self.now_time),
                        (int(self.image.shape[1] / 2 - 130), int(self.image.shape[0] - 10)),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1.0, (255, 255, 255), 1)  # 图片对象、文本、像素、字体、字体大小、颜色、字体粗细
            self.timer_camera.stop()  # 暂停定时器
            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.Text_TuPian.setPixmap(QPixmap.fromImage(showImage))
            # self.ui.Text_TuPian.pixmap().toImage()  # 获取QLabel上的图像QImage
            self.ui.Text_TuPian.setScaledContents(True)
            self.ZhaoPian = self.image

            if self.cap.isOpened():
                self.cap.release()  # 释放摄像头
            # if self.timer_camera.isActive():
            #     self.timer_camera.stop()      # 暂停定时器

