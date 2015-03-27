import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector
RELAY = 16 #pin 16 used for relay
DELAY = 120 #120 seconds without movement will turn relay off


#pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN) #used to read sension detection
GPIO.setup(RELAY, GPIO.OUT) #controls relay

while GPIO.input(MOTION)==GPIO.LOW:
	if GPIO.input(MOTION)==GPIO.HIGH: #motion detected here
		motion_detected()


def motion_detected():
	var = 1
	while var == 1:
		#time when relay was switched on
		start = time.time()
		#turns relay on
		GPIO.output(RELAY, GPIO.HIGH)

		#if movement detector is still seeing movement, start function again
		if GPIO.input(MOTION)==GPIO.HIGH:
			motion_detected()
		if check_time(start)==true:
		

			return main

def check_time(start):
	global DELAY
	#current time to see if 120sec has passed
	end = time.time()
	if (end-start)<DELAY:
		return false
	else:
		return true
