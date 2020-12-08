#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import MFRC522
import os
import pickle

GPIO.setwarnings(False)

print("-------------------------")
print("Enregistrement Tag RFID")
print("-------------------------")

continuer = True

try:
    with open('/home/pi/projet/projet_actif/medias', 'rb') as fichier:
        mes_albums = pickle.load(fichier)
        print("mediatheque chargée")

except:
    mes_albums = {}
    print("mediathèque vide")


def lecture_tag():
    tagLu = 0
    while type(tagLu) != str:
        MIFAREReader = MFRC522.MFRC522()
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        lecture_prev = 0
        if status == MIFAREReader.MI_OK:
            (status,uid) = MIFAREReader.MFRC522_Anticoll()           
            try:
                tagLu = (str(str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])))
                if tagLu != lecture_prev:
                    lecture_prev = tagLu
                    return tagLu
            except IndexError:
                print("erreur lecture type 1")
                lecture_tag()
            except TypeError:
                print("erreur lecture type 2")
                lecture_tag()
        else:
            lecture_tag()

def selection_artiste():
    i = 0
    artiste_liste = [f for f in os.listdir('/home/pi/Music')]
    artiste_liste.sort()
 
    num_artiste = []
    for i in range(i,len(artiste_liste)):
        num_artiste.append(i+1)
        i+1
        mes_artistes=dict(zip(num_artiste,artiste_liste))
 
    for cle, valeur in mes_artistes.items():
        print("n°{}:-{}".format(cle,valeur))
    print("selectionner numero de l'artiste")
    choix_artiste = input()
    choix_artiste = int(choix_artiste)
    artiste_select = mes_artistes.get(choix_artiste)
 
    return artiste_select
                     
def selection_album(artiste):
    repertoire = ('/home/pi/Music/',artiste)
    repertoire_str = ''.join(repertoire)

    i = 0
    album_liste = [f for f in os.listdir(repertoire_str)]
    album_liste.sort()

    num_album = []
    for i in range(i,len(album_liste)):
        num_album.append(i+1)
        i+1
        mes_albums_a=dict(zip(num_album,album_liste))

    for cle, valeur in mes_albums_a.items():
        print("n°{}:-{}".format(cle,valeur))
    print("selectionner numero de l'album")
    choix_album = input()
    choix_album = int(choix_album)
    album_select = mes_albums_a.get(choix_album)

    return album_select


def ecriture(tag_select,nouveau_str):

    mes_albums[tag_select] = nouveau_str

    with open('medias', 'wb') as f1:
        pickle.dump(mes_albums, f1)
    
    
    
while continuer:    
    print("1 : Enregistrer un nouveau tag")
    print("2 : Quitter")
    selection = input()

    if selection == "1":
        print("Veuillez poser le tag à enregistrer")
        tag_select = lecture_tag()
        try:
            print ("UID du nouveau tag : " + tag_select)
        except TypeError:
            print("erreur lecture type 3")
            lecture_tag()
        print("*****veuillez selectionner l'artiste*******")
        artiste = selection_artiste()
        print("artiste choisi : ",artiste)
        print("******veuillez selectionner un album********")
        album = selection_album(artiste)
        print("album choisi : ", album)
        nouveau = ('/home/pi/Music/',artiste,'/',album,'/')
        nouveau_str = ''.join(nouveau)
        print("emplacement de l'album : ", nouveau_str)
        print("ecriture dans la mediathèque")
        ecriture(tag_select, nouveau_str)
            
    elif selection == "2":
        continuer = False

    else:
        print("choix non reconnu")

