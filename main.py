import serial
import time

response=''
ser = serial.Serial("COM1",115200,timeout=1)
ser.flushInput()
def senddata(send):
    # ser.write(send.encode('utf-8'))
    ser.write(send.encode())
def receivedata(_bytes):
    receive=ser.read(_bytes)
    receive=str(receive,encoding='utf-8')
    return receive

if __name__ == '__main__':
    # message = "3VA?\r"#测试
    message = "1PA0\r"
    #print(message.encode())
    senddata(message)
    # senddata("3VA?")
    # print(senddata(message))
    data=receivedata(20)
    if data:
        print(data)
    #     pass
    time.sleep(2)

    def video_button(self):
        if (self.flag == 0):
            self.cap_video = cv2.VideoCapture(1)
            self.timer.start(50)
            self.flag += 1
            self.pushButton_Camera.setText("Close")
        else:
            self.timer.stop()
            self.cap_video.release()
            self.Label_Camrea.clear()
            self.pushButton_Camera.setText("Open")
            self.flag = 0

    def show_viedo(self):
        ret, self.img = self.cap_video.read()
        if ret:
            self.show_cv_img(self.img)

    def show_cv_img(self, img):
        shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        QtImg = QtGui.QImage(shrink.data,
                             shrink.shape[1],
                             shrink.shape[0],
                             shrink.shape[1] * 3,
                             QtGui.QImage.Format_RGB888)
        jpg_out = QtGui.QPixmap(QtImg).scaled(
            self.Label_Camrea.width(), self.Label_Camrea.height())

        self.Label_Camrea.setPixmap(jpg_out)

