import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ledstate = False
def my_callback(channel):
    global ledstate
    ledstate = not ledstate
    print("You pressed the button")
    GPIO.output(23, ledstate)
    time.sleep(1)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)

GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback)

    
i=0

try:
    
    while True:
        
        i=i+1
        
        print(i)
        
        time.sleep(1)

except KeyboardInterrupt:
    
    GPIO.cleanup()
