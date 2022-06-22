from serial import Serial
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import json
from logger import default_logger

with open("config.json","r") as f:
    cfg = json.load(f)

CLIENT_ID = cfg["id"]
BROKER = cfg["broker"]
TOPICS = cfg["topics"]
CREDS = {"username": cfg["username"], "password": cfg["password"]}

def publishmqtt(m, t, c):
    try:
        c.publish(topic=t, payload=m, retain=True)
    except Exception as e:
        l.exception(e.message)


def readserial(s):
    try:
        return s.readline().decode().splitlines()[0]
    except Exception as e:
        l.exception(e.message)
        s.close()


if __name__ == '__main__':
    l = default_logger(logger_name="serial-mqtt", level="INFO", silent=False)
    l.debug("config file: {}".format(cfg))

    mqtt_client = mqtt.Client(client_id=CLIENT_ID,clean_session=False)
    mqtt_client.username_pw_set(username=CREDS["username"], password=CREDS["password"])
    mqtt_client.connect(host=BROKER)
    mqtt_client.loop_start()

    s = Serial(port="/dev/ttyUSB0", baudrate=115200)
    while s.isOpen():
        try:
            data = readserial(s)
            if data:
                l.info(data)
                if "temperature" in data:
                    publishmqtt(data, TOPICS[0], c=mqtt_client)
                elif "person" in data:
                    publishmqtt(data, TOPICS[1], c=mqtt_client)
        except Exception as e:
            l.exception(e.message)
            mqtt_client.disconnect()
            break
