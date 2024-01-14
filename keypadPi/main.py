import network
import socket
from machine import Pin
import utime
import _thread

ssid = ''
password = ''
centralIP = ''
matrixKeys = [['1','2','3','A'],
              ['4','5','6','B'],
              ['7','8','9','C'],
              ['*','0','#','D']]
colPins = []
rowPins = []
keypadRows = [17, 18, 19, 20]
keypadColm = [21, 22, 26, 27]
enteredCode = ''
hardsetPassword = '123'
ledDelay = 0.2
passwordSet = False
alarmActive = False
alarmStart = 0
alarmPing = 0
securityType = '0' # 0 = no security | 1 = soft security (doors activate not motion) | 2 = security

# Connecting to internet
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1234))
s.listen(5)

# Pins
gLed = Pin(3, Pin.OUT)
rLed = Pin(1, Pin.OUT)
noise = Pin(16, Pin.OUT)
led0 = Pin(14, Pin.OUT) #g
led1 = Pin(13, Pin.OUT) #b
led2 = Pin(15, Pin.OUT) #r
securityLeds = [led0, led1, led2]
for x in range(0, 4):
    rowPins.append(Pin(keypadRows[x], Pin.OUT))
    rowPins[x].value(1)
    colPins.append(Pin(keypadColm[x], Pin.IN, Pin.PULL_DOWN))
    colPins[x].value(1)

# Scan keys
def scanKeys():
    global enteredCode, alarmActive, passwordSet, securityType, alarmPing, securityLeds
    while True:

        if (alarmActive == True): # Sounding the alarm
            timeNow = utime.time() # So we dont have to call the function multiple times
            if(timeNow - alarmStart > 30): # Loud alarm
                if(timeNow - alarmPing > 5):
                    alarmPing = timeNow
                    noise.on()
                    utime.sleep(4)
                    noise.off()
            else:
                if(timeNow - alarmPing > 5):
                    alarmPing = timeNow
                    noise.on()
                    utime.sleep(0.2)
                    noise.off()



        for row in range(4):
            for col in range(4):
                rowPins[row].high()
                key = None
                
                if (colPins[col].value() == 1):
                    output = matrixKeys[row][col]
                    
                    if (passwordSet == True):
                        if (output == 'A'):
                            securityType = "0"
                            rLed.off()
                            gLed.off()
                            passwordSet = False
                        if (output == 'B'):
                            securityType = "1"
                            rLed.off()
                            gLed.off()
                            utime.sleep(0.1)
                            noise.on()
                            utime.sleep(0.1)
                            noise.off()
                            passwordSet = False
                        elif (output == 'C'):
                            securityType = "2"
                            rLed.off()
                            gLed.off()
                            utime.sleep(0.1)
                            noise.on()
                            utime.sleep(0.1)
                            noise.off()
                            utime.sleep(0.1)
                            noise.on()
                            utime.sleep(0.1)
                            noise.off()
                            passwordSet = False
                            utime.sleep(120)
                    else:
                        if (output == '*'): # Clear enteredCode
                            enteredCode = ''
                            rLed.on()
                            utime.sleep(ledDelay)
                            rLed.off()
                        elif (output == '#'):
                            if (enteredCode == hardsetPassword): # Password Correct
                                if (alarmActive == True):
                                    alarmActive = False
                                    securityType = "0" # turning off security system
                                    gLed.on()
                                    rLed.on()
                                    utime.sleep(ledDelay)
                                    gLed.off()
                                    rLed.off()
                                    utime.sleep(ledDelay)
                                    gLed.on()
                                    rLed.on()
                                    utime.sleep(ledDelay)
                                    gLed.off()
                                    rLed.off()
                                else:
                                    passwordSet = True
                                    gLed.on()
                                    rLed.on()
                            else:
                                enteredCode = ''
                                rLed.on()
                                utime.sleep(ledDelay)
                                rLed.off()
                        elif (output == 'D'):
                            securityLeds[int(securityType)].on()
                            utime.sleep(1)
                            securityLeds[int(securityType)].off()
                        else:
                            enteredCode += str(output)
                            gLed.on()
                            utime.sleep(ledDelay)
                            gLed.off()
                    
            rowPins[row].low()

# listen for connections
def connListener():
    global centralConnection, alarmActive, securityType, alarmStart
    while True:
        conn, address = s.accept()
        print(f"Addy: {address}")
        if (address[0] == centralIP):
            msg = conn.recv(1024)
            msg = msg.decode('utf-8')
            if(msg == 'motion'): # Motion is detected set alarm
                alarmActive = True
                alarmStart = utime.time()
                conn.send(bytes('alarm set', 'utf-8'))
            elif(msg == 'alarm'):
                if(alarmActive): # Alarm was true send alerts
                    conn.send(bytes('true', 'utf-8'))
                else: # Turn off alarm do not send alerts
                    conn.send(bytes('false', 'utf-8'))
            elif(msg == 'security'): # Checking to see security state
                conn.send(bytes(securityType, 'utf-8'))
            else:
                conn.send(bytes(f'unknown: {msg}', 'utf-8'))
        else:
            print("not correct IP")


_thread.start_new_thread(scanKeys, ())
connListener()
