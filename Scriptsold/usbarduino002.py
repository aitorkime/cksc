import time
import serial
import numpy as np
import json
import requests
import datetime
from datetime import datetime
N = 1
ii = 0
#data = np.zeros((N, 3))
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)#, timeout=1.0)
#with arduino:
#    ii = 0
while True: 
        #try:
            data = np.zeros((N, 3))
            line = arduino.readline()
            print(line)
            #if not line:
            #    continue
            data[ii] = np.fromstring(line.decode('ascii', errors='replace'),sep=', ')
            #ii += 1
            now = datetime.now() # current date and time 
            date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
            #print(date_time)
            print(data[0,0])#direccion
            print(data[0,1])#viento
            print(data[0,2])#temperatura
            r = requests.post('http://192.168.1.2/post', json={"token": "6737d1b7fd0ebe6d74a810437464bff3d329822d6737d1b7fd0ebe6d74a810437464bff3d329822d6737d1b7fd0ebe6d74a810437464bff3d329822d","ws":[{"dt":(date_time),"t":(data[0,2]),"ws":(data[0,1]),"wd":(data[0,0])}]})
            #r = requests.post('http://192.168.1.2/post', json={"token": "yPIV5","ws":[{"dt":(date_time),"t":(data[0,2]),"ws":(data[0,1]),"wg":48,"wd":(data[0,0]),"bp":1024.5}]})
            r.status_code
            200
            #r.json()
            #{'args': {},
            #         'data': '{"token": "yPIV5","ws":[{"dt":(date_time),"t":(data[0,2]),"ws":(data[0,1]),"ki":(data[0,0]),"kk":255,"bp":1024}]}',
            #         'files': {},
            #         'form': {},
            #         'headers': {'Accept': '*/*',
            #         'Accept-Encoding': 'gzip, deflate',
            #         'Connection': 'close',
            #         'Content-Length': '16',
            #         'Content-Type': 'application/json',
            #         'Host': 'httpbin.org',
            #         'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
            #         'X-Request-Id': 'xx-xx-xx'},
            #         'json': {'key1': 'value2'},
            #         'origin': 'x.x.x.x',
            #         'url': 'http://192.168.1.2/post'}
        #except KeyboardInterrupt:
            #print("Exiting")
            #break
#print(data[1,1])
#print(data[1,0])
