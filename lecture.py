#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
continue_reading = True
GPIO.setwarnings(False)
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()



def lecture_rfid():
    while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)


        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
                try:
                  tagLu = (str(str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])))
                  return tagLu
                except:
                  tagLu = str(0)
                  return tagLu
