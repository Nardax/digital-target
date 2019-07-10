import grovepi
import thread
import time
import sys
from flask import Flask

app = Flask(__name__)

led = 5
sensor = 4

grovepi.pinMode(led, "OUTPUT")

def flash_led(count, duration):
    for x in range(1, count):
        grovepi.analogWrite(led, 255)
        time.sleep(duration)
        grovepi.analogWrite(led, 0)
        time.sleep(duration)

def set_led_value(value):
    grovepi.analogWrite(led, int(value))
    
def detect_hit():
    try:
        lastDistance = grovepi.ultrasonicRead(sensor)
        while True:
            distance = grovepi.ultrasonicRead(sensor)
            change = abs(distance - lastDistance)
            if change > 2:
        #       grovepi.analogWrite(led,0)
                lastDistance = distance
                print(change)
    except:
        e = sys.exc_info()[0]
        print(e)

@app.route('/<pinValue>', methods=['POST'])
def set_led(pinValue):
    print(type(pinValue))
    set_led_value(pinValue)
    return pinValue

flash_led(10, .2)

thread.start_new_thread(detect_hit, ())

app.run(host='0.0.0.0')

