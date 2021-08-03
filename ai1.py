#importing all the python modules required

import pyttsx3

import random
import speech_recognition as sr
import pyaudio
from datetime import datetime

engine = pyttsx3.init()

lang = "en"
list1 = ["rock","paper","scissor"]
computer = random.choice(list1)
r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()


def options():
    engine.say("Welcome to Rooky AI")
    engine.runAndWait()
    engine.say("Please choose between, game,date,time ")
    engine.runAndWait()


def main_microphone():
    with sr.Microphone() as source:
        print("speak now ")
        audio = r1.listen(source,timeout=10)
        try:
            text = r1.recognize_google(audio)
            print(text)
            return audio
        except TimeoutError:
            engine.say("Timed out speak within 10 seconds.....")
            engine.runAndWait()
            print("Timed out speak within 10 seconds.....")


def listening_and_Responding():
        global r
        with sr.Microphone as source:
            print("listening ")
            audio1 = r.listen(source)
            text = r.recognize_google(audio1)
            print(text)
            return audio1


def date_fun(audio):
        engine.say(str(datetime.date(datetime.now())))
        engine.runAndWait()
        print(datetime.date(datetime.now()))

def time_fun(audio):
        engine.say(str(datetime.time(datetime.now())))
        engine.runAndWait()
        print(datetime.time(datetime.now()))

def game_fun():
        engine.say("Choose either rock,paper,scissor or say stop to quit")
        engine.runAndWait()
        print("choose either rock ,paper ,scissor")
        global computer
        audio2 = main_microphone()
        if "rock" in r2.recognize_google(audio2):
                        if computer == "rock":
                            engine.say("Draw")
                            engine.runAndWait()
                        elif computer == "scissor":
                            engine.say("Won")
                            engine.runAndWait()
                        elif computer == "paper":
                            engine.say("Lose")
                            engine.runAndWait()
        elif "paper" in r2.recognize_google(audio2):
                        if computer == "rock":
                            engine.say("Won")
                            engine.runAndWait()
                        elif computer == "scissor":
                            engine.say("lose")
                            engine.runAndWait()
                        elif computer == "paper":
                            engine.say("draw")
                            engine.runAndWait()
        elif "scissor" in r2.recognize_google(audio2):
                        if computer == "rock":
                            engine.say("lose")
                            engine.runAndWait()
                        elif computer == "scissor":
                            engine.say("draw")
                            engine.runAndWait()
                        elif computer == "paper":
                            engine.say("won")
                            engine.runAndWait()
        elif "stop" in r2.recognize_google(audio2):
                        engine.say("Thank you for playing")
                        engine.runAndWait()
                        exit()
def basic_ai(audio):
        if "game" in r2.recognize_google(audio):
            game_fun()

        elif "date" in r2.recognize_google(audio):
            date_fun(audio)

        elif "time" in r2.recognize_google(audio):
            time_fun(audio)

options()
basic_ai(main_microphone())