import grovepi
import time
import sqlite3
from sqlite3 import Error

led = 5 
sensor = 4

grovepi.pinMode(led,"OUTPUT")
conn = sqlite3.connect("data.db")

def flash_led(count, duration):
	for x in range(1, count):
		set_led_value(255)
		time.sleep(duration)
		set_led_value(0)
		time.sleep(duration)

def set_led_value(value):
    	grovepi.analogWrite(led, int(value))

def get_led_value(currentLedValue):
	try:
		c = conn.cursor()
		c.execute("SELECT [Value] FROM  PinValue WHERE Id=5;")
		result = c.fetchone()
		ledValue = result[0]
		if currentLedValue != ledValue:
			set_led_value(ledValue)
			return ledValue
		else:
			return currentLedValue
	except Error as e:
		print(e)

def detect_hit():
    currentLedValue = 0
	while True:
		currentLedValue = get_led_value(currentLedValue)
		if currentLedValue == 255:
			distance = grovepi.ultrasonicRead(sensor)
			if distance < 10:
				report_hit()
				print(distance)

def report_hit():
	set_led_value(0)   	
	print("HIT!!!!")

flash_led(10, .2)
detect_hit()