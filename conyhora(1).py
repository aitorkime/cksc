import serial
from datetime import datetime
import csv
import json
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
        dato = arduino.readline()
	now = datetime.now() # current date and time
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
        out="cdda7ec43ef99fe921981755f5f0d51e144c6fa,"+(date_time)+","+(dato)
	print (out)
        f = open( './arduino', 'w')
	f.write(out)
	f = open( './arduino', 'rU')
	reader = csv.DictReader( f, fieldnames = ( "token","dt","t","ws","wg","wd"))
	salida = json.dumps( [ row for row in reader ] )
	f2 = open( './parsed.json', 'w')
        f2.write(salida)
