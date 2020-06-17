#!/usr/bin/python
# coding=UTF-8
import os
import re
import time
import serial
import binascii
import crcmod.predefined

class CRCGenerator(object):
    def __init__(self):
       self.module = 'crc-8'
    
    def crc_8(self, hexData):
       crc8 = crcmod.predefined.Crc(self.module)
       hexData =binascii.unhexlify(hexData)
       crc8.update(hexData)
       result = hex(crc8.crcValue)
       result = re.sub("0x", '', result)
       if len(result) < 2:
            result = "0" + result
       return result

    def crcAdd(self, status):
        sum = 0
        i = 0
        statusLen = len(status)
        while True:
            sum = sum + int(status[i:i+2], 16)
            i+=2
            if i >= statusLen:
                break
        sumStr = hex(sum)[-2:]
        return sumStr


class myserial:
    def __init__(self, port, baudrate, timeout):
        self.port = serial.Serial(port, baudrate)
        if self.port.isOpen():
            print("open :", self.port.portstr)
        else:
            print("打开端口失败")
        self.recvmsg = ""
        # 是否做校验
        self.crc_send = True
        self.crc_recv = True

    def hexshow(self, data):
        hex_data = ''
        hLen = len(data)
        for i in range(hLen):
            hhex = '%02x' % data[i]
            hex_data += hhex
        return hex_data

    def hexsend(self, string_data):
        hex_data = bytes.fromhex(string_data)
        return hex_data

    def receivemsg(self):
        while True:
            size = self.port.in_waiting
            if size:
                self.recdata = self.port.read_all()
                if self.recdata != "":
                    rcvData = self.hexshow(self.recdata)
                    if self.crc_recv:
                        if rcvData[-2:] == crc.crc_8(rcvData[:-2]):
                            self.recvmsg = str(self.hexshow(self.recdata))
                    else:
                        self.recvmsg = str(self.hexshow(self.recdata))
            self.rcvData = ""
                    
    def sendmsg(self, sendData):
        if self.crc_send:
            sendData = sendData + crc.crc_8(sendData)
        senddata = self.hexsend(sendData)
        self.port.write(senddata)


# 实例化
crc = CRCGenerator()
try:
    serial_port0 = myserial('/dev/ttyUSB0', baudrate=115200, timeout=1)
except:
    time.sleep(1)
    serial_port0 = myserial('/dev/ttyUSB0', baudrate=115200, timeout=1)
# serial_port0.sendmsg("30010705010606")


