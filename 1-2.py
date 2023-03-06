import RPi.GPIO as TT

TT.setmode(TT.BCM)

TT.setup(14, TT.OUT)
TT.setup(18, TT.IN)

while True:
    TT.output(14, TT.input(18))