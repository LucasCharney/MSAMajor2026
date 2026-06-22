import flask
from flask import request,jsonify
#import student_generator_v2 as sg
# create a flask app object
app = flask.Flask(__name__)
# tell the server to reload each time the code changes
app.config["DEBUG"] = True
# create a route for the homepage of the application
# create endpoints for the functions we will create
@app.route('/', methods=['GET'])
def index():
    return "<h1>My name is Lucas Charney</h1>"
# run the application
app.run(debug = True)
