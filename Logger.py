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
Led = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT)   # Set LedPin's mode is output
GPIO.setup(Beam1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Set BtnPin's mode is input, and pull down



GPIO.output(Led, True)
#Start_Time = time.time()

with open('Beam_Log.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Date Triggered', 'Time Triggered', 'Duration'])

time.sleep(1)

GPIO.output(Led, False)


def loop():
    GPIO.add_event_detect(Beam1, GPIO.RISING, callback=Start_Log,
                          bouncetime=200)  # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed

    while True:
        pass



def Start_Log(ev=None):
    Trigger_Date = datetime.date()
    Start_Time = time.time()

    while (GPIO.input(Beam1)):
        GPIO.output(Led, True)

    Delta = time.time() - Start_Time

    with open('Beam_Log.csv', 'a') as csvfile:
        Append_Log = csv.writer(csvfile)
        Append_Log.writerow([Trigger_Date, Start_Time, Delta])
    csvfile.close()

    GPIO.output(Led, False)

try:
    loop()

except KeyboardInterrupt:
    GPIO.output(Led, False)  # led off
    GPIO.cleanup()  # Release resource
