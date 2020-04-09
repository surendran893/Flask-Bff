import TensorFlowController as tf
import flask
from flask import jsonify, request
import sys

# out = final_checking.final_checking

# func = out.image_detection()
# print(func)


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/imageDetect', methods=['POST'])
def lat_res():
    IMAGE_DETECTION_CLASS = tf.final_checking
    object_val = IMAGE_DETECTION_CLASS.image_detection()

    data = {"objectList" : object_val}
    return jsonify(data)


app.run()