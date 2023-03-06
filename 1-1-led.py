import RPi.GPIO as TT
import time

TT.setmode(TT.BCM)

TT.setup(14, TT.OUT)
for i in range(10):
    if i % 2 == 0:
        TT.output(14, 1)
        time.sleep(1)
    else:
        TT.output(14,0)
        time.sleep(1)