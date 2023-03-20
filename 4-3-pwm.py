import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(22, gpio.OUT)

p = gpio.PWM(22, 100)
p.start(0)
try:
    while True:
        p.start(float(input('duty cycle = ')))

finally:
    gpio.output(22, 0)
    gpio.cleanup(22)