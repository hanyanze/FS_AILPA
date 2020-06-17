import socket
import platform

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip

class GetIP:
    def __init__(self):
        self.module = 'GetIP'

    def Getip(self):
        ip_address = "0.0.0.0"
        sysstr = platform.system()
        if sysstr == "Windows":
            ip_address = socket.gethostbyname(socket.gethostname())
            print ("Windows @ " + ip_address)
        elif sysstr == "Linux":
            ip_address = getip()
            # print ("Linux @ " + ip_address)
        elif sysstr == "Darwin":
            ip_address = socket.gethostbyname(socket.gethostname())
            print ("Mac @ " + ip_address)
        else:
            print ("Other System @ some ip")
        return ip_address

    def ip2hexstr(self, ip): # 分开
        hexstr = ""
        len_str = len(ip)
        for i in range(len_str):
            hex_str = str(hex(ord(ip[i])))[2:]
            hexstr = hexstr + hex_str
        # print("hex ip :", hexstr)
        return hexstr

    def ip2hexstr_(self, ip): # 整体
        hexstr = ""
        len_str = len(ip)
        parting_ip = ip.split(".", -1)
        # print(parting_ip)
        for i in range(4):
            hex_str = str(hex(int(parting_ip[i], 10)))[2:]
            if len(hex_str) < 2:
                hex_str = "0" + hex_str
            hexstr = hexstr + hex_str
        # print("hex ip :", hexstr)
        return hexstr


get = GetIP()
