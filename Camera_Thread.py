import time
from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import time
# 定义一个线程类
class Camera_Thread(QThread):# 必须继承QTread
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    Signal_Camera = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Camera_Thread, self).__init__(parent)

        self.Camera_ID = '0'
        self.enable = False
        # 中心点 (cx,cy)
        self.cx = 0
        self.cy = 0
        # self.cap_video = cv2.VideoCapture(int(self.Camera_ID), cv2.CAP_DSHOW)
    def Open_Camera(self):
        self.cap_video = cv2.VideoCapture(int(self.Camera_ID), cv2.CAP_DSHOW)
        self.enable = True
    def Close_Camera(self):
        self.enable =False
        self.cap_video.release()
    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        while True:
            if not self.enable:
                break
            time.sleep(0.05)
            self.Signal_Camera.emit("Camera Running")
        pass


if __name__ == '__main__':
    Camera = Camera_Thread(Camera_ID=0)
    print(Camera.Camera_ID)