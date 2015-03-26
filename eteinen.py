import RPi.GPIO as GPIO

#pin setup
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.IN) #used to read sension detection
GPIO.setup(16, GPIO.OUT) #controls relay

