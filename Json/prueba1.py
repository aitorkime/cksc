import serial
from datetime import datetime
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
        dato = arduino.readline()
        now = datetime.now() # current date and time
	date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
	print ((date_time)+','+(dato))
	#print (out)
