from flask import Flask
import os

app = Flask(__name__)
	
@app.route('/<pinValue>', methods=['POST'])
def set_pin_value(pinValue):
	print(type(pinValue))
	os.environ['PIN_VALUE'] = pinValue
	return pinValue

app.run(host='0.0.0.0')
