import subprocess
import psutil
import time

p = subprocess.Popen("calc")
r = psutil.pids()
psutil.process_iter()
p = psutil.Process(p.pid)
print(p.name())
print(p.username())
print(p)