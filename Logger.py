# =====================================================================
# ET Nice 01/12/2018
# By Vaughn Sander
# This script Uses a Raspberry Pi ZeroW to long the triggers on Beams.
# =====================================================================

#!/usr/bin/env python

import time
from datetime import datetime
import csv
import RPi.GPIO as GPIO

Beam1 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Beam1, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, True)
time.sleep(5)
GPIO.output(17, False)

#Start_Time = time.time()
file = open("/home/ET-Logger/Beam_Log.csv", "a")
if os.stat("/home/ET-Logger/Beam_Log.csv").st_size == 0:
        file.write("Time Triggered ,Duration of trigger\n")

GPIO.output(17, True)

time.sleep(1)
GPIO.output(17, False)

while True:

    if GPIO.input(Beam1) == GPIO.HIGH:
        Trigger_Time = datetime.now()
        Start_Time = time.time()

        GPIO.output(17, True)

        while GPIO.input(Beam1) == 1:
           # GPIO.output(17, True)
            pass

        GPIO.output(17, False)

        End_Time = time.time()
        Delta = End_Time - Start_Time

file.write(str(Trigger_Time) + "," + str(Delta) + "\n")

    GPIO.cleanup()

#    GPIO.output(4, True)
#    time.sleep(1)
#    GPIO.output(4,False)
#    time.sleep(1)



#End_Time = time.time()

#Delta = End_Time - Start_Time
#print(Start_Time)
#print(End_Time)
#print(Delta)

