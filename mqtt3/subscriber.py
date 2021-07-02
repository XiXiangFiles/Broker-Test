import time
import paho.mqtt.client as mqtt
import os
import time
import uuid
import threading
import logging
import json

logging.basicConfig(filename='subscribers_{}.log'.format(os.environ['NUM']), level=logging.INFO)


# The callback for when a PUBLISH message is received from the server.
result = {}
total_times = int(os.environ['TIMES'])

result['flag'] = True
result['pkg_num'] = 0
result['total_pkg'] = int(os.environ['TIMES'])

def on_connect(client, userdata, flags, rc):
    client.subscribe("test", 2)

def on_message(client, userdata, msg):
    result['pkg_num'] += 1
    if result['flag']:
        result['flag'] = False
        result['start'] = time.time()
    else:
        result['end'] = time.time()

def job():
    while(True):
        if not result['flag']:
            if time.time() -  result['end'] > 1:
                start = result['start'] * 10000000
                end = result['end'] * 10000000
                sub = int(end- start)
                result['tps'] = (result['pkg_num']/sub) * 10000000
                result['qos'] = (result['pkg_num']/result['total_pkg']) * 100
                logging.info(json.dumps(result))
                break
        time.sleep(1)
    

client = mqtt.Client(client_id=str(uuid.uuid4()), clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message
t = threading.Thread(target = job)
t.start()

client.connect("mqtt-server", 1883, 60)

client.loop_forever()