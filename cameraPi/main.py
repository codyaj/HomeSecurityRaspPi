import picamera
import datetime
from time import sleep
from gpiozero import MotionSensor

pir = MotionSensor(27)

recordingLength = 60*5 # 5 minutes

# init cam
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)

time.sleep(2) # sleep for 2 seconds to init cam

while (True):
    pir.wait_for_motion()

    # Create a file to let the central rasp pi know that motion has been detected
    x = open("alert.secure", "w")
    x.close()
    
    camera.start_recording(f"video/{datetime.datetime.now().day}_{datetime.datetime.now().month}_{datetime.datetime.now().year}__{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.h264")
    camera.wait_recording(recordingLength)
    camera.stop_recording()
