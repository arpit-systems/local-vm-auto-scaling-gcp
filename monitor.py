import psutil
import time

THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=2)
    print("CPU Usage:", cpu)

    if cpu > THRESHOLD:
        print("CPU crossed 75 percent")
        import os
        os.system("./trigger.sh")
        break

    time.sleep(5)

