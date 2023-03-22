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
def sin_wave_cmd(file_add,A, f, fs, phi, b,t):
    file=open(file_add,'w')
    y,v=sin_wave(A,f,fs,phi,t,b)
    x = np.arange(0, t, 1/fs)
    wave=[]
    # plot_image(" sinx ", x, y)
    for i in range(x.size):
        if (abs(v[i] - 0.0) < 0.0001):
            msg = "MOVEABS %.3f 0.1 \n" % (y[i + 1])
        else:
            msg = "MOVEABS %.3f %.3f \n" % (y[i], abs(v[i]))
        file.write(msg)
        wave.append(msg)
    file.close()
    return wave
def sin_wave_user_cmd(file_add,t):
    file = open(file_add, 'w')
    dt=1/50
    x = np.arange(0, t, dt)
    y = np.zeros(len(x))
    v = np.zeros(len(x))
    for i in range(10):
        yi, vi = sin_wave(0.1, 0.1 * (i + 1), 1 / dt, 0, t, 0)
        y = y + yi
        v = v + vi
    plot_image('sin',x,y)
    wave = []
    # plot_image(" sinx ", x, y)
    for i in range(x.size):
        if (abs(v[i] - 0.0) < 0.0001):
            msg = "MOVEABS %.3f 0.1 \n" % (y[i + 1])
        else:
            msg = "MOVEABS %.3f %.3f \n" % (y[i], abs(v[i]))
        file.write(msg)
        wave.append(msg)
    file.close()
    return wave
if __name__ == '__main__':
    # file_add="D:\PY_Project\python_2022_8_3\sin_wave_cmd.txt"
    file_add = "D:\PY_Project\python_2022_8_3\sin_wave_user_cmd.txt"
    wave=sin_wave_user_cmd(file_add,10)