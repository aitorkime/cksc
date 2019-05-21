import time
import serial
import numpy as np
import json
import requests
import datetime
from datetime import datetime
N = 1
ii = 0
data = np.zeros((N, 4))
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)#, timeout=1.0)
while True: 
        try:
            data = np.zeros((N, 4))
            line = arduino.readline()
            print(line)
            if not line:
                continue
            data[ii] = np.fromstring(line.decode('ascii', errors='replace'),sep=', ')
            now = datetime.now() # current date and time 
            date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
            print(date_time)
            print(data[0,0])#direccion
            print(data[0,1])#viento
            print(data[0,2])#racha
            print(data[0,3])#temperatura
            #r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add', json={"token": "cdda7ec43ef99fe921981755f5f0d51e144c6fa","ws":[{"dt":(date_time),"t":(data[0,2]),"ws":(data[0,1]),"wg":48,"wd":(data[0,0]),"bp":1024.5}]})
            r = requests.post('http://cksc.es/index.php/wp-json/weatherstation/v1/add', json={"token": "cdda7ec43ef99fe921981755f5f0d51e144fc6fa","ws":[{"dt":(date_time),"t":(data[0,3]),"wg":(data[0,2]),"ws":(data[0,1]),"wd":(data[0,0])}]})
            r.status_code
            200
        except KeyboardInterrupt:
            print("Exiting")
            break
