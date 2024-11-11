import subprocess
import pygetwindow as gw
import time
import pyttsx3

subprocess.Popen(['notepad', 'C:/AllNewFiles/read_from_files/read.txt'])
time.sleep(2)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

with open("C:/AllNewFiles/read_from_files/read.txt") as file:
    lines = file.readlines()

for line in lines:
    # print(line.strip())
    engine.say(line.strip())
    engine.runAndWait()
    time.sleep(0.5)

engine.stop()
