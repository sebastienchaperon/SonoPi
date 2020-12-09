#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import os


try:
    with open('/home/pi/SonoPi/medias','rb') as fichier:
        mes_albums = pickle.load(fichier)
        print("mediatheque chargée")
except:
    print("mediatheque absente")
def comparaison(tag):
    if tag in mes_albums.keys():
        existant = True
        return existant
    else:
        existant = False
        return existant

def infos(tag):
    alire = mes_albums.get(tag)
    playlist = str(alire)
    liste = os.listdir(playlist)
    liste.sort()
    return playlist, liste

def lecture_en_cours(tag, previous = 0):
    if tag == previous:
        etat = True
        return previous, etat
    if tag != previous:
        previous = tag
        etat = False
        return previous, etat

