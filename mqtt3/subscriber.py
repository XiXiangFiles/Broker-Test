import time
import paho.mqtt.client as mqtt
import os
import time
import uuid

def on_connect(client, userdata, flags, rc):
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
result = {}
total_times = int(os.environ['TIMES'])

result['flag'] = True
result['pkg_num'] = 0

def on_message(client, userdata, msg):
    result['pkg_num'] += 1
    if result['flag']:
        result['flag'] = False
        result['start'] = time.time()
    else:
        result['end'] = time.time()
        print(result)

client = mqtt.Client(client_id=str(uuid.uuid4()), clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-server", 1883, 60)
client.loop_forever()