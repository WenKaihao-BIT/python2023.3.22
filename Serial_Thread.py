from PyQt5.QtCore import QThread, pyqtSignal
import time
import serial


# 定义一个线程类
class Serial_Thread(QThread):  # 必须继承QTread
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    Signal_Serial = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Serial_Thread, self).__init__(parent)
        self.port = "COM1"
        self.rate = 115200
        self.send = ''
        self.receive = ''


    def enable_port(self):
        self.ser = serial.Serial(self.port, self.rate, timeout=0.02)
        self.ser.flushInput()

    def close_port(self):
        self.ser.close()

    def senddata(self, data):
        self.ser.write(data.encode('utf-8'))

    def receivedata(self):
        # self.receive = self.ser.readline()
        # receive = self.ser.read_all()
        # receive = str(receive, encoding='utf-8')
        # return receive
        self.receive = self.ser.read_all()
        self.receive = str(self.receive, encoding='utf-8')
        return self.receive
    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        while True:
            time.sleep(0.05)
            self.Signal_Serial.emit("Serial Running")
        pass


if __name__ == '__main__':
    Serial_1 = Serial_Thread()
