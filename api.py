from flask import Flask
import os

app = Flask(__name__)

print(os.environ['HOME'])

@app.route('/<pinValue>', methods=['POST'])
def set_pin_value(pinValue):
	print(type(pinValue))
	os.environ['PIN_VALUE'] = pinValue
	print(os.getenv('PIN_VALUE', 123))
	return pinValue

app.run(host='0.0.0.0')
