#STARTER CODE GIVEN
#import speech_recognition as sr
#listening = True
#mic = sr.Microphone()





import speech_recognition as sr
import time, serial, sys
from TangoController import *
usb = serial.Serial('/dev/ttyACM0')
tangoController = Tango_Controller(usb)
from tkinter import *
from time import sleep

self = Tk()


def forward():
        if (tangoController.motors['Right_Wheel'].get_speed() == 0):
                tangoController.adjust_backward_forward(2)
        else:
                tangoController.adjust_backward_forward(1)

def backward():
        if (tangoController.motors['Right_Wheel'].get_speed() == 0):
                tangoController.adjust_backward_forward(-2)
        else:
                tangoController.adjust_backward_forward(-1)

def turnRight():
        tangoController.adjust_left_right(3)

def turnLeft():
        tangoController.adjust_left_right(-3)

def twistRight():
        tangoController.adjust_pan_waist(-1)

def twistLeft():
        tangoController.adjust_pan_waist(1)

def lookUp():
        tangoController.adjust_tilt_neck(1)

def lookDown():
        tangoController.adjust_tilt_neck(-1)

def lookRight():
        tangoController.adjust_pan_neck(-1)

def lookLeft():
        tangoController.adjust_pan_neck(1)

def speedHigh():
        self.label.destroy()
        self.label = Label(self, text="Speed 3")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        self.speed = 3

def speedMed(e):
        self.label.destroy()
        self.label = Label(self, text="Speed 2")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        self.speed = 2

def speedLow():
        self.speed = 1

def stop():
        tangoController.stop()


while(True):
    r = sr.Recognizer()
#     r.dynamic_energy_threshold = False
#     r.energy_threshold = 2000
    speech = sr.Microphone(device_index=6)
    with speech as source:
        print("say something!…")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language = 'en-US')
        if (recog == 'forward'):
                forward()
        if (recog == 'backward'):
                backward()
        if (recog == 'stop'):
                stop()
        if (recog == 'twist right'):
                twistRight()
        if (recog == 'twist left'):
                twistLeft()
        if (recog == 'look up'):
                lookUp()
        if (recog == 'look down'):
                lookDown()
        if (recog == 'look right'):
                lookRight()
        if (recog == 'look left'):
                lookLeft()
        if (recog == 'turn right'):
                turnRight()
                sleep(0.65)
                stop()
        if (recog == 'turn left'):
                turnLeft()
                sleep(0.75)
                stop()


        print("You said: " + recog)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))







#while listening:
#    with sr.Microphone() as source:
#        r = sr.Recognizer()
#        r.adjust_for_ambient_noise(source)
#        r.dyanmic_energythreshhold = 3000

#        try:
#            print("listening")
#            audio  = r.listening(source)
#            print("Got audio")
#            word = r.reconize_google(audio)
#            print(word)
#        except sr.UnknownValueError:
#            print("Don't  know that word")

#mic = sr.Microphone()

#with mic as source:
#        au = r.listen(source)

#print("here")
#word = r.reconize_google(au)
#print("here" word)

