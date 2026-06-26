
from Student import Student
from datetime import datetime

def write_to_error_log(message:str) -> None:
    the_date = datetime.now()
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{the_date}: {message}\n")

    return

def load_students(filename:str) -> list[Student]:
    #open menu.txt: create file handler to open file in read mode
    kids = []
    data_file = open(filename, "r")
    # create an empty dictionary
    #use a loop to open file line by line
    #get the item and price from the list
    # close the file 
    line_number = 0
    for line_of_data in data_file:
        student = line_of_data.split(",")
        line_number +=1
        try:
            if len(student) !=6:
                write_to_error_log(f"Error on line {line_number} of the file. data has {len(student)} items, but should have 6.")
                raise Exception(f"Error on line {line_number} of the file. data has {len(student)} items, but should have 6\n")
        except Exception as error:
            continue
        try:
            information=Student(student[0],student[1],student[2],int(student[3]),float(student[4]),int(student[5])) 
        except:
            write_to_error_log(f"Error on line {line_of_data} of the file. Incorrect data types")
            continue
        kids += [information]
    data_file.close()
    return kids

"""
Function to convert student objects into student dictionaries
inputL:list of student objects
output:list of student dictionaries
"""
def student_to_dictionaries(list_of_students: list[Student]) -> list[dict]:
    student_dictionary_list = []
    for student in list_of_students:
        student_dictionary = {}
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_GPA()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()
        student_dictionary_list.append(student_dictionary)
    return student_dictionary_list

"""
function to get student dictionaries
input: none
output: a list of student dictionaries
"""
def get_student_dictionaries():
    # get a list of students
    student_list = load_students("students.csv")
    dictionary = student_to_dictionaries(student_list)
    return dictionary
