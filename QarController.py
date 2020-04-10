from TensorFlowController import final_checking as tf
from ColorDetectionController import Color_Detection as color
import flask
from flask import jsonify, request
import sys, os

# out = final_checking.final_checking

# func = out.image_detection()
# print(func)


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/imageDetect', methods=['POST'])
def lat_res():
    IMG_PATH = "C:/Workspace/Machine Learning Project/Images/Test Images"
    object_val = tf.image_detection(IMG_PATH)

    COLOR_VALUE = color.detect_Color(os.path.join(IMG_PATH,os.listdir(IMG_PATH)[0]))

    data = {"objectList" : object_val, "colorName" : COLOR_VALUE}
    return jsonify(data)


app.run()