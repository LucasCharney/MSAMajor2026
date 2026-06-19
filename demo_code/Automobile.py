import datetime
class Automobile():
    #define a constructor
    #the constructor is a function that is called in order to create a automobile
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        #define class properties wi9th the parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
        self.__color = color
        #cretae getter and setter methods for class properties
        
        def get_model(self):
            return self.__model
        
        def get_make(self):
            return self.__make
        
        def get_vin(self):
            return self.__vin
        
        def get_engine_size(self):
            return self.__engine_size
        
        def set_engine_size(self, new_size:float):
            self.__engine_size = new_size
            return
        
        def get_owner(self):
            return self.__owner
        
        def set_owner(self, new_owner:str):
            self.__owner = new_owner
            return
        
        def get_year(self):
            return self.__year
        
        def get_color(self):
            return self.__color
        
        def set_color(self, new_color:str):
            self.__color = new_color
            return
        # create a method to print automobile data
    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}. Engine size: {self.__engine_size}")
        print(f"Owner: {self.__owner} Year: {self.__year} Color: {self.__color}")
    #create a method to get an automobiles age 
    def get_age(self):
        the_date = datetime.datetime.now()
        this_year = the_date.year
        return this_year - self.year