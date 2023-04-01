import RPi.GPIO as GPIO  
import time            
GPIO.setwarnings(False)  

######
#  For Hardware, apply the following col and row
#col=[12,22,27,25,17,24,23,18]
#row=[21,20,26,16,19,13,6,5]

######
# For Proteus apply the following list of col and row
col=[18,23,20,12,16,24,25,21]
row=[19,6,22,27,5,17,13,26]

GPIO.setmode(GPIO.BCM)
for i in range(len(row)):
    GPIO.setup(row[i],GPIO.OUT)
for i in range(len(col)):
    GPIO.setup(col[i],GPIO.OUT)

colValue=[[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],
   [0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]]
   
rowValue=[[0,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1],[1,1,0,1,1,1,1,1],[1,1,1,0,1,1,1,1],
   [1,1,1,1,0,1,1,1],[1,1,1,1,1,0,1,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,0]]

try: 
   while 1:
      for x in range(8):
         for j in range(8):
            GPIO.output(col[j], colValue[x][j])   
            GPIO.output(row[j], rowValue[x][j])  
         time.sleep(0.0002)
except KeyboardInterrupt:
   GPIO.cleanup()