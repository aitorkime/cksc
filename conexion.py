import serial
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
	dato = arduino.readline()
	print (dato)

