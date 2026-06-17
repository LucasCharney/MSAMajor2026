def main():
    #open menu.txt: create file handler to open file in read mode
    data_file = open("menu.txt", "r")
    print(data_file)
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
    for items, price in menu_items.items():
        print(f"{items}: ${price}")

main()