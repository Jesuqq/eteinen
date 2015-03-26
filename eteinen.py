import RPi.GPIO as GPIO

MOTION = 13
RELAY = 16
#pin setup
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN) #used to read sension detection
GPIO.setup(RELAY, GPIO.OUT) #controls relay

#this is test for git
