import tensorflow as tf
import numpy as np

import cv2
import os

from time import sleep

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'    
tf.get_logger().setLevel('ERROR')   

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
    
from object_detection.utils import label_map_util
from AudioPlayer import AudioPlayer

import warnings
warnings.filterwarnings('ignore') 


class SignDetector:

    PATH_TO_SAVED_MODEL = os.getcwd() + '\\exported-models\\resnet\\saved_model'
    category_index = label_map_util.create_category_index_from_labelmap(os.getcwd() + '\\exported-models\\label_map.pbtxt', use_display_name=True)
    detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

    def __init__(self, cap):
        """
        cap - cv2 VideoCapture object;
        """
        self.cap = cap
        self.is_playing = False
        self.audio_player = None

    def detect(self):

        while True:
            _, image_np = self.cap.read()

            image_np_expanded = np.expand_dims(image_np, axis=0)
            input_tensor = tf.convert_to_tensor(image_np_expanded)
            detections = self.detect_fn(input_tensor)
            num_detections = int(detections.pop('num_detections'))
            detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
            detections['num_detections'] = num_detections
            detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
            
            self.has_detected_sign(detections['detection_classes'], detections['detection_scores'])

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def has_detected_sign(self, labels, score):
        """
        80% certainty to activate player. It's detecting signs all the time, just low probability
        """
        if score[0] >= 0.8:
            self.activate_player(labels[0])
        return
    
    def activate_player(self, label):

        if self.is_playing == False:
             self.audio_player = AudioPlayer()

        if label == 1 and self.is_playing == False:
            print('Starting player...')
            self.audio_player.play_song()
            self.is_playing = True
        
        elif label == 2 and self.is_playing == True:
            print('Stopping player...')
            self.audio_player.stop()
            self.is_playing = False
            self.audio_player = None
        
        elif label == 3 and self.is_playing == True:
            print('Going next')
            self.audio_player.go_next()
            sleep(3)

        elif label == 4 and self.is_playing == True:
            print('Going back')
            self.audio_player.go_back()
            sleep(3)
        
        return
        
