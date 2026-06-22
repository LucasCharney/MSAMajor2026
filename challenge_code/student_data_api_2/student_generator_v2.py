from student_data_api.Student import Student

def load_items(filename:str) -> list:
    #open menu.txt: create file handler to open file in read mode
    kids = []
    data_file = open(filename, "r")
    # create an empty dictionary
    #use a loop to open file line by line
    #get the item and price from the list
    # close the file 
    for line_of_data in data_file:
        student = line_of_data.split(",")
        try:
            if len(student) !=6:
                raise Exception(f"Error on line {line_of_data} of the file. data has {len(student)} items, but should have 6")
        except:
            continue
        try:
            information=Student(student[0],student[1],student[2],int(student[3]),float(student[4]),int(student[5])) 
        except:
            continue
        kids += [information]
    data_file.close()
    return kids
def main():
    kids = load_items("students.csv")
    for people in kids:
        people.print_data()
main()


