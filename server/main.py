from sftpCollector import saveFiles
from disposal import deleteOldVideos
import time

print(deleteOldVideos()) # Only needs to be checked once per boot but if on running on a server with alot of uptime it should be moved into the while loop

while (True):
    print(saveFiles())
    # Check the response from saveFiles() and if it isnt good sftp a file to central pi to sound a quick alarm (Buzz or something every now and then to alert home owner)
    time.sleep(10800) # Time is in seconds | 10800s = 3h | Therefor Files if present will be saved on pc boot or every 3 hours
