import grovepi
import time
import sqlite3
from sqlite3 import Error
import http.client
import socket

led = 5 
sensor = 4
target = socket.gethostname()

def flash_led(count, duration):
	for x in range(1, count):
		set_led_value(0)
		time.sleep(duration)
		set_led_value(255)
		time.sleep(duration)
	set_led_value(0)

def set_led_value(value):
	grovepi.analogWrite(led, int(value))

def set_pin_value(pin, value):
	try:
		conn = sqlite3.connect("/home/pi/repos/digital-target/data.db")
		c = conn.cursor()
		c.execute("UPDATE PinValue SET [Value]=? WHERE Id=?;", (value, pin))
		conn.commit()
	except Error as e:
		print(e)
	finally:
		conn.close()

def get_pin_value(pin):
	try:
		conn = sqlite3.connect("/home/pi/repos/digital-target/data.db")
		c = conn.cursor()
		c.execute("SELECT [Value] FROM PinValue WHERE Id=?;", (pin,))
		result = c.fetchone()
		return result[0]
	except Error as e:
		print(e)
	finally:
		conn.close()

def detect_hit():
	currentPinValue = 0
	while True:
		newPinValue = get_pin_value(led)

		if currentPinValue != newPinValue:
			currentPinValue = newPinValue
			set_led_value(currentPinValue)
			print("LED VALUE CHANGED")

		if currentPinValue == 255:
			distance = grovepi.ultrasonicRead(sensor)
			if distance > 2 and distance < 10:
				report_hit()
				print(distance)

def report_hit():
	set_pin_value(led, 0) 
	set_led_value(0)
	conn = http.client.HTTPConnection("192.168.1.37", 5000)
	conn.set_debuglevel(1)
	conn.request("POST", "/games/" + target[1])
	conn.close()
	print("HIT!!!!")

grovepi.pinMode(led,"OUTPUT")
flash_led(10, .2)
detect_hit()