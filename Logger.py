# =====================================================================
# ET Nice 01/12/2018
# By Vaughn Sander
# This script Uses a Raspberry Pi ZeroW to long the triggers on Beams.
# =====================================================================
import time
import RPI.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

Start_Time = time.time()

while True
    GPIO.set
    time.sleep(2)

End_Time = time.time()

Delta = End_Time - Start_Time
print(Start_Time)
print(End_Time)
print(Delta)
