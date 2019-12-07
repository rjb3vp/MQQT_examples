#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.




#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#https://pypi.org/project/paho-mqtt/
#http://www.steves-internet-guide.com/publishing-messages-mqtt-client/

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
    #result = client.publish("ButtonPress/Red", "Pressed", 2)
def button_callbackY(channel):
    print("Y Button was pushed!")
    result = client.publish("ButtonPress/Yellow", "Pressed")
    #result = client.publish("ButtonPress/Yellow", "Pressed", 2)
def button_callbackB(channel):
    print("B Button was pushed!")
    result = client.publish("ButtonPress/Blue", "Pressed")
    #result = client.publish("ButtonPress/Blue", "Pressed", 2)

client.on_connect = on_connect
#client.connect("192.168.43.8", 1883, 60)
#client.connect("192.168.1.230", 1883, 60)
client.connect("Meltan", 1883, 60)

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
    client.disconnect()





