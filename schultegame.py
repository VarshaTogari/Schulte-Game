from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import time
from kivy.lang import Builder

class Gridlayout(GridLayout):

        txt = StringProperty('next:' + str(1))

        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuff1 = (str(random.choice(l)))
        l.remove(int(shuff1))
        shuff2 = (str(random.choice(l)))
        l.remove(int(shuff2))
        shuff3 = (str(random.choice(l)))
        l.remove(int(shuff3))
        shuff4 = (str(random.choice(l)))
        l.remove(int(shuff4))
        shuff5 = (str(random.choice(l)))
        l.remove(int(shuff5))
        shuff6 = (str(random.choice(l)))
        l.remove(int(shuff6))
        shuff7 = (str(random.choice(l)))
        l.remove(int(shuff7))
        shuff8 = (str(random.choice(l)))
        l.remove(int(shuff8))
        shuff9 = (str(random.choice(l)))
        l.remove(int(shuff9))

        li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def on_click(self, k):

            self.k = k
            for i in self.li:
                if i < 9:
                    if str(i) == self.k:
                        # print(i)
                        self.txt = ('next:' + str(i + 1))
                        self.li.remove(i)

                    else:
                        break
                elif i == 9:
                    if str(i) == self.k:
                        self.txt = ('next:' + str(i))


class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        start_button=Button(text="Tap to start",font_size= 28,size_hint=(0.4, 0.1),pos_hint={"center_x":0.5,'y':0.3},color= (1,1,1,0.6),background_color=(0.3,0.4,0.6,1))
        start_button.bind(on_press=self.switch_to_timer_screen)
        self.add_widget(start_button)

    def switch_to_timer_screen(self, instance):
        self.manager.current = 'game begins'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

        self.start_time = None
        self.timer_label = Label(text="Timer: 0.00 seconds",font_size=22,pos_hint={'x':0.03,'y':0.3},color=(0.8,0.6,0.6,0.9))
        self.add_widget(self.timer_label)

        stop_button = Button(text="over",size_hint=(0.1,0.1),pos_hint= {'x':0.9,'y':0.2})
        stop_button.bind(on_press=self.switch_to_result_screen)
        self.add_widget(stop_button)

    def on_enter(self):

        self.start_time = time.time()
        self.timer_event = Clock.schedule_interval(self.update_timer, 0.01)

    def on_leave(self):
        if self.timer_event:
            self.timer_event.cancel()

    def update_timer(self, dt):
        self.elapsed_time = time.time() - self.start_time
        self.timer_label.text= f"Timer: {self.elapsed_time:.2f} seconds"
        #print(elapsed_time)
    def switch_to_result_screen(self, instance):
        self.manager.current = 'gamer'

        self.manager.get_screen('gamer').set_timer_value(self.elapsed_time)

class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)

        self.timer_value_label = Label(text="Timer Value: N/A",pos_hint={'x':0.003 ,'y':0.2},font_size=18)
        self.add_widget(self.timer_value_label)
        self.best=6.94
        self.best_score =Label(text=f'Best score: {self.best:.2f} seconds',pos_hint={'x':0.03,'y':-0.1},font_size=18)
        self.add_widget(self.best_score)

    def set_timer_value(self, timer_value):
        self.timer_value_label.text = f"Score: {timer_value:.2f} seconds"
        if timer_value < self.best:
            self.best=timer_value
            self.best_score.text=f'Best score: {timer_value:.2f} seconds'

Builder.load_string('''
<Screen1>:
    name: 'main'
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size    
    Label:
        text: 'Schulte game'
        font_size:64
        size_hint: 1,1
    Label:
        text: '       INSTRUCTIONS\\n* Tap 1 to 9 as fast as you can \\n* Then press "over" \\n* (Do not press "over" before completing the game)\\n  The highest score is 6.94 \\n  Check if you can beat it'
        pos_hint: {'x':0.2,'y':0.3}
        font_size: 18
        color: 1,1,1,0.5
        font_name: 'Roboto-BoldItalic.ttf'
    Button:
        text: 'Tap to start'
        font_size: 28
        size_hint: 0.4,0.1
        pos_hint: {"center_x":0.5,'y':0.3}
        color: 1,1,1,0.6
        background_color: 0.3,0.2,0.5,1
        on_release: root.manager.current= 'game begins'

<Screen2>:
    name: 'game begins'
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size 
    Gridlayout:
    
<Screen3>:
    name: 'gamer'
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size                             

<Gridlayout>:
    cols:3
    rows:3
    pos_hint: {'x':0.42,'y':-0.3}

    Button:

        text: root.shuff1
        size_hint: None, None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff1)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff2
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        pos_hint: {"x":0.1}
        on_press: root.on_click(root.shuff2)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff3
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff3)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff4
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff4)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff5
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff5)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff6
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff6)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff7
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff7)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff8
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff8)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1
    Button:
        text: root.shuff9
        size_hint: None,None
        width: '100dp'
        height: '90dp'
        on_press: root.on_click(root.shuff9)
        color: 1,1,0.3,0.7
        background_color:0.8,0.5,0.5,1 
    Label:
        text: root.txt
        font_size: 28
        size_hint: 0.3,0.3
        pos_hint: {'x':0.8,'y':0.9}
''')

class Screenmanage(ScreenManager):
    pass

class TheLabApp(App):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Screen1(name='main'))
        screen_manager.add_widget(Screen2(name="game begins"))
        screen_manager.add_widget(Screen3(name='gamer'))
        return screen_manager

TheLabApp().run()
