##import time, serial, sys
from tkinter import *
##from TangoController import *

self = Tk()

class Keyboard_Input:
    self.title('Robot')
    self.geometry("400x400")

    def forward(e):
        myLabel = Label(self, text="Forward")
        myLabel.pack()

    def backward(e):
        myLabel = Label(self, text="Backward")
        myLabel.pack()

    def turnRight(e):
        myLabel = Label(self, text="Turning Right")
        myLabel.pack()

    def turnLeft(e):
        myLabel = Label(self, text="Turning Left")
        myLabel.pack()

    def twistRight(e):
        myLabel = Label(self, text="Twisting Right")
        myLabel.pack()

    def twistLeft(e):
        myLabel = Label(self, text="Twisting Left")
        myLabel.pack()

    def lookUp(e):
        myLabel = Label(self, text="Looking Up")
        myLabel.pack()

    def lookDown(e):
        myLabel = Label(self, text="Looking Down")
        myLabel.pack()

    def lookRight(e):
        myLabel = Label(self, text="Looking Right")
        myLabel.pack()

    def lookLeft(e):
        myLabel = Label(self, text="Looking Left")
        myLabel.pack()

    def speedHigh(e):
        myLabel = Label(self, text="Speed 3")
        myLabel.pack()

    def speedMed(e):
        myLabel = Label(self, text="Speed 2")
        myLabel.pack()

    def speedLow(e):
        myLabel = Label(self, text="Speed 1")
        myLabel.pack()

    def stop(e):
        myLabel = Label(self, text="Stop")
        myLabel.pack()

    self.bind('<w>', forward)
    self.bind('<W>', forward) #also handles capital letters if caps lock is on
    self.bind('<s>', backward)
    self.bind('<S>', backward)
    self.bind('<d>', turnRight)
    self.bind('<D>', turnRight)
    self.bind('<a>', turnLeft)
    self.bind('<A>', turnLeft)
    self.bind('<e>', twistRight)
    self.bind('<E>', twistRight)
    self.bind('<q>', twistLeft)
    self.bind('<Q>', twistLeft)
    self.bind('<Up>', lookUp)
    self.bind('<Down>', lookDown)
    self.bind('<Right>', lookRight)
    self.bind('<Left>', lookLeft)
    self.bind(3, speedHigh) #these are keyboard numbers that will set the speed
    self.bind(2, speedMed)
    self.bind(1, speedLow)
    self.bind('<z>', stop)
    self.bind('<Z>', stop)


    self.mainloop()


#------------------
#class Keyboard_Input:
#    DEFAULT_VALID = {'<Up>', '<Left>', '<Down>', '<Right>', '<space>', '<z>', '<c>', '<w>', '<s>', '<a>', '<d>'}
#    def __init__(self, win, control_list = DEFAULT_VALID):
#        self.win = win
#        self.control_list = control_list
#        return
#    pass
