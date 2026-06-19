class Student():

    def __init__(self, first_name, last_name, major, credit_hours, GPA, id_number):
            #define class properties wi9th the parameter values
            self.__first_name = first_name
            self.__last_name = last_name
            self.__major = major
            self.__credit_hours = credit_hours
            self.__GPA = GPA
            self.__id_number = id_number
            #cretae getter and setter methods for class properties
            
    def get_last_name(self):
        return self.__last_name
    
    def set_first_name(self, new_first_name:str):
                self.__GPA = new_first_name
                return
    
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_first_name:str):
                self.__GPA = new_first_name
                return
    
    def get_major(self):
        return self.__major
    
    def set_major(self, new_major:str):
        self.__GPA = new_major
        return
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours:int):
        self.__credit_hours = new_credit_hours
        return
    
    def get_GPA(self):
        return self.__GPA
    
    def set_GPA(self, new_GPA:int):
        self.__GPA = new_GPA
        return
    
    def get_id_number(self):
        return self.__id_number

    def get_class_level(self):
        if self.__credit_hours<= 30:
            return "Freshman"
        elif self.__credit_hours<= 60:
            return "Sophmore"
        elif self.__credit_hours<= 90:
            return "Junior"
        else:
            return "Senior"
    def update_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours

    def print_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level}, Major: {self.__major}")
        print(f"GPA: {self.__GPA} ID: {self.__id_number}\n")