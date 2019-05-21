import time
import serial
import json
import csv
import requests
import datetime
from datetime import datetime
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
        dato = arduino.readline()
        now = datetime.now() # current date and time
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
        f = open( './arduino', 'w')
        f.write(dato)
        f = open( './arduino', 'rU')
        reader = csv.DictReader( f, fieldnames = ( "t","ws","wg","wd"))
        salida = json.dumps( [ row for row in reader ] )
        f2 = open( './parsed.json', 'w')
        f2.write(salida)
        #r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add', json={"token": "cdda7ec43ef99fe921981755f5f0d51e144c6fa","ws":[{"dt":(date_time),"t":(data[0,2]),"ws":(data[0,1]),"wg":48,"wd":(data[0,0]),"bp":1024.5}]})
        #r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add', json={"token": "cdda7ec43ef99fe921981755f5f0d51e144fc6fa","ws":[{"dt":(date_time),"t":"8","ws":"9","wg":"10","wd":"100"}]})
	r = requests.post('http://192.168.1.2/uri' ,json={"token": "cdda7ec43ef99fe921981755f5f0d515f0d51e144fc6fa","ws":[{"t":"8","ws":"9","wg":"10","wd":"100"}]})
            #r.status_code
            #200
        #except KeyboardInterrupt:
         #   print("Exiting")
          #  break
