from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class FirstKivyMDApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, world! From KivyMDApp!")
    

if __name__ == "__main__":
    FirstKivyMDApp().run()
    
