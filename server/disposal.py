import time
import os

def deleteOldVideos():
    filesDeleted = 0
    os.chdir("video")
    for file in os.listdir():
        creationDate = os.path.getmtime(file)
        if ((time.time() - creationDate) >= 604800): # 604800 is a week in seconds
            os.remove(file)
            filesDeleted += 1
    return f"{filesDeleted} files deleted"
