from Automobile import Automobile

def main():
    #create instyances of automobiles
    #change some properties of automobile
    #create a list of automobiles
    #print all of autmobile data
    auto1 = Automobile("Honda", "Accord", "23456", 2.4, "Alice", 2024, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")
    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)
    for auto in auto_list:
        auto.print_data()
        print(f" Auto1 is {auto1.get_age()} years old")

main()