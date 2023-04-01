import RPi.GPIO as GPIO
from time import *
buzzer_pin=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
pwm_buzzer=GPIO.PWM(buzzer_pin, 500)
pwm_buzzer.start(10)
while True:
   duty = 0
   for i in range(10):
      duty = duty + 10 
      pwm_buzzer.ChangeDutyCycle(duty)
      sleep(1)
GPIO.cleanup()
