# MQTT_examples

The universalLEDsub.py and universalButtonPub.py both run with python3 on Linux.

'cleaned' versions are simply more readable, but less thoroughly tested.

'noBlueLEDSub.py' is a variant of the LED sub that never subscribes to the blue channel, provided as an example.

The user must make sure that python3 and pip3 are installed, as well as paho-mqtt.

pip3 install paho-mqtt


If run on a Raspberry Pi with external hardware, the Python GPIO library must be installed as well.


Finally, a MQTT broker must be run.  I recommend installing mosquitto.  
Make sure that every client.connect function call is connecting to the hostname of the machine running the broker, with the corresponding port (default used in example code).

Email rjb3vp@umd.edu with any questions.


