# =====================================================================
# ET Nice 01/12/2018
# By Vaughn Sander
# This script Uses a Raspberry Pi ZeroW to long the triggers on Beams.
# =====================================================================

#!/usr/bin/env python

import time
import datetime
import csv
import RPi.GPIO as GPIO

Beam1 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Beam1, GPIO.OUT)

Start_Time = time.time()

with open('Beam_Log.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Time activated', 'Duration active'])


while True:

    if Beam1:
        Trigger_Time = str(datetime.now())
        Start_Time = time.time()
        while Beam1:
            pass

        End_Time = time.time()
        Delta = str(End_Time - Start_Time)

    filewriter.writerow([Trigger_Time, Delta])


#    GPIO.output(4, True)
#    time.sleep(1)
#    GPIO.output(4,False)
#    time.sleep(1)



#End_Time = time.time()

#Delta = End_Time - Start_Time
#print(Start_Time)
#print(End_Time)
#print(Delta)

