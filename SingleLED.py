import RPi.GPIO as GPIO
from time import * 

GPIO.setmode(GPIO.BCM)

pin=18

GPIO.setup(pin,GPIO.OUT)
          
try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin, GPIO.LOW)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
 