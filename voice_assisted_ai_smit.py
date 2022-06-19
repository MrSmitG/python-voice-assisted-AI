from lib2to3.pgen2 import driver
import speech_recognition as sr
from selenium import webdriver

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()
    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()

                    if "search" in command:
                        driver = webdriver.Chrome()
                        print(driver)
                        driver.get(f"https://www.google.com/search?q={command.split('search')[-1]}")

            except sr.UnknownValueError:
                pass

listener = Voice()