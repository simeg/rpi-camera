import time
from picamera import PiCamera
from time import sleep

try:
    camera = PiCamera()
    
    camera.start_preview()
    sleep(5)
    
    timestamp = int(time.time())
    file_path = '/home/pi/camera/images/{}.png'.format(str(timestamp))
    
    camera.capture(file_path)
    camera.stop_preview()
except Exception:
    print
