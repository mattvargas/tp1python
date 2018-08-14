import psutil
import time

for i in range(20):
    time.sleep(0.1)
    print(psutil.cpu_times_percent())