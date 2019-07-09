import grovepi
import thread
import time
import sys
from flask import Flask

app = Flask(__name__)

led = 5

grovepi.pinMode(led, "OUTPUT")

def flash_led(count, duration):
	for x in range(1, count):
		grovepi.analogWrite(led, 255)
		time.sleep(duration)
		grovepi.analogWrite(led, 0)
		time.sleep(duration)

def set_led_value(value):
	grovepi.analogWrite(led, int(value))
	
@app.route('/<pinValue>', methods=['POST'])
def set_led(pinValue):
	print(type(pinValue))
	set_led_value(pinValue)
	return pinValue

flash_led(10, .2)

app.run(host='0.0.0.0')
