
def load_menu_items(filename:str) -> dict:
    #open menu.txt: create file handler to open file in read mode

    data_file = open("menu.txt", "r")
    # create an empty dictionary
    #use a loop to open file line by line
    #get the item and price from the list
    # close the file 
    menu_items = {}
    for line_of_data in data_file:
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        menu_items[item_name] = item_price
    data_file.close()
    return menu_items
def main():
    menu_items = load_menu_items("menu.txt")
    total = 0
    while True:
            order = input("Item:\n").title()
            if order.lower() == "end":
                break
            if order in menu_items:
                total += menu_items[order]
                print(f"Total: ${total:.2f}")
            else:
                continue
            continue
    print(f"Total: ${total:.2f}")
main()