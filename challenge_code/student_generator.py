from Student import Student

def load_menu_items(str) -> list:
    #open menu.txt: create file handler to open file in read mode

    data_file = open("students.csv", "r")
    # create an empty dictionary
    #use a loop to open file line by line
    #get the item and price from the list
    # close the file 
    menu_items = {}
    for line_of_data in data_file:
        student = line_of_data.split(",")
        
    data_file.close()
load_menu_items(str)