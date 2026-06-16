def main():
    scores = [55, 75, 87, 82, 91]
    students = ["alice", "bob", "jerry", "jane", "bill"]
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")
    # create a dictionary of names and scores
    student_scores = {
    "alice": 55,
    "bob": 75,
    "jerry": 87,
    "jane": 82,
    "bill": 91
    }
    print(f"\nPrint bob and janes scores\n------------")
    print(student_scores["bob"])
    print(student_scores["jane"])
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")
    #create a dictionary to store car information
    car_1 = {"make": "Ferrari", "model": "F-50", "year": "2024", "value": 500000, "engine": 4.8}
    for key, value in car_1.items():
        print(f"{key}: {value}")
    car_2 = {"make": "Honda", "model": "Accord", "year": 2024, "value": 18000, "engine": 2.4}
    dictionary_list = [car_1, car_2]
    print(f"\nDisplay information for all cars\n------------")
    #create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}
    # print all car information from the dictionary
    print("\nCar info from dictionaries\n--------------")
    for make, car in car_dictionary.items():
        print(f"\n{make}")
        for feature, value in car.items():
            print(f"{feature}: {value}")
    key = "Transmission"
    if key not in car_1.keys():
        print(f"ERROR : KEY '{key}' does not exist in the dictionary")
    else:
        print(f"{car_1[key]}")












    
main()