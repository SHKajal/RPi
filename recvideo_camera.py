from picamera import PiCamera
from time import sleep 

camera=PiCamera()
camera.rotation=180

#camera.start_preview()
sleep(2)
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(30)
camera.stop_recording()
#camera.stop_preview()
