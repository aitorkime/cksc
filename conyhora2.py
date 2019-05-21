import serial
from datetime import datetime
import csv
import json
import requests
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
        temp = arduino.readline().strip('\n\r\\')
	viento = arduino.readline().strip('\n\r\\')
        racha = arduino.readline().strip('\n\r\\')
	dir = arduino.readline().strip('\n\r\\')
	now = datetime.now() # current date and time
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
	#print (dato)
        #out={'token':'cdda7ec43ef99fe921981755f5f0d51e144fc6fa','ws':[{'dt':(date_time),'t':(temp),'ws':(viento),'wg':(racha),'wd':(dir)}]}
        r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add', json={"token": "cdda7ec43ef99fe921981755f5f0d51e144fc6fa","ws":[{"dt":(date_time),"t":(temp),"ws":(viento),"wg":(racha),"wd":(dir)}]})
	#r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add',json=out) 
            #r.status_code 200
        #except KeyboardInterrupt:
        #    print("Exiting")
        #    break

	#f = open( './arduino', 'w')
	#f.write(out)
	#f = open( './arduino', 'rU')
	#reader = csv.DictReader( f, fieldnames = ( "token","dt","t","ws","wg","wd"))
	#salida = json.dumps( [ row for row in reader ] )
	#f2 = open( './parsed.json', 'w')
        #f2.write(salida)
