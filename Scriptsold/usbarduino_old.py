import time
import serial
import numpy as np
N = 2
data = np.zeros((N, 3))
arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0)
with arduino:
    ii = 0
    while ii < N:
        try:
            line = arduino.readline()
            print(line)
            if not line:
                continue
            data[ii] = np.fromstring(line.decode('ascii', errors='replace'),sep=', ')
            ii += 1
        except KeyboardInterrupt:
            print("Exiting")
            break
print(data)
