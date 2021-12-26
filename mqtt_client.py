import random
import time
import numpy as np
from paho.mqtt import client as mqtt_client


broker = '127.0.0.1'
port = 1883
topic = "v1/devices/me/telemetry"
client_id = f'56c87bc0-65dd-11ec-8b81-fdc73a656785'
username_mqtt =f'Z0YWYFDjKWQdqhnzUbxH'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.username_pw_set(username=username_mqtt, password="")
    client.connect(broker, port)
    return client


def publish(client,msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def load_massage():
    msg_list=[]

    temperature_real=100*np.random.rand()
    msg_1 = f"{{\"temperature_real\":{temperature_real}}}"
    msg_list.append(msg_1)

    temperature_voltage=0.25+0.028*temperature_real
    msg_2 = f"{{\"temperature_voltage\":{temperature_voltage}}}"
    msg_list.append(msg_2)

    return msg_list

def run():
    client = connect_mqtt()
    client.loop_start()
    while True:
        time.sleep(5)
        msg_list=load_massage()
        for msg in msg_list:
            publish(client,msg)


if __name__ == '__main__':
    run()
