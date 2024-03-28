from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen

class MainMenu(Screen):
    def __init__(self, name='main_menu'):
        super().__init__(name=name)
        btn1 = Button(text='Button1')
        btn1.on_press = self.go_to_first
        btn2 = Button(text='Button2')
        btn2.on_press = self.go_to_second
        btn3 = Button(text='Button3')
        btn3.on_press = self.go_to_third
        btn4 = Button(text='Button4')
        btn4.on_press = self.go_to_fourth

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        self.add_widget(layout)

    def go_to_first(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'

    def go_to_second(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

    def go_to_third(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'third'

    def go_to_fourth(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'fourth'

class Button1(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back to Main Menu", on_press=self.go_to_main_menu)
        slider = Slider(min=1, max=800, value=15)
        input = TextInput()
        layout.add_widget(slider)
        layout.add_widget(input)
        layout.add_widget(back_btn)
        self.add_widget(layout)
       

    def go_to_main_menu(self, instance):
        self.manager.transition.direction = 'down'
        self.manager.current = 'main_menu'


class Button2(Screen):
    def __init__(self, name = "second"):
        super().__init__(name = name)
        layout = BoxLayout()
        scroll_view = ScrollView()
        content = BoxLayout(orientation='vertical')
        for i in range(1):
            label = Label(text="Dark label".format(i+1))
            content.add_widget(label)
        scroll_view.add_widget(content)
        back_btn = Button(text="Back", on_press=self.go_to_main_menu)
        togglebutton = ToggleButton(text='turn on-off', group='toggles', state='normal')
    
        layout.add_widget(scroll_view)
        layout.add_widget(togglebutton)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_to_main_menu(self, instance):
        self.manager.transition.direction = 'down'
        self.manager.current = 'main_menu'


class Button3(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        layout = BoxLayout()
        back_btn = Button(text="Back to Main Menu", on_press=self.go_to_main_menu)
        progressBar = ProgressBar(max=10)
        switch = Switch()
        layout.add_widget(switch)
        layout.add_widget(progressBar)
        layout.add_widget(back_btn)
        self.add_widget(layout)
    
    def go_to_main_menu(self, instance):
        self.manager.transition.direction = 'down'
        self.manager.current = 'main_menu'


class Button4(Screen):
    def __init__(self, name = "fourth"):
        
        super().__init__(name = name)
        layout = BoxLayout(orientation='horizontal') 
        back_btn = Button(text="Back", on_press=self.go_to_main_menu)
        checkBox = CheckBox()
        self.txt = Label(text="PUT YOUR ANSWER YES/NO")
        layout.add_widget(self.txt)  
        layout.add_widget(checkBox)
        layout.add_widget(back_btn) 
        self.add_widget(layout)

    def go_to_main_menu(self, instance):
        self.manager.transition.direction = 'down'
        self.manager.current = 'main_menu'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu())
        sm.add_widget(Button1())
        sm.add_widget(Button2())
        sm.add_widget(Button3()) 
        sm.add_widget(Button4())
        return sm

MyApp().run()
