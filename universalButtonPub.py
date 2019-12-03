#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

hasGPIO = False

try:
    import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
    print("Device detected as Raspberry Pi")
    hasGPIO = True
except ImportError as importError:
    print("Device detected as PC")  
    hasGPIO = False

import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def button_callbackR(channel):
    print("R Button was pushed!")
    result = client.publish("ButtonPress/Red", "Pressed")
def button_callbackY(channel):
    print("Y Button was pushed!")
    result = client.publish("ButtonPress/Yellow", "Pressed")
def button_callbackB(channel):
    print("B Button was pushed!")
    result = client.publish("ButtonPress/Blue", "Pressed")


client.on_connect = on_connect
client.connect("192.168.1.230", 1883, 60)


if hasGPIO:
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(8,GPIO.RISING,callback=button_callbackR) # Setup event on pin 10 rising edge
    GPIO.add_event_detect(10,GPIO.RISING,callback=button_callbackY) # Setup event on pin 10 rising edge
    GPIO.add_event_detect(12,GPIO.RISING,callback=button_callbackB) # Setup event on pin 10 rising edge
    client.loop_forever()
    GPIO.cleanup() # Clean up
else:
    response = ""
    while not (("Q" in response) or ("q" in response)):
        response = input("Simulate [R]ed, [[Y]ellow or [B]lue button press, or [Q]uit:")
        if (("R" in response) or ("r" in response)):
            button_callbackR(0)
        if (("B" in response) or ("b" in response)):
            button_callbackB(0)
        if (("Y" in response) or ("y" in response)):
            button_callbackY(0)
#message = input("Press enter to quit\n\n") # Run until someone presses enter


#https://pypi.org/project/paho-mqtt/
#http://www.steves-internet-guide.com/publishing-messages-mqtt-client/




# The callback for when the client receives a CONNACK response from the server.


    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
#def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))


#client.on_message = on_message

#client.connect("mqtt.eclipse.org", 1883, 60)


