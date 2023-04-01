import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
pwmRed = GPIO.PWM(18, 500)
pwmRed.start(100)
pwmGreen = GPIO.PWM(23, 500)
pwmGreen.start(100)
pwmBlue = GPIO.PWM(24, 500)
pwmBlue.start(100)
try:
    while True:
        dutyRed=input("Enter Duty Cycle for Red LED : ")
        pwmRed.ChangeDutyCycle(float(dutyRed))
        dutyGreen=input("Enter Duty Cycle for Green LED : ")
        pwmGreen.ChangeDutyCycle(float(dutyGreen))
        dutyBlue=input("Enter Duty Cycle for Blue LED : ")
        pwmBlue.ChangeDutyCycle(float(dutyBlue))
except KeyboardInterrupt:
    print("Program is Closed by the User")
    GPIO.cleanup()
