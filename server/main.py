from sftpCollector import saveFiles
from disposal import deleteOldVideos
import time

print(deleteOldVideos()) # Only needs to be checked once per boot | If you're running this on a server with a very high ontime I strongly suggest putting this with the saveFiles function call

while (True):
    print(saveFiles())
    time.sleep(10800) # Time is in seconds | 10800s = 3h | Therefor Files if present will be saved on pc boot or every 3 hours
