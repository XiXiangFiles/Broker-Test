import paho.mqtt.client as mqtt
import uuid
import time
import os
import threading
import logging
import json

logging.basicConfig(filename='publishers_{}.log'.format(os.environ['NUM']), level=logging.INFO)

result = {}
total_times = int(os.environ['TIMES'])
result['success_times'] = 0
result['flag'] = True

def on_connect(client, userdata, flags, rc):
    client.subscribe("trigger")
    
    
def on_message(client, userdata, msg):
    if result['flag']:
        result['start'] = time.time()
        result['flag'] = False
        for i in range(total_times):
            try:
                body = str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())
                client.publish("test", payload=body, qos=2, retain=False)
                result['success_times'] = result['success_times'] + 1
                result['end'] = time.time()
            except Exception as err:
                pass

def job():
    while(True):
        if not result['flag']:
            if time.time() -  result['end'] > 1:
                start = result['start'] * 10000000
                end = result['end'] * 10000000
                sub = int(end- start)
                result['tps'] = (result['success_times']/sub) * 10000000
                json_result = json.dumps(result)
                logging.info(json_result)
                print(json_result)
                break
        time.sleep(1)


    
client = mqtt.Client(client_id=str(uuid.uuid4()), clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message
t = threading.Thread(target = job)
t.start()
client.connect("mqtt-server", 1883, 60)
client.loop_forever()