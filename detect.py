import grovepi

led = 5 
sensor = 4

grovepi.pinMode(led,"OUTPUT")
grovepi.analogWrite(led,255)

while True:
	distance = grovepi.ultrasonicRead(sensor)
	if distance < 10:
		grovepi.analogWrite(led,0)
		print(distance)
