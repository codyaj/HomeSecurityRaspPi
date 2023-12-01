from sftpCollector import saveFiles
from disposal import deleteOldVideos
import time

print(deleteOldVideos()) # Only needs to be checked once per boot

while (True):
    output = saveFiles()
    print(output)
    if (output.split()[0] != "No" or output.split()[0] != "Successful"):
        break;
    # Check the response from saveFiles() and if it isnt good sftp a file to central pi to sound a quick alarm (Buzz or something every now and then to alert home owner)
    time.sleep(10800) # Time is in seconds | 10800s = 3h | Therefor Files if present will be saved on pc boot or every 3 hours

input()
