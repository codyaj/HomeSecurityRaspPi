import picamera
import datetime
from time import sleep
import datetime
from gpiozero import MotionSensor

pir = MotionSensor(27)
recording = False
waitingForMotion = False
timeSinceMotion = 0
diffSinceMotion = 0

while (True):
    sleep(0.1) # wait

    if (waitingForMotion):

        if(pir.motion_detected == True): # Reset the counter
            timeSinceMotion = datetime.datetime.now()

        diffSinceMotion = (datetime.datetime.now() - timeSinceMotion).total_seconds()

        if (diffSinceMotion <= 20): # wait 20 seconds on waitingForMotion before stopping the recording
            continue

        else: # Stop the recording and reset variables
            recording = False
            waitingForMotion = False
            timeSinceMotion = 0
            diffSinceMotion = 0
            camera.stop_recording()
            camera.close()
            f = open("video/finshedRecording", "w") # Create file to show recording is finished
            f.close()

    elif (pir.motion_detected == True and recording == False): # Begin Recording
        # Init Cam
        camera = picamera.PiCamera()
        camera.resolution = (1920, 1080)

        timeSinceMotion = datetime.datetime.now()
        waitingForMotion = True

        camera.start_recording(f"video/{datetime.datetime.now().day}_{datetime.datetime.now().month}_{datetime.datetime.now().year}__{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.h264")

        # Create a file to let the central rasp pi know that motion has been detected
        x = open("alert.secure", "w")
        x.close()
