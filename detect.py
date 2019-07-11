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
		grovepi.analogWrite(led, 255)
		time.sleep(duration)
		grovepi.analogWrite(led, 0)
		time.sleep(duration)
	set_led_value(0)

def set_led_value(newValue):
	grovepi.analogWrite(led, int(newValue))
	try:
		c = conn.cursor()
		c.execute("UPDATE PinValue SET [Value]=? WHERE Id=?;", (newValue, led))
	except Error as e:
		print(e)

def get_led_value():
	try:
		c = conn.cursor()
		c.execute("SELECT [Value] FROM PinValue WHERE Id=?;", (led))
		result = c.fetchone()
		return result[0]
	except Error as e:
		print(e)

def detect_hit():
	currentLedValue = 0
	while True:
		newLedValue = get_led_value()
		if currentLedValue != newLedValue:
			currentLedValue = newLedValue

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