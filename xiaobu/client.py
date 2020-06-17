from socket import *
import threading
import binascii
import re
import time


class Client:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 23458
        BUFSIZ = 1024
        ADDRESS = (HOST, PORT)

        self.tcpClientSocket = socket(AF_INET, SOCK_STREAM)
        self.tcpClientSocket.connect(ADDRESS)
        self.recvData = ""

    def hex_send(self, string_data):
        hex_data = bytes.fromhex(string_data)
        return hex_data

    def hex_show(self, data):
        hex_data = ''
        hLen = len(data)
        for i in range(hLen):
            hhex = '%02x' % data[i]
            hex_data += hhex
        return hex_data

    def send2server(self, data):
        data = self.hex_send(data)
        self.tcpClientSocket.send(data)

    def recv_from_server(self):
        while True:
            data, addr = self.tcpClientSocket.recvfrom(2048)
            if data:
                data = self.hex_show(data)
                self.recvData = data
                # print(data)


client = Client()
# client.send2server("303333")
# while True:
#     client.recv_from_server()



