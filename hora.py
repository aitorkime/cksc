from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
print(date_time)   
