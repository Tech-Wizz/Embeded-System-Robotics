from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random



#Builder.load_file('images.kv')

class MyLayout(GridLayout):
    img = Image(source='maps/One.png')
    map = 1
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.bottom = GridLayout(size_hint_y = None,
                    height=50)
        self.bottom.cols = 2
        
        self.img.keep_ratio= False
        self.img.allow_stretch = True 
        self.add_widget(self.img)
        self.callback
        self.add_widget(self.bottom)
        self.att = Button(color =(1, 0, .65, 1),
                    size_hint_y = None,
                    height=50,
                   )
        self.att.bind(on_press=self.callback)
        self.bottom.add_widget(self.att)

        self.all = Button(color =(1, 0, .65, 1),
                    size_hint_y = None,
                    height=50,
                   )
        self.all.bind(on_press=self.callback)
        self.bottom.add_widget(self.all)
        

    def callback(self, instance):
        map = random.randint(1,9)
        if map == 1:
            self.img.source = 'maps/One.png'
        elif map == 2:
            self.img.source = 'maps/two.png'
        elif map == 3:
            self.img.source = 'maps/three.png'
        elif map == 4:
            self.img.source = 'maps/six.png'
        elif map == 5:
            self.img.source = 'maps/seven.png'
        elif map == 6:
            self.img.source = 'maps/eight.png'
        elif map == 7:
            self.img.source = 'maps/eleven.png'
        elif map == 8:
            self.img.source = 'maps/twelve.png'
        elif map == 9:
            self.img.source = 'maps/thirteen.png'


class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (800,480)
        Window.top = 10
        Window.left = 50
        #img = Image(source='Buttons/normal/RUN.png')
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
