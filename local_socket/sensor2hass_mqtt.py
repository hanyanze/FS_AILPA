# -*- coding:utf-8 -*-
# author:hyz
import sys
import threading
import binascii
import re
import time
from datetime import datetime
import json
from mySerial import myserial
import paho.mqtt.client as mqtt
import config


class mqtt2sensor:
    def __init__(self):
        self.dict_num = config.doInit()
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect('127.0.0.1', 1883, 5)
        self.client.subscribe('control', qos=0)
        self.client.loop_start()
        self.now_time = datetime.now()
        self.pre_status_light = ""
        self.pre_status_relay = ""
        self.pre_status_fan = ""
        self.pre_status_beep = ""

    def on_connect(self, client, userdata, flags, rc):
        pass
        # print("Connected with result code: " + str(rc))

    def on_message(self, client, userdata, msg):
        # print(msg.topic + " " + str(msg.payload.decode('utf-8')))
        data = json.loads(str(msg.payload.decode('utf-8')))
        for i in data.keys():
            for j in range(self.dict_num):
                if i == config.get("/sensor{}/payload_key".format(j)):
                    if data.get(i) == "on":
                        myserial.serial_port0.sendmsg(config.get("/sensor{}/sensor_protocol_on".format(j)))
                    else:
                        myserial.serial_port0.sendmsg(config.get("/sensor{}/sensor_protocol_off".format(j)))
                    break

    def data_up(self, num, data):
        battery = int(data[16:18], 16)
        battery_num = battery if battery < 100 else 100
        # 设备是光强传感器
        if config.get("/sensor{}/payload_key".format(num)) == "lightpower":
            self.client.publish('state/lightpower01', payload='{"lightpower":%d, "lightpower_battery":%d}'
                                                              % (int(data[18:22], 16), battery_num), qos=0)
        # 设备是人体红外
        elif config.get("/sensor{}/payload_key".format(num)) == "infrared":
            if data[18:20] == "31":
                self.client.publish('state/infrared01',
                                    payload='{"infrared":"有人", "infrared_battery":%d}' % (battery_num))
            else:
                self.client.publish('state/infrared01',
                                    payload='{"infrared":"无人", "infrared_battery":%d}' % (battery_num))
        # 设备是温湿度传感器
        elif config.get("/sensor{}/payload_key".format(num)) == "temhum":
            self.client.publish('state/temhum01',
                                payload='{"tem":%d, "hum":%d, "temhum_battery":%d}'
                                        % (int(data[18:20], 16), int(data[20:22], 16), battery_num), qos=0)
        # 设备是火焰传感器
        elif config.get("/sensor{}/payload_key".format(num)) == "flame":
            if int(data[18:22], 16) > 1500:
                self.client.publish('state/flame01',
                                    payload='{"flame":"有火焰", "flame_battery":%d}' % (battery_num), qos=0)
            else:
                self.client.publish('state/flame01',
                                    payload='{"flame":"无火焰", "flame_battery":%d}' % (battery_num), qos=0)
        # 设备是光电开关
        elif config.get("/sensor{}/payload_key".format(num)) == "itr":
            if data[18:20] == "31":
                self.client.publish('state/itr01',
                                    payload='{"itr":"有遮挡", "itr_battery":%d}' % (battery_num))
            else:
                self.client.publish('state/itr01',
                                    payload='{"itr":"无遮挡", "itr_battery":%d}' % (battery_num))
        # 设备是可燃气体
        elif config.get("/sensor{}/payload_key".format(num)) == "gas":
            if int(data[18:22], 16) > 20:
                self.client.publish('state/gas01',
                                    payload='{"gas":"超标", "gas_battery":%d}' % (battery_num), qos=0)
            else:
                self.client.publish('state/gas01',
                                    payload='{"gas":"正常", "gas_battery":%d}' % (battery_num), qos=0)
        # 设备是烟雾
        elif config.get("/sensor{}/payload_key".format(num)) == "fog":
            if int(data[18:22], 16) > 1:
                self.client.publish('state/fog01',
                                    payload='{"fog":"超标", "fog_battery":%d}' % (battery_num), qos=0)
            else:
                self.client.publish('state/fog01',
                                    payload='{"fog":"正常", "fog_battery":%d}' % (battery_num), qos=0)
        # 设备是电位器
        elif config.get("/sensor{}/payload_key".format(num)) == "potentiometer":
            self.client.publish('state/potentiometer01',
                                payload='{"potentiometer":%f, "potentiometer_battery":%d}'
                                        % (round(int(data[18:22], 16) / 1000, 2), battery_num), qos=0)
        # 设备是超声波
        elif config.get("/sensor{}/payload_key".format(num)) == "ultrasonic":
            self.client.publish('state/ultrasonic01',
                                payload='{"ultrasonic":%f, "ultrasonic_battery":%d}'
                                        % (round(int(data[18:22], 16) / 1000, 2), battery_num), qos=0)
        # 设备是灯
        elif config.get("/sensor{}/payload_key".format(num)) == "light":
            self.client.publish('state/light_battery01',
                                payload='{"light_battery":%d}' % (battery_num), qos=0)
            if data[18:24] != self.pre_status_light:
                if data[18:24] == "ffffff":
                    self.client.publish('state/light01', payload='{"light":"on"}', qos=0)
                else:
                    self.client.publish('state/light01', payload='{"light":"off"}', qos=0)
                self.pre_status_light = data[18:24]
        # 设备是风扇
        elif config.get("/sensor{}/payload_key".format(num)) == "fan":
            self.client.publish('state/fan_battery01',
                                payload='{"fan_battery":%d}' % (battery_num), qos=0)
            if data[18:20] != self.pre_status_fan:
                if data[18:20] == "31":
                    self.client.publish('state/fan01', payload='{"fan":"on"}', qos=0)
                else:
                    self.client.publish('state/fan01', payload='{"fan":"off"}', qos=0)
                self.pre_status_fan = data[18:20]
        # 设备是继电器
        elif config.get("/sensor{}/payload_key".format(num)) == "relay":
            self.client.publish('state/relay_battery01',
                                payload='{"relay_battery":%d}' % (battery_num), qos=0)
            if data[18:20] != self.pre_status_relay:
                if data[18:20] == "31":
                    self.client.publish('state/relay01', payload='{"relay":"on"}', qos=0)
                else:
                    self.client.publish('state/relay01', payload='{"relay":"off"}', qos=0)
                self.pre_status_relay = data[18:20]
        # 设备是蜂鸣器
        elif config.get("/sensor{}/payload_key".format(num)) == "beep":
            self.client.publish('state/beep_battery01',
                                payload='{"beep_battery":%d}' % (battery_num), qos=0)
            if data[18:20] != self.pre_status_beep:
                if data[18:20] == "31":
                    self.client.publish('state/beep01', payload='{"beep":"on"}', qos=0)
                else:
                    self.client.publish('state/beep01', payload='{"beep":"off"}', qos=0)
                self.pre_status_beep = data[18:20]

    def send_mqtt(self, data):
        print(data)
        for j in range(self.dict_num):
            if data[14:16] == config.get("/sensor{}/sensor_type".format(j)):
                self.data_up(j, data)
                break


serial = threading.Thread(target=myserial.serial_port0.receivemsg)
serial.start()
ms = mqtt2sensor()
while True:
    if myserial.serial_port0.recvmsg != "":
        ms.send_mqtt(myserial.serial_port0.recvmsg)
        myserial.serial_port0.recvmsg = ""

