import myserial
import threading
import time

t1 = threading.Thread(target = myserial.serial_port0.receivemsg)
t1.start()
while True:
    if myserial.serial_port0.recvmsg != "":
        print(myserial.serial_port0.recvmsg)
        myserial.serial_port0.recvmsg = ""
