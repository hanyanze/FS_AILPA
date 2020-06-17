import os
import json
from getIP.getip import *

# Return CPU temperature as a float
def getCPUtemperature():
    f = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
    temp = int(f.readline().strip())/1000
    return round(temp, 1)

# Return RAM information (unit=MB) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    f = os.popen("free | awk '/Mem/ {print $2,$3,$4}'")
    info = f.readline().split()
    # info = [round(int(i)/1024, 1) for i in info]
    return str(int(info[1]) * 100 // int(info[0])) + "%" 


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def getDiskinfo():
    f = os.popen("df -h /")
    info = f.readlines()[1].split()[1:5]
    return info[3]

def getIP():
    return get.Getip()

if __name__ == '__main__':
    RaspiInfo = {}
    RaspiInfo['CPUtemp'] = getCPUtemperature()
    RaspiInfo['RAMinfo'] = getRAMinfo()
    RaspiInfo['DISKinfo'] = getDiskinfo()
    RaspiInfo['IPinfo'] = getIP()
    #RaspiInfo['CPUuse'] = getCPUinfo()
    # 必须转化为标准 JSON 格式备用，下文有解释
    print(json.dumps(RaspiInfo))
