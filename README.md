[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
## About The Project
<!-- Add Image of project -->
The HomeSecurityRaspPi project is a completely automated home security system that has the ability to record video and audio from around the property, detect intruders with motion detectors and door sensors, and sound alarms as well as send alerts if the home is broken into.

### How it works

#### Security Camera

The camera on the Raspberry Pi will record video and save the file every hour to the raspberry pi. Whenever your desktop is booted or enough time has passed since the last file transfer the videos will be transfered each Raspberry Pi Camera to the Desktop using [Secure File Transfer Protocol (SFTP)](https://www.techtarget.com/searchcontentmanagement/definition/Secure-File-Transfer-Protocol-SSH-File-Transfer-Protocol).

#### Central Security Station

> To Be Completed

## Getting Started

This sections outlines how to replicate this project onto your own server and Raspberry Pi so you can use this project yourself.

### Prerequisites

#### Server

pysftp
```sh
pip install pysftp
```

Install SSH for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) or run the below in terminal on debian operating systems
```sh
sudo apt install openssh-server
```

#### Raspberry Pi Zero 2 W

Install the Raspberry Pi Imager [here](https://www.raspberrypi.com/software/).

### Hardware

* Server
  * Desktop Pc 
* Camera
  * [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
  * Infared Camera with infared LED modules
  * Case
  * [Motion Detector](https://www.jaycar.com.au/duinotech-arduino-compatible-pir-motion-detector-module/p/XC4444)
  * Active Buzzer
  * Prefered method of powering
  * **(OPTIONAL) Magnetic Door Sensor**
* Central
  * [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
  * [ESP8266](https://www.makerstore.com.au/product/elec-nodemcu-esp8266/)
  * Monitor
  * Active Buzzer

### Tools

* Soldering Iron
* 

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

Enable your camera with these steps
1. type "sudo raspi-config"
2. Select Interfacing Options
3. Click on "Enabled" for the camera then hit OK

If you have a no IR cam navigate into your /boot/ folder and edit the config.txt folder adding the line. Otherwise skip this step

```sh
awb_auto_is_greyworld=1
```

At this stage you will want to download the code from the [cameraPi file](https://github.com/codyaj/HomeSecurityRaspPi/tree/main/cameraPi) and transfer it to the raspberry pi via [sftp](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

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
 - [ ] Smart Door Bell
   - [ ] Setup a live feed over the local network working with video and audio
   - [ ] Send alerts to Central Unit when doorbell is rung
   - [ ] Create enclosure with a camera
 - [ ] Central Security Station
   - [ ] Connect Motion detectors and Magnetic door sensors to one rasp pi
   - [ ] Setup a keypad that will turn off the alarm when triggered
   - [ ] Enable remote enabling of motion detecter online

 
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

