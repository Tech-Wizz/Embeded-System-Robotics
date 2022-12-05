import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from TextToSpeech import *



class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    
    def __init__(self, **kwargs):
        arrayAction = [0,0,0,0,0,0]
        amount = 0
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #Set colums
        self.rows = 6
        self.columns = 3

        #add widgets
        self.lookLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookLeft.png',
                    background_down ='Buttons/down/lookLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookLeft.bind(on_press=self.pressLookLeft)
        self.add_widget(self.lookLeft)
        ####################################################
        self.lookRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookRight.png',
                    background_down ='Buttons/down/lookRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookRight.bind(on_press=self.pressLookRight)
        self.add_widget(self.lookRight)
        ####################################################
        self.lookDown = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookDown.png',
                    background_down ='Buttons/down/lookDown.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookDown.bind(on_press=self.pressLookDown)
        self.add_widget(self.lookDown)
        ####################################################
        self.lookUp = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/lookUp.png',
                    background_down ='Buttons/down/lookUp.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.lookUp.bind(on_press=self.pressLookUp)
        self.add_widget(self.lookUp)
        ####################################################
        self.twistLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistLeft.png',
                    background_down ='Buttons/down/twistLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistLeft.bind(on_press=self.pressTwistLeft)
        self.add_widget(self.twistLeft)
        ####################################################
        self.twistRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/twistRight.png',
                    background_down ='Buttons/down/twistRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.twistRight.bind(on_press=self.pressTwistRight)
        self.add_widget(self.twistRight)
        ####################################################
        self.turnLeft = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/turnLeft.png',
                    background_down ='Buttons/down/turnLeft.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.turnLeft.bind(on_press=self.pressTurnLeft)
        self.add_widget(self.turnLeft)
        ####################################################
        self.turnRight = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/turnRight.png',
                    background_down ='Buttons/down/turnRight.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.turnRight.bind(on_press=self.pressTurnRight)
        self.add_widget(self.turnRight)
        ####################################################
        self.Forewards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Forewards.png',
                    background_down ='Buttons/down/Forewards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Forewards.bind(on_press=self.pressForewards)
        self.add_widget(self.Forewards)
        ####################################################
        self.Backwards = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/Backwards.png',
                    background_down ='Buttons/down/Backwards.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.Backwards.bind(on_press=self.pressBackwards)
        self.add_widget(self.Backwards)
        ####################################################
        self.RUN = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/RUN.png',
                    background_down ='Buttons/down/RUN.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.RUN.bind(on_press=self.pressRUN)
        self.add_widget(self.RUN)
        ####################################################
        self.reset = Button(color =(1, 0, .65, 1),
                    background_normal = 'Buttons/normal/reset.png',
                    background_down ='Buttons/down/reset.png',
                    size_hint_y = None,
                    height=100,
                    size_hint_x = None,
                    width=100,
                   )
        self.reset.bind(on_press=self.pressReset)
        self.add_widget(self.reset)
        ####################################################
        self.question = Label(text="",
                              font_size = 36,
                              color = '#00abFF')
        self.add_widget(self.question)

        
    def makeLog(self, instance):
        i = 0
        myLog = ""
        while i < 6:
            if arrayAction[i] == 0:
                myLog = ""
                i = i + 1
            elif arrayAction[i] == 1:
                myLog = myLog + "Backward   "
                i = i + 1
            elif arrayAction[i] == 2:
                myLog = myLog + "Forwards   "
                i = i + 1
            elif arrayAction[i] == 3:
                myLog = myLog + "TurnRight   "
                i = i + 1
            elif arrayAction[i] == 4:
                myLog = myLog + "TurnLeft   "
                i = i + 1
            elif arrayAction[i] == 5:
                myLog = myLog + "TwistRight   "
                i = i + 1
            elif arrayAction[i] == 6:
                myLog = myLog + "TwistLeft   "
                i = i + 1
            elif arrayAction[i] == 7:
                myLog = myLog + "LookUp   "
                i = i + 1
            elif arrayAction[i] == 8:
                myLog = myLog + "LookDown   "
                i = i + 1
            elif arrayAction[i] == 9:
                myLog = myLog + "LookRight   "
                i = i + 1
            elif arrayAction[i] == 10:
                myLog = myLog + "LookLeft   "
                i = i + 1
        self.question.text = myLog

               

    ##Buttons when pressed

    def pressRUN(self,instance):
        talkBack("RUN")

        
    def pressReset(self,instance):
        talkBack("reset")
        arrayAction[0] = 0
        arrayAction[1] = 0
        arrayAction[2] = 0
        arrayAction[3] = 0
        arrayAction[4] = 0
        arrayAction[5] = 0

    def pressBackwards(self,instance):
        #Action is 1
        if amount < 6:
            talkBack("Backwards")
            arrayAction[i] = 1
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        
    def pressForewards(self,instance):
        #Action is 2
        if amount < 6:
            talkBack("Forewards")
            arrayAction[i] = 2
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")

    def pressTurnRight(self,instance):
        #Action is 3
        if amount < 6:
            talkBack("Turn Right")
            arrayAction[i] = 3
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        
    def pressTurnLeft(self,instance):
        #Action is 4
        if amount < 6:
            talkBack("Turn Left")
            arrayAction[i] = 4
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")

    def pressTwistRight(self,instance):
        #Action is 5
        if amount < 6:
            talkBack("Twist Right")
            arrayAction[i] = 5
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        
    def pressTwistLeft(self,instance):
        #Action is 6
        if amount < 6:
            talkBack("Twist Left")
            arrayAction[i] = 6
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")

    def pressLookUp(self,instance):
        #Action is 7
        if amount < 6:
            talkBack("Look Up")
            arrayAction[i] = 7
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        
    def pressLookDown(self,instance):
        #Action is 8
        if amount < 6:
            talkBack("Look Down")
            arrayAction[i] = 8
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")

    def pressLookRight(self,instance):
        #Action is 9
        if amount < 6:
            talkBack("Look Right")
            arrayAction[i] = 9
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        
    def pressLookLeft(self,instance):
        #Action is 10
        if amount < 6:
            talkBack("Look Left")
            arrayAction[i] = 10
            amount = amount + 1
        else:
            talkBack("You have hit the limit of actions")
        

