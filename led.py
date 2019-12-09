import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
while True: # Run forever
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.LOW)
	sleep(1)
	GPIO.output(14, GPIO.LOW)
	GPIO.output(15, GPIO.HIGH)
	sleep(1)
