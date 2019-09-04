from os import environ, path

import pocketsphinx
import sphinxbase
import tkinter as tk
import speech_recognition as sr

#for i in pocketsphinx.LiveSpeech():
#    print(i)

r = sr.Recognizer()
mike = sr.Microphone()

a = r.record(mike, duration=5)

print(r.recognize_wit(a, HPOWQAPVFVA72L3TOQSAKMAIGAN5PWWK))