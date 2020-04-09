import os
import cv2
import numpy as np
import tensorflow as tf
import sys
sys.path.insert(1, 'C:/Workspace/Machine Learning Project/Testingtf2.0/models/research/object_detection')


class final_checking(object):
    

    def image_detection():
        
        sys.path.insert(1, 'C:/Workspace/Machine Learning Project/Testingtf2.0/models/research/object_detection')
        sys.path.append("..")

        from utils import label_map_util
        from utils import visualization_utils as vis_util

        # Name of the directory containing the object detection module we're using
        MODEL_NAME = 'inference_graph'


        CWD_PATH = "C:/Workspace/Machine Learning Project/Tensorflow_2.0/models/research/object_detection"

        IMG_PATH = "C:/Workspace/Machine Learning Project/Images/Test Images"

        PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

        PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

        NUM_CLASSES = 50

        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        category_index =  label_map_util.create_category_index(categories)

        detection_graph = tf.Graph()

        with detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            sess = tf.compat.v1.Session(graph=detection_graph)

        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')


        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')

        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        objects = []
        object_dict = {}

        for IMAGE_NAME in os.listdir(IMG_PATH):

            PATH_TO_IMAGE = os.path.join(IMG_PATH,IMAGE_NAME)

            print("Image pathis locat ->>>>>>>>>>>>>>>",PATH_TO_IMAGE)

            #Load image using OpenCV and
            #expand image dimensions to have shape: [1, None, None, 3]
            #i.e. a single-column array, where each item in the column has the pixel RGB value
            image = cv2.imread(PATH_TO_IMAGE)
            image_expanded = np.expand_dims(image, axis=0)

            #Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict = {image_tensor: image_expanded})

            
            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=4,
                min_score_thresh=0.60)

            threshold = 0.5 # in order to get higher percentages you need to lower this number; usually at 0.01 you get 100% predicted objects
            for index, value in enumerate(classes[0]):
                # print("index  is {} and valuie si {}".format(index, value))                
                if scores[0, index] > threshold:
                    # object_dict[(category_index.get(value)).get('name')] = round((scores[0, index]*100),2)
                    # objects.append(object_dict)
                    key = (category_index.get(value)).get('name')
                    val = round((scores[0, index]*100),2)
                    if key in object_dict:
                        if val > object_dict[key]:
                            object_dict[key] = val
                    else:
                        object_dict[key] = val

        for key, val in object_dict.items():
            objects.append(key + "~" + str(val))
            

        return objects
