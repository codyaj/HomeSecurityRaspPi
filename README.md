[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
## About The Project
<!-- Add Image of project -->
As you may have guessed this repo is for the home security systems created using the Raspberry Pi Zero 2 W. The final goal for this project is to have a **full** home automated security system designed by myself. The extent I will go to for this home security system will include at the minimum secuity camera(s), indoor motion detectors, magnetic door sensors, and finally to connect everything together, a central station that will be used to disarm the alarm if triggered and call the police in an emergency situation. 

To send sensitive data over my local network ill be using Secure File Transfer Protocol (SFTP). SFTP works great at making sure any listening devices connected to your network cannot see the information being transfered but one limitation that will affect this project is the tranfer speed. According to this [article](https://www.nsoftware.com/kb/articles/legacy/sbb/6-lowtransferspeedsftp) the transfer speed of sftp is 1-1.5 Mb/sec and through the test i've conducted it has taken almost 10 minutes to transfer an hours worth of 720p 30fps video with 128kbps audio attached within a .mp4 file. A simple solution to this problem is to once the .mp4 file has finished recording on the rasp pi, compress the file using zip, then transfer via sftp.

## Getting Started

This sections outlines how to replicate this project onto your own server and Raspberry Pi so you can use this project yourself.

### Prerequisites

#### Server

pysftp
```sh
pip install pysftp
```

opencv
```sh
pip install opencv-python
```

zipfile
```sh
pip install zipfile
```

Install SSH for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) or run the below in terminal on debian operating systems
```sh
sudo apt install openssh-server
```

#### Raspberry Pi Zero 2 W

Install the Raspberry Pi Imager [here](https://www.raspberrypi.com/software/).

opencv
```sh
pip install opencv-python
```


zipfile
```sh
pip install zipfile
```

### Hardware

* [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
* Server (*Does not need to run 24/7*)
  * Home PC or
  * Dedicated server
* Cameras
  * Infared (nightvision) or
  * Regular
* Camera/pi mount
  * Try to have a hidden and high camera that is hard to reach/find 

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

> To be completed

## Usage

<!-- Add Images of project -->
The best use for this project is as a home security system. With the ability to make this project in its entirety open source you can ensure your most private data is not sent anywhere you dont want it to be sent.

## Roadmap

 - [ ] Security Camera
   - [ ] Have Raspberry Pi locally capturing and storing video and audio
   - [X] Setup a local server and use SFTP to move data between devices
   - [ ] Setup a live feed over the local network
   - [ ] Use motion detection on the Raspberry Pi. Send alerts to the live feed and create a log
   - [ ] Create enclosure and setup wired camera and audio capture device
 - [ ] Smart Door Bell
   - [ ] Create enclosure with a camera
   - [ ] Use code from the Security Camera with a new raspberry pi inside the camera
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

