import grovepi
import time
import os

led = 5 
sensor = 4
default_pinValue = 0

grovepi.pinMode(led,"OUTPUT")

def flash_led(count, duration):
	for x in range(1, count):
		set_led_value(255)
		time.sleep(duration)
		set_led_value(0)
		time.sleep(duration)

def set_led_value(value):
    	grovepi.analogWrite(led, int(value))

def detect_hit():
	while True:
		pinValue = os.getenv('PIN_VALUE', default_pinValue)
		set_led_value(pinValue)
		if pinValue == 255:
			distance = grovepi.ultrasonicRead(sensor)
			if distance < 10:
				set_led_value(0)
				os.environ['PIN_VALUE'] = 0
				report_hit()
				print(distance)

def report_hit():
	print("HIT!!!!")

flash_led(10, .2)
detect_hit()