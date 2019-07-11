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
	except Error as e:
		print(e)
	finally:
		conn.close()
	
	return str(value)

app.run(host='0.0.0.0')
