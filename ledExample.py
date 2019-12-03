import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redPin = 21
yellowPin = 20
bluePin = 16
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(yellowPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

GPIO.output(redPin,GPIO.LOW)
GPIO.output(yellowPin,GPIO.LOW)
GPIO.output(bluePin,GPIO.LOW)

while True:
	print("LED on")
	GPIO.output(bluePin,GPIO.HIGH)
	time.sleep(1)
	print("LED off")
	GPIO.output(bluePin,GPIO.LOW)
	time.sleep(1)
