import datetime
import json
import requests
from datetime import datetime 
now = datetime.now() # current date and time 
date_time = now.strftime("%Y-%m-%dT%H:%M:%S") 
print(date_time)  
r = requests.post('http://192.168.1.102/post', json={"token": "yPIV5","ws":[{"dt":(date_time),"t":"25,6"}]})#,"t":"temperatura","ws":45,"wg":48,"wd":265,"bp":1024,5})
r.status_code
200
r.json()
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
 'Accept-Encoding': 'gzip, deflate',
 'Connection': 'close',
 'Content-Length': '16',
 'Content-Type': 'application/json',
 'Host': 'httpbin.org',
 'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
 'X-Request-Id': 'xx-xx-xx'},
 'json': {'key1': 'value2'},
 'origin': 'x.x.x.x',
 'url': 'http://192.168.1.102/post'}
