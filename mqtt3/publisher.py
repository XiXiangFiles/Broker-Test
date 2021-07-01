import paho.mqtt.client as mqtt
import uuid
import time
import os

result = {}
total_times = int(os.environ['TIMES'])

def on_connect(client, userdata, flags, rc):
    result['start'] = time.time() * 10000000
    times = 0
    for i in range(total_times):
        try:
            body = str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())+str(uuid.uuid4())
            client.publish("test", payload=body, qos=2, retain=False)
            times = times + 1
        except Exception as err:
            pass
    result['end'] = time.time() * 10000000
    result['success_times'] = times
    sub = int(result['end']- result['start'])
    result['tps'] = (times/sub) * 10000000
    
    
client = mqtt.Client(client_id=str(uuid.uuid4()), clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect

client.connect("mqtt-server", 1883, 60)
client.loop_forever()