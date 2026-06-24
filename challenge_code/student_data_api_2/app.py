import flask
from flask import request,jsonify
import student_generator_v2 as sg
# create a flask app object
app = flask.Flask(__name__)
# tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
function to querry the list of student dictionaries based on a search key and a value
input: search_key - key in the dictionary we watnt to check the value of
    search_value the item of the key we need to match
output: list of student dictionaries that mathc the search criteria
"""
# create a route/view for the homepage of the application
# create endpoints for the functions we will create
def search_dictionary_list(search_key, search_value):
    student_list = []
    for student in sg.get_student_dictionaries():
        if student[search_key].lower() == search_value.lower():
            student_list.append(student)
    return student_list


@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

#cretae a route  to return all student data 
@app.route('/api/students/all', methods = ['GET'])
def api_all():
    #get student sictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

@app.route('/api/major/<string:major>', methods =['GET'])
def api_students_by_major(major:str):
    # call the search function to get students with this major
    major_students = search_dictionary_list("major",major)
    return jsonify(major_students)

@app.route('/api/class/<string:student_class>', methods = ['GET'])
def api_students_by_class(student_class:str):
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)
     
@app.route('/api/student/id/<string:id>', methods=['GET'])
def api_get_students_by_id(id:str):
    id = search_dictionary_list("class", id)
    return jsonify(id)



app.run(debug = True)
