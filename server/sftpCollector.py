import pysftp
import datetime
import json
import os

def saveFiles():
    startTime = datetime.datetime.now()

    try: # disposal.py changes the directory into video this checks it and corrects if it occurs
        jsonFile = open("sshCredentials.json")
    except:
        os.chdir("..") 
        jsonFile = open("sshCredentials.json")
    try: # Checks to see if the .json file holding the ssh credentials are good
        sftpFileContent = json.load(jsonFile)
    except:
        return "!!!!!! Invalid sshCredentials Json File !!!!!!"
    jsonFile.close()

    for sftpDict in sftpFileContent:
        try:
            with pysftp.Connection(sftpDict["FTPhostName"], username=sftpDict["FTPusr"], password=sftpDict["FTPpwd"]) as sftp:
                sftp.cwd("video")
                fileList = sftp.listdir()
                if (len(fileList) == 0):
                    return "No files to be saved"
                for file in fileList:
                    sftp.get(file)
                    sftp.remove(file)
                    os.replace(file, f"video/{file}")
        
                # Create local(server) log file
                fileName = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}"
                f = open(f"serverLogs/{fileName}.txt", "a")
                f.write(f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} - {len(fileList)} files saved \n{fileList}\n")
                f.close()
        
                # Save log file to other machine
                sftp.cwd("../serverLogs")
                sftp.put(f"serverLogs/{fileName}.txt")

                endTime = datetime.datetime.now() 
                timeDifference = (endTime - startTime).total_seconds()

                return f"Successful {timeDifference}s taken for {len(fileList)} files"
        except Exception as e:
            return e
