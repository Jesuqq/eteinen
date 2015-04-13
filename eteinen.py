import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector
RELAY = 11 #pin 11 used for relay
TOUCH = 15 #pin 15 used for touch sensor 
DELAY = 60 #x seconds without movement will turn relay off


#pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN) #used to read motion detection
GPIO.setup(RELAY, GPIO.OUT) #controls relay
GPIO.setup(TOUCH, GPIO.IN) #used for touch sensor

#relay shut down in beginning
GPIO.output(11, False)

print("GPIO setup")

def motion_detected():
	var = 1
	while var == 1:
		#time when relay was switched on
		start = time.time()
		#turns relay on
		GPIO.output(RELAY, True)
		print("Lights turned on!!")

		#here we will check if user wants to end automatic lights with touch sensor
		if GPIO.input(TOUCH)==GPIO.HIGH:
			#must be touched for 1 second to work
			time.sleep(1)
			
			if GPIO.input(TOUCH)==GPIO.HIGH:
					set_off()

		print("will now sleep for "+str(DELAY)+" seconds")
		time.sleep(DELAY-5)
		start = time.time()
		stop = time.time()

		print("will now check for new motion")
		while (stop-start) <= 5 > 0:
			#5 seconds before delay is up will check for new motion
			#if new motion is detected will continue without shutting relay down
			if checkForMovement()==True:			
				waitForMovement(True)
			stop = time.time()

		print("no new motion")
		#if no new motion is detected for 5 
		waitForMovement(False)

#this propably wont be used
def check_time(start):
	global DELAY
	#current time to see if 120sec has passed
	end = time.time()
	if (end-start)<DELAY:
		return False
	else:
		return True


def set_off():
	#program will come here if touch sensor is touched
	#will wait here for a new touch to activate again
	var = 1
	while var == 1:
		if GPIO.input(TOUCH)==GPIO.HIGH:
			#touch is detected
			#must be touched for 1 secod to activate again
			time.sleep(1)
		
			if GPIO.input(TOUCH)==GPIO.HIGH:
				return waitForMovement()

def waitForMovement(again):

	if again == True:
		print("New motion, will start again")
		motion_detected()

	else:
		print("Waiting for motion")
		GPIO.output(RELAY, False)
		var = 1
		while var == 1:
        		#motion pin is low when no motion detected
        		#will wait here for motion
			if checkForMovement()==True: #motion detected here
				print("Motion detected!")
				motion_detected()

		time.sleep(0.1)

def checkForMovement():

	if GPIO.input(MOTION)==GPIO.HIGH:
		return True

	else:
		return False

#value false starts motion detection with relay off
again = False
waitForMovement(again)
