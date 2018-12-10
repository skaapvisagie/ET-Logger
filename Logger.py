# =====================================================================
# ET Nice 01/12/2018
# By Vaughn Sander
# This script Uses a Raspberry Pi ZeroW to long the triggers on Beams.
# =====================================================================

#!/usr/bin/env python

import time
from datetime import datetime
import os
import RPi.GPIO as GPIO
import csv

Beam1 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Beam1, GPIO.IN)
GPIO.setup(17, GPIO.OUT)


GPIO.output(17, True)
#Start_Time = time.time()

with open('Beam_Log.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Trigger Time', 'Duration'])

time.sleep(1)

with open('Beam_Log.csv', 'a') as csvfile:
    Append_Log = csv.writer(csvfile)
    Append_Log.writerow([Beam1, '0'])
csvfile.close()

GPIO.output(17, False)



while True:

    if GPIO.input(Beam1) == 1:
        Trigger_Time = datetime.now()
        Start_Time = time.time()

       # GPIO.output(17, True)

        while GPIO.input(Beam1) == 1:
           # GPIO.output(17, True)
            pass

       # GPIO.output(17, False)

        End_Time = time.time()
        Delta = End_Time - Start_Time

    with open('Beam_Log.csv', 'a') as csvfile:
        Append_Log = csv.writer(csvfile)
        Append_Log.writerow([Trigger_Time, Delta])
    csvfile.close()

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
