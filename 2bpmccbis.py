# - *- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)

BP1 = 25
BP2 = 8
IN1 = 18
IN2 = 23

# configurer (setup) GPIO en sortie et entree
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)
GPIO.setup (BP1, GPIO.IN)
GPIO.setup (BP2, GPIO.IN)

def MCC_un_sens():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def MCC_autre_sens():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def MCC_arret():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

while True:
    etat2 = GPIO.input(BP2)
    if(etat2 == 0):
        etat1 = GPIO.input(BP1)
        if(etat1 == 1):
            print ("bouton 1 appuyé et MCC dans un sens")
            MCC_un_sens()
        else:
            print ("bouton 1 laché et MCC dans autre sens")
            MCC_autre_sens()
    else:
        print ("bouton 2 appuyé et MCC arrêt")
        MCC_arret()

