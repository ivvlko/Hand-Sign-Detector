import cv2

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from ObjectDetector import ObjectDetector


Builder.load_string('''
<Container>:

    orientation: 'horizontal'

    Button:
        text: 'Detect'
        size_hint_y: None
        font_size: 40
        pos_hint: {'top':.5,'right':.5}
        height: '32dp'
        color: 'white'
        background_color: 'purple'
        on_press: root.detect()

    Button:
        text: 'Exit'
        size_hint_y: None
        font_size: 40
        pos_hint: {'top':.5,'right':.5}
        height: '32dp'
        color: 'white'
        background_color: 'purple'
        on_press: app.close()
''')

class Container(BoxLayout):
    
    def detect(self):
        
        cap = cv2.VideoCapture(0)
        detector = ObjectDetector(cap)
        detector.detect()


class Detection(App):

    def build(self):
        return Container()
    
    def close(self):
        return App.get_running_app().stop()


Detection().run()