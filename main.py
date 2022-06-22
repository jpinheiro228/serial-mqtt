from serial import Serial
import datetime
import paho.mqtt.publish as publish
import json
from logger import default_logger

with open("config.json","r") as f:
    cfg = json.load(f)

CLIENT_ID=cfg["id"]
BROKER = cfg["broker"]
TOPIC = cfg["topics"][0]
CREDS = {"username": cfg["username"], "password": cfg["password"]}


def publishmqtt(m, t):
    try:
        publish.single(topic=t, payload=m, hostname=BROKER,
                       client_id=CLIENT_ID, retain=True, auth=CREDS)
    except Exception as e:
        l.exception(e.value)


def readserial(s):
    try:
        return s.readline().decode().splitlines()[0]
    except:
        s.close()


if __name__ == '__main__':
    l = default_logger(logger_name="serial-mqtt", level="INFO", silent=False)
    l.debug("config file: {}".format(cfg))
    s = Serial(port="/dev/ttyUSB0", baudrate=115200)
    while s.isOpen():
        data = readserial(s)
        l.info(data)
        publishmqtt(data, TOPIC)
