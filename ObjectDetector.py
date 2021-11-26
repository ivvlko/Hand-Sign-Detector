import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings('ignore')  
import cv2

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    

tf.get_logger().setLevel('ERROR')   

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
    
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import numpy as np


class ObjectDetector:

    PATH_TO_SAVED_MODEL = 'D:\\projects\\DesktopAppDetection\\exported-models\\resnet\\saved_model'
    category_index = label_map_util.create_category_index_from_labelmap('exported-models\\label_map.pbtxt', use_display_name=True)
    detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

    def __init__(self, cap):
        """
        cap - cv2 VideoCapture object;
        """
        self.cap = cap

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
            image_np_with_detections = image_np.copy()

            viz_utils.visualize_boxes_and_labels_on_image_array(
                                                                image_np_with_detections,
                                                                detections['detection_boxes'],
                                                                detections['detection_classes'],
                                                                detections['detection_scores'],
                                                                self.category_index,
                                                                use_normalized_coordinates=True,
                                                                max_boxes_to_draw=2,
                                                                min_score_thresh=.50,
                                                                agnostic_mode=False
                                                                )

            cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

