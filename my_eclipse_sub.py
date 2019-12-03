#https://pypi.org/project/paho-mqtt/
#http://www.steves-internet-guide.com/publishing-messages-mqtt-client/

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

#This snipped from 
# https://www.hivemq.com/blog/mqtt-client-library-paho-python/
#def on_subscribe(client, userdata, mid, granted_qos):
#    print("Subscribed: "+str(mid)+" "+str(granted_qos))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_subscribe = on_subscribe

#client.connect("mqtt.eclipse.org", 1883, 60)
client.connect("192.168.1.230", 1883, 60)


client.subscribe("ButtonPress/Blue")
client.subscribe("ButtonPress/Yellow")
client.subscribe("ButtonPress/Red")
#client.connect("192.168.1.230", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
