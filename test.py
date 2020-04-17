import flask
from flask import jsonify, request
import sys
import requests
# sys.path.insert(1, 'C:/Workspace/Machine Learning Project/Testingtf2.0/models/research/object_detection')
# import Test1
# import final_checking


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/imageDetect', methods=['POST'])
def lat_res():
    # print("Step3")
    # test1_value = final_checking.final_checking
    # print("Step4")


    # object_val = test1_value.task3_final()

    # print(object_val)

    req_data = request.get_json()
    VIN_NO = req_data['vinNo']
    QC_TYPE = req_data['qcType']
    ENVIRONMENT_TYPE = req_data['enviType']
    IMG_PATH = req_data['imagePath']
    print("request Body is --->> {} , {}, {}, {}".format(VIN_NO, ENVIRONMENT_TYPE, QC_TYPE, IMG_PATH))

    objects =  [{ "RXBC_PWR_WDW_SW" : 98.67 } ,{ "RXBC_FAB_ARR" : 98.67 } ,{ "RXBC_PB_PHND" : 98.67 }  ,
    { "RXBC_MANUAL_AUD/NAM" : 98.67 } ,{ "RXBC_NO_UGLB" : 98.67 } ,{ "RXBC_NO_LGLB" : 98.67 } ,{ "RXBC_TINT_AV" : 98.67 } ,{ "RXBC_BLACK_MIRROR" : 98.67 } ,
    { "RXBC_TINT_TD" : 98.67 } ,{ "RXBC_TRIP_SW"  : 98.67 } ]

    result = []
    for obj in objects:
        for val in obj:
            print()
            result.append(val +"~" +str(obj[val]))


    ressult1 = ['RXBC_PWR_WDW_SW~91.63', 'RXBC_CTINT_AV~91.63', 'RXBC_SHINY_CF~91.63']
    data = {"objectList" : result,"colorName" : ""}
    return jsonify(data)


app.run()