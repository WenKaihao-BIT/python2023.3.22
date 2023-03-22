import serial
response=''
# ser = serial.Serial("COM3",115200,timeout=1)
# ser.flushInput()
# 串口初始化
def serial_init(port,rate):
    ser = serial.Serial(port,rate, timeout=1)
    ser.flushInput()
    return ser

def senddata(send,ser):
    ser.write(send.encode('utf-8'))
def receivedata(ser):
    # receive=ser.read(_bytes)
    receive = ser.readline()
    receive=str(receive,encoding='utf-8')
    return receive

if __name__ == '__main__':
    # test

    print(serial)
    port = "COM1"
    rate = 115200
    data = "3VA?\r"
    ser = serial_init(port,rate)
    senddata(data,ser)
    while(1):
        message = receivedata(ser)
        if message:
            print(message)
