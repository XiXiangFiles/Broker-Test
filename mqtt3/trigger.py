import paho.mqtt.client as mqtt
import uuid

def on_connect(client, userdata, flags, rc):
    client.publish("trigger", payload="start", qos=2, retain=False)
    # client.publish("test", payload="start", qos=2, retain=False)

    
client = mqtt.Client(client_id=str(uuid.uuid4()), clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.connect("127.0.0.1", 1883, 60)
client.loop_forever()