import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]




@app.route('/', methods=['POST'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/service', methods=['POST'])
def service():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)


    return jsonify(results)


@app.route('/books/<val>', methods=['POST'])
def test(val):
    obj = "value is {}".format(val)
    return obj


objects =  [{'RXBC_CHROME_FOG': 100.0},{'RXBC_LAMP': 100.0},{'RXBC_WHITE_MIRROR': 99.97},{'RXBC_3_CHROME_GRILL': 99.95},
{'RXBC_INDC': 99.84},{'RXBC_WHITE_OS_HND': 98.93}]

@app.route('/api/image', methods=['POST'])
def image_detect():
    return jsonify(objects)

@app.route('/api/imageDetect', methods=['POST'])
def lat_res():
    objects =  [{ "RXBC_MT" : 99.0 } ,{ "RXBC_12V_CH" : 99.0 } ]

    result = []
    for obj in objects:
        for val in obj:
            print()
            result.append(val +"~" +str(obj[val]))

    data = {"objectList" : result}
    return jsonify(data)


app.run()