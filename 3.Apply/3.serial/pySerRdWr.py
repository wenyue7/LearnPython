import os
import time
import threading
import serial
import mpty

def creatSer():
    mSer1 = serial.Serial(mpty.slaveName1, 38400, timeout = 0.5)
    if mSer1.isOpen():
        print("mSer1 open success !")
    else:
        print("mSer1 open failed !")

    mSer2 = serial.Serial(mpty.slaveName2, 38400, timeout = 0.5)
    if mSer2.isOpen():
        print("mSer1 open success !")
    else:
        print("mSer1 open failed !")

    return mSer1, mSer2


def sendData(serial, data):
    if data != "":
        # encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
        ret = serial.write(str(data).encode())

    return ret


def recvData(serial):
    while True:
        # encode() 方法正好相反，decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。
        # data = serial.read_all()
        data = serial.readline().decode()
        if data == '':
            continue
        else:
            break
    return data




def test():
    mpty.createInteractionWithThread()
    ser1,ser2 = creatSer()

    while True:
        sendData(ser1, "hello world")
        data = recvData(ser2)
        print("---- recv data ----", data)


if __name__ == "__main__":
    test()
