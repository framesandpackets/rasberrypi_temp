import os
import time

def temperature():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp="," "))
 
while True:
        print("The current tempature of your Raspberry Pi is:", str(temperature()))
        time.sleep(1)