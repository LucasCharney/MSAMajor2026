from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url:str):
    #make a request
    #convert the format to json
    #return the response
    response = requests.get(url)
    response_json = response.json()
    return response_json
@app.route('/', methods=['GET'])
def index():
    url = "http://127.0.0.1:5000/api/students/all"
    student_data = get_student_data(url)
    return render_template('index.html', student_data=student_data)
#run the flask app
@app.route('/majors', methods=['GET'])
def majors_get():
    url = "http://127.0.0.1:5000/api/majors/all"
    major_list = get_student_data(url)
    return render_template('majors.html', major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():
    url = "http://127.0.0.1:5000/api/majors/all"
    #get the list of majors
    major_list = get_student_data(url)
    #get the form data
    major = request.form.get('major')

    if major == "":
        flash("ERROR: You must select a major")
        return redirect(url_for('majors_get'))
    # create a url to get students from that major
    url = f"http://127.0.0.1:5000/api/major/{major}"
    # get the response after sending it
    result_list = get_student_data(url)
    #send all the data to the majors template to be displayed in the browser
    return render_template('majors.html', major_list =major_list, result_list=result_list, major=major)
app.run(port=5001)
