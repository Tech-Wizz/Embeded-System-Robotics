import time, serial, sys
from tkinter import *
from TangoController import *

usb = serial.Serial('/dev/ttyACM0')
tangoController = Tango_Controller(usb)


self = Tk()

class Keyboard_Input:
    self.title('Robot')
    self.geometry("200x100")
    self.speed = 0
    self.label = Label(self, text="")


    def forward(e):
        self.label.destroy()
        self.label = Label(self, text="Forward")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_backward_forward(1)

    def backward(e):
        self.label.destroy()
        self.label = Label(self, text="Backward")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_backward_forward(-1)

    def turnRight(e):
        self.label.destroy()
        self.label = Label(self, text="Turning Right")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_left_right(1)

    def turnLeft(e):
        self.label.destroy()
        self.label = Label(self, text="Turning Left")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_left_right(-1)
        

    def twistRight(e):
        self.label.destroy()
        self.label = Label(self, text="Twisting Right")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_pan_waist(-1)

    def twistLeft(e):
        self.label.destroy()
        self.label = Label(self, text="Twisting Left")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_pan_waist(1)

    def lookUp(e):
        self.label.destroy()
        self.label = Label(self, text="Looking Up")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_tilt_neck(1)

    def lookDown(e):
        self.label.destroy()
        self.label = Label(self, text="Looking Down")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_tilt_neck(-1)

    def lookRight(e):
        self.label.destroy()
        self.label = Label(self, text="Looking Right")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_pan_neck(-1)

    def lookLeft(e):
        self.label.destroy()
        self.label = Label(self, text="Looking Left")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.adjust_pan_neck(1)

    def speedHigh(e):
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

    def speedLow(e):
        self.label.destroy()
        self.label = Label(self, text="Speed 1")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        self.speed = 1

    def stop(e):
        self.label.destroy()
        self.label = Label(self, text="Stop")
        self.label.pack()
        self.label.place(relx = 0.5, rely = 0)
        tangoController.stop()

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
