from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MainActivity(FloatLayout):
    pass

class Gako(App):
    def build(self):
        return MainActivity()
        
if __name__ == '__main__':
    Gako().run()
