import os
import re
import time
import binascii
import threading
from socket import *
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


class Myudp:
    def __init__(self, port):
        self.port = port
        # 是否做校验
        self.crc_send = False
        self.crc_recv = False
        # 建立socket
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        # 绑定端口
        self.server_socket.bind(('', self.port))
        self.recvmsg = ""

    def hexsend(self, string_data):
        hex_data = bytes.fromhex(string_data)
        return hex_data

    def hexshow(self, data):
        hex_data = ''
        hLen = len(data)
        for i in range(hLen):
            hhex = '%02x' % data[i]
            hex_data += hhex
        return hex_data

    # 数据接收
    def receivemsg(self):
        while True:
            # 接收数据
            data, addr = self.server_socket.recvfrom(1024)
            self.recvmsg = str(data, encoding="utf-8")
            # print ('Received from:', addr, str(self.recvmsg, encoding="utf-8"))
         
    # 发送单播，需要参数：发送内容，对方IP地址，端口   
    def sendmsg_unicast(self, data, client_ip, port):
        addr = (client_ip, port)
        self.server_socket.sendto(data.encode("utf-8"), addr)

    # 发送广播，需要参数：发送内容，端口  
    def sendmsg_broadcast(self, data, port):
        addr = ("<broadcast>", port)
        self.server_socket.sendto(data.encode("utf-8"), addr)


crc = CRCGenerator()
my_udp = Myudp(15679)
# my_udp.receivemsg()
# myudp_s.sendmsg_unicast("300123", "192.168.11.84", 23459)
# myudp_s.sendmsg_broadcast("300123", 23459)

