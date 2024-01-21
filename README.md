[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
## About The Project
<!-- Add Image of project -->
The HomeSecurityRaspPi project is a completely automated home security system that has the ability to record video and audio from around the property, detect intruders with motion detectors and door sensors, and sound alarms as well as send alerts if the home is broken into.

### How it works

#### Security Camera

The camera connected to the Raspberry Pi will wait for motion to be detected and when said motion is detected a recording will begin. These recordings when completed will be sent to the CSS *(Central Security Station)* and be deleted from the camera incase the camera is stolen or turned off the video can still be accessed. The files are transferred to the CSS using [Secure File Transfer Protocol (SFTP)](https://www.techtarget.com/searchcontentmanagement/definition/Secure-File-Transfer-Protocol-SSH-File-Transfer-Protocol).

#### Central Security Station

The CSS *(Central Security Station)* is actively connected to every camera and keypad and is responsible for downloading video recordings and communicating motion detection to the keypad. When the home computer is booted all of the video recordings are downloaded using [SFTP](https://www.techtarget.com/searchcontentmanagement/definition/Secure-File-Transfer-Protocol-SSH-File-Transfer-Protocol) and then deleted from the CSS. Another important function of the CSS is to send phone alerts when the alarm length goes over the acceptable time threshold.

#### Keypad

The keypad is setup to sound a small alarm when motion is detected and if a code is not input within an acceptable time a louder alarm will be sounded and the CSS *(Central Security Station)* will send a phone alert. The keypad also grants the ability to enable and disable the alarm.

## Getting Started

This sections outlines how to impliment the project into your own space.

### Prerequisites

#### Software

pysftp will need to be installed on all devices except the keypads.
```sh
pip install pysftp
```

Install SSH for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) or run the below in terminal on debian operating systems.
```sh
sudo apt install openssh-server
```

To install the OS onto the micro SD cards you will need to install the Raspberry Pi Imager [here](https://www.raspberrypi.com/software/).

#### Hardware

* Server
  * Desktop Pc 
* CameraPi
  * [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
  * Infared Camera with infared LED modules
  * Case
  * [Motion Detector](https://www.jaycar.com.au/duinotech-arduino-compatible-pir-motion-detector-module/p/XC4444)
* CentralPi
  * [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
* KeypadPi
  * [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
  * Active Buzzer
  * Keypad
  * LED's

### Installation

#### Raspberry Pi Zero 2 W Setup

When you open the Raspberry Pi Installer you will see this page. Its important to not that your micro SD card should also be plugged into the PC at this point.

![RaspPiInstaller-Home]

Once this page is open select choose devices --> Select the Raspberry Pi device you are using. Then Choose OS --> Raspberry Pi OS (other) --> Raspberry Pi OS (Legacy) Lite. Then Choose Storage --> You storage device --> NEXT.

![RaspPiInstaller-NEXT]

SELECT EDIT SETTINGS

Configure all settings inside the General tab. Once done with the General tab go to the Services tab and click Enable SSH then Use password authentication. Once both of these tabs are completed click Save then **Yes**.

Next ssh into your rasp pi while it is turned on with these commands

```sh
ssh username@hostname
password
```

### Camera Pi

Enable your camera with these steps
1. type "sudo raspi-config"
2. Select Interfacing Options
3. Click on "Enabled" for the camera then hit OK

If you have a no IR cam navigate into your /boot/ folder and edit the config.txt folder adding the line. Otherwise skip this step

```sh
awb_auto_is_greyworld=1
```

At this stage you will want to download the code from the [cameraPi file](https://github.com/codyaj/HomeSecurityRaspPi/tree/main/cameraPi) and transfer it to the raspberry pi via [sftp](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

### Server Pi

You'll want to download the code from the [server file](https://github.com/codyaj/HomeSecurityRaspPi/tree/main/server) and transfer it to the raspberry pi via [sftp](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

### File start at startup

To make the now downloaded file run at startup follow these instructions

```sh
sudo nano /etc/rc.local
```

and below the comment and above the line `exit 0` add changing "NameForYourRaspPi" to the username of your pi

```sh
python3 /home/NameForYourRaspPi/main.py
```

Now to make sure the file rc.local is executable after exiting nano type

```sh
sudo chmod +x /etc/rc.local
```

#### Home-PC/Server Setup

First download all files from the [server folder](https://github.com/codyaj/HomeSecurityRaspPi/tree/main/server). Please note you may have to edit the main.py script if you are running this on a server with high uptime.

Windows:

1. Right click main.py and click "Create Shortcut"
2. Press Windows Key + R
3. Type "shell:startup"
4. Drag said shortcut into the folder that opened

Other operating systems will be added to this list later.

## Roadmap

 - [X] Security Camera
   - [X] Have Raspberry Pi locally capturing and storing video and audio
   - [X] Setup a local server and use SFTP to move data between devices
   - [X] Use motion detection on the Raspberry Pi. Send alerts to the Central Unit and create a log
   - [X] Create enclosure and setup wired camera and audio capture device
 - [ ] Keypad
   - [X] Setup Communication between central pi and self
   - [X] Configure keypad and LEDS to enable/disable alarm
   - [ ] Create enclosure
 - [X] Central Security Station
   - [X] Connect to all rasp pis over Wi-Fi using sftp and sockets
   - [X] Configure alarm to be triggered when motion is detected
   - [X] Grab video feed from the cameras
 - [ ] Home PC
   - [ ] Setup connection to central pi
   - [ ] Take video from the central pi

 
## License

Distributed under the MIT License. See '[LICENSE](https://github.com/codyaj/HomeSecurityRaspPi/blob/main/LICENSE)' for more information.

## Contact

Cody Jackson - cajackson05@icloud.com

Project Link: [https://github.com/codyaj/HomeSecurityRaspPi](https://github.com/codyaj/HomeSecurityRaspPi)


<!-- Images -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/codyaj/HomeSecurityRaspPi/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/codyaj/
[RaspPiInstaller-Home]: https://github.com/codyaj/HomeSecurityRaspPi/assets/57662320/1314faf1-10a1-4ec5-8fe4-72970ec12001
[RaspPiInstaller-NEXT]: https://github.com/codyaj/HomeSecurityRaspPi/assets/57662320/a3233ca6-8bc7-4966-8477-c914ceed9b2f

