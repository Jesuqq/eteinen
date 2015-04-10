import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector
RELAY = 11 #pin 11 used for relay
TOUCH = 15 #pin 15 used for touch sensor 
DELAY = 120 #120 seconds without movement will turn relay off


#pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN) #used to read motion detection
GPIO.setup(RELAY, GPIO.OUT) #controls relay
GPIO.setup(TOUCH, GPIO.IN) #used for touch sensor

while GPIO.input(MOTION)==GPIO.LOW:
	#motion pin is low when no motion detected
	#will wait here for motion
	if GPIO.input(MOTION)==GPIO.HIGH: #motion detected here
		motion_detected()


def motion_detected():
	var = 1
	while var == 1:
		#time when relay was switched on
		start = time.time()
		#turns relay on
		GPIO.output(RELAY, GPIO.HIGH)

		#here we will check if user wants to end automatic lights with touch sensor
		if GPIO.input(TOUCH)==GPIO.HIGH:
			#must be touched for 1 second to work
			time.sleep(1)
				if GPIO.input(TOUCH)==GPIO.HIGH:
					set_off()

		#if movement detector is still seeing movement, start function again
		if GPIO.input(MOTION)==GPIO.HIGH:
			motion_detected()
		if check_time(start)==true:
			#if 120 seconds have passed will switch relay off
			GPIO.output(RELAY, GPIO.LOW)
			return main

def check_time(start):
	global DELAY
	#current time to see if 120sec has passed
	end = time.time()
	if (end-start)<DELAY:
		return false
	else:
		return true


def set_off():
	#program will come here if touch sensor is touched
	#will wait here for a new touch to activate again
	var = 1

	while var = 1:
		if GPIO.input(TOUCH)==GPIO.HIGH:
			#touch is detected
			#must be touched for 1 secod to activate again
			time.sleep(1)
			if GPIO.input(TOUCH)==GPIO.HIGH:
				return main



