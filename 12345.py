import  numpy as np
import matplotlib.pyplot as plt
import matplotlib
from ClassSer import *
import time
import datetime
matplotlib.use('TkAgg')
def plot_image(title, x, y):
    plt.title(title)
    plt.plot(x, y, 'deepskyblue')
    plt.show()
    pass

def sin_wave(A, f, fs, phi, t, b):
    '''
    :params A:    振幅
    :params f:    信号频率
    :params fs:   采样频率
    :params phi:  相位
    :params t:    时间长度
    :param b: 偏置
    '''
    # 若时间序列长度为 t=1s,
    # 采样频率 fs=1000 Hz, 则采样时间间隔 Ts=1/fs=0.001s
    # 对于时间序列采样点个数为 n=t/Ts=1/0.001=1000, 即有1000个点,每个点间隔为 Ts
    Ts = 1 / fs
    n = t / Ts
    n = np.arange(n)
    pos = A * np.sin(2 * np.pi * f * n * Ts + phi * (np.pi / 180)) + b
    v =2 * np.pi * f  *A*np.cos(2 * np.pi * f * n * Ts + phi * (np.pi / 180))
    return pos,v
dt = 1/50
t = 100
x = np.arange(0, t, dt)
y=np.zeros(len(x))
v=np.zeros(len(x))
# for i in range(10):
#     yi, vi = sin_wave(0.1,0.1*(i+1),1/dt,0,t,0)
#     y = y+yi
#     v = v+vi
# plot_image("sinx", x, y)
# y= sin_wave(1,0.1,1/dt,0,t,0)+sin_wave(1,0.2,1/dt,0,t,0)+sin_wave(1,0.3,1/dt,0,t,0)+sin_wave(1,0.4,1/dt,0,t,0)+sin_wave(1,0.5,1/dt,0,t,0)+sin_wave(1,0.6,1/dt,0,t,0)+sin_wave(1,0.7,1/dt,0,t,0)+sin_wave(1,0.8,1/dt,0,t,0)+sin_wave(1,0.9,1/dt,0,t,0)+sin_wave(1,1,1/dt,0,t,0)
#ycmd = sin(0.01*2*pi*t)+sin(0.02*2*pi*t)+sin(0.03*2*pi*t)+sin(0.04*2*pi*t)+sin(0.05*2*pi*t)+sin(0.06*2*pi*t)+sin(0.07*2*pi*t)+sin(0.08*2*pi*t)+sin(0.09*2*pi*t)+sin(0.10*2*pi*t)+10
# plot_image("sinx",x,y1[0]+y2[0])
y,v=sin_wave(0.3,1,1/dt,0,t,0)
plot_image("sinx",x,v)
# print(y1[0])
plot_image("v",x,v)


# def checksum(s):
#     response_hex_list = []
#     for i in range(len(s)):
#         response_hex_list.append(hex(ord(s[i]))[2:])
#     check_sum_str = hex(sum([int(i, 16) for i in response_hex_list]))[-2:].upper()
#     return check_sum_str
#
# a=checksum("MOVEINC 0.1 0.1 3")
#
#
#
#
f=open("test.txt", "w")
f1=open("test_v.txt",'w')
f2=open("test_d.txt",'w')
for i in range(x.size):
    # print('J ' +'%.3f' %v[i]+' 50')
    if(abs(v[i]-0.0)<0.0001):
        msg="MOVEABS %.3f 0.1 \n" % (y[i+1])
        f1.write(msg.split(' ')[2]+'\n')
        f2.write(msg.split(' ')[1]+'\n')
    #     # print("MOVEABS %.3f 0.10" % (y[i]))
    else:
        msg="MOVEABS %.3f %.3f \n" % (y[i],abs(v[i]))
        f1.write(msg.split(' ')[2]+'\n')
        f2.write(msg.split(' ')[1]+'\n')
        # print("MOVEINC %.3f 0.1 3" % (y[i + 1] - y[i]))
    f.write(msg)

f.close()
f1.close()
f2.close()

# for i in range(x.size-1):
#     # print('J ' +'%.3f' %v[i]+' 50')
#     if(abs(v[i]-0.0)<0.0001):
#         msg="MOVEINC %.3f 0.1 3\n" % (y[i+1]-y[i])
#         f1.write(msg.split(' ')[2]+'\n')
#         f2.write(msg.split(' ')[1]+'\n')
#     #     # print("MOVEABS %.3f 0.10" % (y[i]))
#     else:
#         msg="MOVEINC %.3f %.3f 3\n" % (y[i+1]-y[i],abs(v[i]))
#         f1.write(msg.split(' ')[2]+'\n')
#         f2.write(msg.split(' ')[1]+'\n')
#         # print("MOVEINC %.3f 0.1 3" % (y[i + 1] - y[i]))
#     f.write(msg)
# f.close()
# f1.close()
# f2.close()
# ser = serial_port()
# ser.port='COM12'
# ser.rate='115200'
# ser.enable_port()
# f=open("D:/PY_Project/python_2022_8_3/test.txt", "r")
# a=f.readlines()
# print(a[0].split('\n')[0]+'<')
# print(a)
# commend = f.readline()
# # print(commend)
# dt_ms = datetime.datetime.now().strftime('---%Y-%m-%d %H:%M:%S.%f')
# print(dt_ms)
# while commend:
#     ser.send = commend
#     ser.senddata()
#     # print(commend)
#     commend = f.readline()
#
#     ser.receivedata()
#     if ser.receive:
#         print(ser.receive)
#     time.sleep(0.1)
# dt_ms2 = datetime.datetime.now().strftime('---%Y-%m-%d %H:%M:%S.%f')
# print(dt_ms2)
# for item in a:
#     ser.senddata(item)
#     ser.receivedata()
#     if ser.receive:
#         print(ser.receive)
#     time.sleep(0.50)