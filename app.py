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
        id: detect_btn
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
        camera_ports = [1, 0, 2, 3, 99, 100]
        
        try:          
            for port in camera_ports:
                try:
                    cap = cv2.VideoCapture(port)
                    detector = ObjectDetector(cap)
                    detector.detect()
                    break
                except Exception as e:
                    print(f'No Camera at {port}')
        except:
            self.ids['detect_btn'].text = 'Camera Not Found'


class Detection(App):

    def build(self):
        return Container()
    
    def close(self):
        return App.get_running_app().stop()


Detection().run()