class MyApp(App):
    

    def build(self):
        Window.fullscreen = True
        return MyGridLayout()
##        self.window = GridLayout()
##        self.icon = 'hello.jpg'
##        self.window.cols = 1
##        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
##        self.window.add_widget(Image(source='hello.jpg',
##                                     size_hint = (3,3)))
##        self.question = Label(text="What is your robot's name?",
##                              font_size = 36,
##                              color = '#00abFF')
##        self.window.add_widget(self.question)
##        self.answer = TextInput(multiline = False,
##                                padding_y = (20 ,20),
##                                padding_x = (10,10),
##                                size_hint = (1, 0.9))
##        self.window.add_widget(self.answer)

##        self.button1 = Button(color =(1, 0, .65, 1),
##                     background_normal = 'Buttons/normal/RUN.png',
##                     background_down ='Buttons/down/RUN.png',
##                     size_hint = (.3, .3),
##                     pos_hint = {"x":0.35, "y":0.3}
##                   )
##        self.button1.bind(on_press = self.callback)
##        self.window.add_widget(self.button1)
        
        return self.window

    def callback(self, instance):
        print(instance)
        self.question.text = "Hello " + self.answer.text + "!"
        talkBack(self.question.text)
 

########These are the 7 actions our robot has to do########
    def motorsRun(speed, time, direction):
        pass

    def motorsTurn(direction, time):
        pass

    def headTilt():
        pass

    def headPan():
        pass

    def waistTurn():
        pass

    def speechInput():
        pass

    

def main():
    MyApp().run()
main()
