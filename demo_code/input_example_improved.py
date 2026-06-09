#program to convert lbs to kgs
# INPUT (getting the data that will be processed)
# loop
while (True):
    #validat5e input:
# Prompt user to enter weight in lbs
    try:
        user_weight = float(input("Enter weight in lbs: "))
        # check if weight is less than zero 
        # if weight is less than or equal to zero output error message and reprompt user
        if user_weight <= 0:
            print("ERROR: Please enter a number greater than zero.\n")
            continue
        break
    except:
        print("ERROR: Please enter a number.\n")
        continue
    # validate input: ensure the data is a number type 
    # if the input is invalid, then reprompt the user until the input is valid

# PROCESSING
# use a conversion factor to convert lbs to kgs (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT
# print the output
print(f"You weigh {user_weight_in_kg:.2f} kgs.")