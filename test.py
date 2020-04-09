import flask
from flask import jsonify, request
import sys
# sys.path.insert(1, 'C:/Workspace/Machine Learning Project/Testingtf2.0/models/research/object_detection')
# import Test1
import final_checking


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/imageDetect', methods=['POST'])
def lat_res():
    print("Step3")
    test1_value = final_checking.final_checking
    print("Step4")


    object_val = test1_value.task3_final()

    print(object_val)
    objects =  [{ "RXBC_MT" : 99.0 } ,{ "RXBC_12V_CH" : 99.0 } ]

    result = []
    for obj in objects:
        for val in obj:
            print()
            result.append(val +"~" +str(obj[val]))


    ressult1 = ['RXBC_PWR_WDW_SW~91.63', 'RXBC_CTINT_AV~91.63', 'RXBC_SHINY_CF~91.63']
    data = {"objectList" : object_val}
    return jsonify(data)


app.run()