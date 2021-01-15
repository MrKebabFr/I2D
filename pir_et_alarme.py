# - *- coding: utf-8 -*-
import RPi.GPIO as GPIO # importer bibliotheque GPIO
import time # importer bibliothèque time
GPIO.setmode (GPIO.BCM) # definir la numerotation BCM


# definir des constantes
inter = 21
BP = 25
PIR = 23
buzzer = 18


# configurer les 4 GPIO en sortie ou en entree
GPIO.setup (inter,  GPIO.IN)
GPIO.setup (BP, GPIO.IN)
GPIO.setup (PIR, GPIO.IN)
GPIO.setup (buzzer, GPIO.OUT)


# definir la fonction Mode_manuel
def Mode_manuel():
    etatbp = GPIO.input(BP)                                # lire la valeur sur la patte ou il y a le BP et la mettre dans variable etatbp
    if (etatbp == 0):                                      # test de cette variable et se demander si elle est nulle
        print('Bouton relache')                            # si oui afficher un texte
        GPIO.output(buzzer, GPIO.LOW)                      # et arreter le buzzer
    else:                                                   # sinon
        print('Bouton appuyee')                            # afficher un texte
        GPIO.output(buzzer, GPIO.HIGH)                     # et faire sonner le buzzer


# definir la fonction Mode_auto
def Mode_auto(temps):
    etatpir = GPIO.input(PIR)                        # lire la valeur sur la patte ou il y a le PIR et la mettre dans variable etatpir
    if (etatpir == 0):                               # test de cette variable et se demander si elle est nulle
        print('Aucune detection')                    # si oui afficher un texte
        GPIO.output(buzzer, GPIO.LOW)                # et arreter le buzzer
    else:                                             # sinon
        print('Dectection')                          # afficher un texte
        GPIO.output(buzzer, GPIO.HIGH)               # et faire sonner le buzzer en alternance (4 lignes)
        time.sleep(temps)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(temps)


# programme principal
while True:                              # boucle infinie
    etatinter = GPIO.input(inter)        # lire la valeur sur la patte ou il y a l'inter et la mettre dans variable etatinter
    if(etatinter == 0):                  # test de cette variable et se demander si elle est nulle
        print ("Mode manuel")            # si oui afficher un texte
        Mode_manuel()                    # appel de la fonction Mode_manuel
    
    else:                                 # sinon
        print('Mode automatique')        # afficher un texte
        Mode_auto(5)                     # appel de la fonction Mode_auto

