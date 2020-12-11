#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lecture
import playlist
import son
import RPi.GPIO as GPIO
import time

pinBtnStop = 37
pinBtnPlay = 31
pinBtnAvance = 33
pinBtnRecule = 35

etat_pp = True

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pinBtnStop, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pinBtnPlay, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pinBtnAvance, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pinBtnRecule, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

LED_b = 36 
LED_r = 38
LED_v = 40

GPIO.setup(LED_v, GPIO.OUT) 
GPIO.setup(LED_r, GPIO.OUT)
GPIO.setup(LED_b, GPIO.OUT)

GPIO.output(LED_v, GPIO.HIGH)
GPIO.output(LED_r, GPIO.HIGH)
GPIO.output(LED_b, GPIO.LOW)

previous = 0
etat = False
liste_file = []
repertoire = "blabla"



try:
    while True:
        tag = lecture.lecture_rfid()


        present_bdd = playlist.comparaison(tag)


        previous, etat = playlist.lecture_en_cours(tag, previous)


        if etat == False:
            if present_bdd == True:

                repertoire, liste_file = playlist.infos(tag)
                n = 0
                alire = liste_file[n]
                chemin = repertoire+alire
                son.play(chemin)
                GPIO.output(LED_b, GPIO.HIGH)
                GPIO.output(LED_r, GPIO.LOW)

        if etat == True:
            if present_bdd == True:
                encours = son.verif()
                if encours == 0:
                    n = n + 1
                    repertoire, liste_file = playlist.infos(tag)
                    longueur = len(liste_file)
                    if n<longueur:
                        alire = liste_file[n]
                        chemin = repertoire+alire
                        son.play(chemin)
                        GPIO.output(LED_b, GPIO.HIGH)
                        GPIO.output(LED_r, GPIO.LOW)
                    if n == longueur:
                        son.decharge()
                        GPIO.output(LED_r, GPIO.HIGH)
                        GPIO.output(LED_b, GPIO.LOW)

        etat_btn_stop = GPIO.input(pinBtnStop)

        if (etat_btn_stop == True):
            repertoire, liste_file = playlist.infos(tag)
            longueur = len(liste_file)
            n = longueur - 1
            son.decharge()
            GPIO.output(LED_r, GPIO.HIGH)
            GPIO.output(LED_b, GPIO.LOW)
                
        
            
        etat_btn_play = GPIO.input(pinBtnPlay)

        if (etat_btn_play == True):
            if (etat_pp == True):
                son.pause()
                time.sleep(.5)
                etat_pp = False
            elif (etat_pp == False):
                son.unpause()
                time.sleep(.5)
                etat_pp = True

        etat_btn_avance = GPIO.input(pinBtnAvance)

        if (etat_btn_avance == True):
            n = n + 1
            repertoire, liste_file = playlist.infos(tag)
            longueur = len(liste_file)
            if n<longueur:
                alire = liste_file[n]
                chemin = repertoire+alire
                son.play(chemin)
                GPIO.output(LED_b, GPIO.HIGH)
                GPIO.output(LED_r, GPIO.LOW)
            if n == longueur:
                son.decharge()
                GPIO.output(LED_r, GPIO.HIGH)
                GPIO.output(LED_b, GPIO.LOW)
            
        etat_btn_recule = GPIO.input(pinBtnRecule)

        if (etat_btn_recule == True):
            n = n - 1
            repertoire, liste_file = playlist.infos(tag)
            longueur = len(liste_file)
            if n<=longueur:
                alire = liste_file[n]
                chemin = repertoire+alire
                son.play(chemin)
                GPIO.output(LED_b, GPIO.HIGH)
                GPIO.output(LED_r, GPIO.LOW)
            if n < 0:
                n = longueur - 1
                alire = liste_file[n]
                chemin = repertoire+alire
                son.play(chemin)
                GPIO.output(LED_b, GPIO.HIGH)
                GPIO.output(LED_r, GPIO.LOW)
       
except KeyboardInterrupt:
    son.decharge()
    GPIO.cleanup()

finally:
    son.decharge()
    GPIO.cleanup()
    
