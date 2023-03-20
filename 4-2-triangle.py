import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    print('period = ')
    period = float(input())
    while True:
        for i in range (256):
            gpio.output(dac, dec2bin(i, 8))
            time.sleep(period / 511)
        for i in range (255, 0, -1):
            gpio.output(dac, dec2bin(i, 8))
            time.sleep(period / 511)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
