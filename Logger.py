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

with open('Beam_Log.csv', 'a') as BeamLog:
    BeamLogFile = csv.writer(BeamLog, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

GPIO.output(17, True)
BeamLogFile.writerow(['Time activated', 'Duration active'])
time.sleep(1)
GPIO.output(17, False)

while True:

    if GPIO.input(Beam1) == GPIO.HIGH:
        Trigger_Time = str(datetime.now())
        Start_Time = time.time()

        GPIO.output(17, True)

        while GPIO.input(Beam1) == 1:
           # GPIO.output(17, True)
            pass

        GPIO.output(17, False)

        End_Time = time.time()
        Delta = str(End_Time - Start_Time)
        row = [Trigger_Time, Delta]

    BeamLogFile.writerow(row)

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

