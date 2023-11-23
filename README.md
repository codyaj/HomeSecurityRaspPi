[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
## About The Project
<!-- Add Image of project -->
As you may have guessed this repo is for the home security systems created using the Raspberry Pi Zero 2 W. The final goal for this project is to have a **full** home automated security system designed by myself. The extent I will go to for this home security system will include at the minimum secuity camera(s), indoor motion detectors, magnetic door sensors, and finally to connect everything together, a central station that will be used to disarm the alarm if triggered and call the police in an emergency situation. 

As you may have suspected this is a big project for a full time student and part-time employee and you would be correct. With the constraints of time and budget I expect to have this project completed mid 2024.

## Getting Started

I'll outline some basic steps to help you replicate this project yourself.

### Hardware

* [Raspberry Pi Zero 2 W](https://core-electronics.com.au/raspberry-pi-zero-2-w-wireless.html)
* Internal laptop webcam

### Tools

* Soldering Iron
* 

### Installation

> To be completed

## Usage

<!-- Add Images of project -->
This project is best used as a personal home security system. With the ability to custom make the project you have the freedom to naturally blend in the camera and other peices of hardware into the environment in order to keep the data being recorded incase of actual emergency. I personally would suggest only transferring the files locally within your network and not to any clouds but of course if you make this yourself you can do as you please.

If you wanted to add facial recognition I would suggest [OpenCV](https://opencv.org/). I opted to not use this to make this project as light weight as possible and not hinder any performance but I do see application in it being used instead of motion detection.

## Roadmap

 - [ ] Security Camera
   - [ ] Have Raspberry Pi locally capturing and storing video and audio
   - [ ] Setup a local server and use SFTP to move data between devices
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
