import pysftp
import datetime
import json
import os

jsonFile = open('sshCredentials.json')
FTPcredentials = json.load(jsonFile)
jsonFile.close()

try:
    with pysftp.Connection(FTPcredentials['FTPhostName'], username=FTPcredentials['FTPusr'], password=FTPcredentials['FTPpwd']) as sftp:
        print("Connection Successful")
        sftp.cwd('video')
        print(sftp.listdir())
        fileList = sftp.listdir()
        sftp.execute('lcd video')
        for file in fileList:
            sftp.get(file)
            os.replace(file, f'video/{file}')
            print(file)


        # Create local(server) log file
        fileName = f'{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}'
        f = open(f"serverLogs/{fileName}.txt", "a")
        f.write(f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} - {len(fileList)} files saved \n{fileList}\n")
        f.close()

        # Save log file to other machine
        sftp.cwd('../serverLogs')
        sftp.put(f"serverLogs/{fileName}.txt")
        print(fileName)
except Exception as e:
    print(e)
