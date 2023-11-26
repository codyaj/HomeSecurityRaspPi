import pysftp
import datetime
import json
import os


def saveFile():
    start_time = datetime.datetime.now() 
    jsonFile = open('sshCredentials.json')
    FTPcredentials = json.load(jsonFile)
    jsonFile.close()
    
    try:
        with pysftp.Connection(FTPcredentials['FTPhostName'], username=FTPcredentials['FTPusr'], password=FTPcredentials['FTPpwd']) as sftp:
            sftp.cwd('video')
            fileList = sftp.listdir()
            for file in fileList:
                sftp.get(file)
                os.replace(file, f'video/{file}')
    
    
            # Create local(server) log file
            fileName = f'{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}'
            f = open(f"serverLogs/{fileName}.txt", "a")
            f.write(f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} - {len(fileList)} files saved \n{fileList}\n")
            f.close()
    
            # Save log file to other machine
            sftp.cwd('../serverLogs')
            sftp.put(f"serverLogs/{fileName}.txt")

            end_time = datetime.datetime.now() 
            time_difference = (end_time - start_time).total_seconds()

            return f"Successful {time_difference}s"
    except Exception as e:
        return e
