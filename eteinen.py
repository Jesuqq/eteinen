import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector
RELAY = 16 #pin 16 used for relay
DELAY = 120 #120 seconds without movement will turn relay off
#pin setup
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN) #used to read sension detection
GPIO.setup(RELAY, GPIO.OUT) #controls relay

while (GPIO.status(MOTION) == LOW)
	
