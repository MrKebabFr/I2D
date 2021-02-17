# - *- coding: utf-8 -*-
import RPi. GPIO as GPIO    # importer bibliotheque GPIO
import time                 # importer bibliothèque time
GPIO.setmode(GPIO.BCM)      # definir la numerotation BCM


IN1 = 18
IN2 = 23
BP1 = 25


# configurer (setup) GPIO en sortie et entree
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)
GPIO.setup (BP1, GPIO.IN)


def MCC_un_sens():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def MCC_autre_sens():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)



while True:
    etat1 = GPIO.input(BP1)
    if etat1 == 1:
        print ("bouton 1 appuye et MCC dans un sens")
        MCC_un_sens()
    else:
        print("Bouton 1 relache et MCC dans l'autre sens")
        MCC_autre_sens()


