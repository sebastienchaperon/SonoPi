#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pygame import mixer



mixer.init()

def play(chemin):
    mixer.music.load(chemin)
    mixer.music.play()

def verif():
    run = mixer.music.get_busy()
    return run
def decharge():
    mixer.music.stop()
def pause():
    mixer.music.pause()
def unpause():
    mixer.music.unpause()
