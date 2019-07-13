from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/<int:pin>/<int:value>', methods=['PUT'])
def set_pin_value(pin, value):
	try:
		conn = sqlite3.connect("data.db")
		c = conn.cursor()
		c.execute("UPDATE PinValue SET [Value]=? WHERE Id=?;", (value, pin))
		conn.commit()
	except Error as e:
		print(e)
	finally:
		conn.close()
	
	return str(value)

@app.route('/<int:pin>', methods=['GET'])
def get_pin_value(pin):
	try:
		conn = sqlite3.connect("data.db")
		c = conn.cursor()
		c.execute("SELECT [Value] FROM PinValue WHERE Id=?;", (pin,))
		result = c.fetchone()
		return str(result[0])
	except Error as e:
		print(e)
	finally:
		conn.close()

@app.route('/<int:pin>', methods=['POST'])
def record_hit(pin):
	print("HIT!!! - " + str(pin))
	return str(pin)

app.run(host='0.0.0.0')
