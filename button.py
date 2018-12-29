#!/usr/bin/env python3
import os, random
from time import sleep
from os import listdir
import RPi.GPIO as GPIO
import subprocess, signal
from multiprocessing import Pool 
#from playsound import playsound
import threading, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

status = False
blinking = False

while True:
    if GPIO.input(14) == False:
        status = True
        GPIO.output(16,GPIO.LOW)
        blinking = True
        GPIO.output(21,GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
        print('--- FM - Started ---') 
        os.system('sudo screen -d -m -S fm sh /home/pi/pifmcc.sh')
    if GPIO.input(15) == False:
        status = True
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        blinking = True
        GPIO.output(20,GPIO.HIGH)
        print('--- FM - Started ---') 
        os.system('sudo screen -d -m -S fm sh /home/pi/pifmyt.sh')
    if GPIO.input(18) == False:
        status = True
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        blinking = True
        GPIO.output(20,GPIO.HIGH)
        print('--- FM - Started ---') 
        os.system('sudo screen -d -m -S fm sh /home/pi/pifmph.sh') 
    if GPIO.input(12) == False:
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        #os.system('sudo screen -X -S fm kill')
        os.system('sudo killall screen')
        print('fm killed')
        blinking = False
        

    if status == True:
        print('status on')
        if blinking == True:
            print('blinking on')
            GPIO.output(16,GPIO.LOW)
            sleep(0.5)
            GPIO.output(16,GPIO.HIGH)
            sleep(0.5)
        else:
            print('blinking off')
            sleep(0.5)
    else:
        print('blinking off')
    sleep(0.25)

#StoneSet - 2018

# Test command :
        #subprocess.Popen(['omxplayer','/home/pi/sound.wav'])
        #playsound.playsound('fm.mp3',True)
        #os.system('omxplayer --no-keys -o local /home/pi/fm.mp3 &')
        #randomfile = random.choice(os.listdir("/home/pi/"))
        #file = '/home/pi/music/'+ randomfile
        #os.system('sudo /home/pi/PiFmRds/src/pi_fm_rds -freq 105.10 -audio sound.wav && omxplayer --no-keys -o local /home/pi/fm.mp3 &')