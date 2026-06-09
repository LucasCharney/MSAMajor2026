# Print Hello World
print("Hello World")

#create a variable to store my name
first_name= "Lucas"

# create a variable for the last name
last_name = "Charney"
"my fullname is firstname lastname"
print("My Full name is", first_name, last_name, sep="") 

#print using thew f string
print(f"My full name is {first_name} {last_name}.")

# create variables to store age and weight
age = 16
weight = 115.8
half_age = age / 2

# print a sentence with name, age and weight
print(f"My name is {first_name} {last_name}. \nI am {age} years old and I weigh {weight} lbs ")

#get and print the data type for age, weight, half age
print("\nChecking Data Types\n---------------------------")
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 statements using string interpolation (f string) to 
#print descriptive sentences for the data types
# "Variable age is an int"
print(f"variable age is an {type(age)}")
print(f"variable weight is an {type(weight )}")
print(f"variable half_age is an {type(half_age)}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2 
print(f"Total: {total}")
# write a python statement to display
