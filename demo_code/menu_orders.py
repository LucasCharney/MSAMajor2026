# create menu dictionary to store items
#create while loop to reprompt items
# ask for input and check if input is valid using if command to check if input is a valid key word, and continue without an error message 
def main():
    total = 0
    while True:
            menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
            order = input("Item:\n").title()
            if order.lower() == "end":
                break
            if order in menu:
                total += menu[order]
                print(f"Total: ${total:.2f}")
            else:
                continue
            continue
    print(f"Total: ${total:.2f}")
main()
