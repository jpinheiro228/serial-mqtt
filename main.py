# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from serial import Serial
import datetime
import paho.mqtt.publish as publish
import json

with open("config.json","r") as f:
    cfg = json.load(f)
CLIENT_ID=cfg["id"]
BROKER = cfg["broker"]
TOPIC = cfg["topics"][0]
CREDS = {"username": cfg["username"], "password": cfg["password"]}

def publishmqtt(m, t):
    publish.single(topic=t, payload=m, hostname=BROKER,
                   client_id=CLIENT_ID, retain=True, auth=CREDS)


def readserial(s):
    try:
        print(datetime.datetime.now(), end="\t")
        return s.readline().decode().splitlines()[0]
    except:
        s.close()


if __name__ == '__main__':
    # s = Serial(port="/dev/ttyUSB0", baudrate=115200)
    # while s.isOpen():
    #     readserial(s)
    publishmqtt("hello!", TOPIC)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
