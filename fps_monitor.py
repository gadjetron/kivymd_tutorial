KV = '''
MDScreen:

    MDLabel:
        text: "Hello, World!"
        halign: "center"
'''

from kivy.lang import Builder

from kivymd.app import MDApp

class FPSMonitorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        self.fps_monitor_start()
        
if __name__ = "__main__":
    FPSMonitorApp().run()
