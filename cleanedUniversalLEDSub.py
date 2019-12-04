#https://pypi.org/project/paho-mqtt/
#http://www.steves-internet-guide.com/publishing-messages-mqtt-client/

import paho.mqtt.client as mqtt


hasGPIO = False

try:
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
    print("Device detected as Raspberry Pi")
    hasGPIO = True
except ImportError as importError:
    print("Device detected as PC")  
    hasGPIO = False





import time

redPin = 21
yellowPin = 20
bluePin = 16

if hasGPIO:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(redPin,GPIO.OUT)
    GPIO.setup(yellowPin,GPIO.OUT)
    GPIO.setup(bluePin,GPIO.OUT)

    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(yellowPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#This snipped from 
# https://www.hivemq.com/blog/mqtt-client-library-paho-python/

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if ("Blue" in msg.topic) :
        print("Blue LED on")
        if hasGPIO:
            GPIO.output(bluePin,GPIO.HIGH)
        time.sleep(1)
        print("Blue LED off")
        if hasGPIO:
            GPIO.output(bluePin,GPIO.LOW)
    if ("Red" in msg.topic) :
        print("Red LED on")
        if hasGPIO:
            GPIO.output(redPin,GPIO.HIGH)
        time.sleep(1)
        print("Red LED off")
        if hasGPIO:
            GPIO.output(redPin,GPIO.LOW)
    if ("Yellow" in msg.topic) :
        print("Yellow LED on")
        if hasGPIO:
            GPIO.output(yellowPin,GPIO.HIGH)
        time.sleep(1)
        print("Yellow LED off")
        if hasGPIO:
            GPIO.output(yellowPin,GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_subscribe = on_subscribe

#client.connect("mqtt.eclipse.org", 1883, 60)
#client.connect("192.168.1.230", 1883, 60)
#client.connect("192.168.43.8", 1883, 60)
client.connect("Meltan", 1883, 60)

client.subscribe("ButtonPress/Blue", 2)
client.subscribe("ButtonPress/Yellow", 2)
client.subscribe("ButtonPress/Red", 2)
#client.connect("192.168.1.230", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
