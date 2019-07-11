from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
led = 5 

@app.route('/<pinValue>', methods=['POST'])
def set_pin_value(pinValue):
	try:
		conn = sqlite3.connect("data.db")
		c = conn.cursor()
		c.execute("UPDATE PinValue SET [Value]=? WHERE Id=?;", (pinValue, led))
	except Error as e:
		print(e)
	finally:
		conn.close()
	
	return pinValue

app.run(host='0.0.0.0')
