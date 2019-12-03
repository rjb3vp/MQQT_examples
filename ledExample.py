import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redPin = 21
GPIO.setup(redPin,GPIO.OUT)
while True:
	print "LED on"
	GPIO.output(redPin,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(redPin,GPIO.LOW)
	time.sleep(1)
