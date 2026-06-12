def main():
        my_name = "lucas"
        my_name_title_case = "Lucas"
        my_last_name = "CHARNEY"
        # capitalize a string
        print(f"My name capitalized: {my_name.capitalize()}")
        print(f"My name uppercased: {my_name.upper()}")
        print(f"My full name lowercased: {my_name.lower()} {my_last_name.lower()}")
        if my_name.lower() == my_name_title_case.lower():
                print(f"The strings are equal")
        else:
                print(f"The strings are not equal")
        print(f"\nUsing the Startswith() Method\n-------------")
        print(f"My name starts with L or l: {my_name.startswith("L") or my_name.startswith("l")}")

        if(not my_name.startswith("Luca") and (not my_name.startswith("luca"))):
                print(f" You spelled my name incorrectly")
        else:
                print(f" You spelled my name correctly")
        if(not my_name.lower().startswith("luca")):
                print(f" You spelled my name incorrectly")
        else:
                print(f" You spelled my name correctly")
        print(f"{my_name} ends with cas': {my_name.endswith('cas')}")
        print(f"\nUsing the Find() Method\n--------------")
        search_letter = "a"
        index_of_substring = my_name.find(search_letter)
        if index_of_substring != -1:
                print(f"The '{search_letter}' is at index {index_of_substring} in {my_name}")
        print("\nLooping through a string")
        for letter in my_name:
                print(letter)
        print(f"{my_name} has {len(my_name)} letters")
        for letter_index in range(len(my_name)):
                print(f"Letter {letter_index}: {my_name[letter_index]}")
        print("\nSearch a string")
        sentence = "I have a cat. My cat is cute. Do you want a cat?"
        #write code that counts the number of occurences of the word dog in the sentence
        #expected output: 3
        search_word = "cat"
        start_index = 0
        number_of_cats = 0
        while True:
                # start at the4 beggining of the string
                # search for the occurence of the word cat at index 0
                cat_index = sentence.find(search_word, start_index)

                # if we find cat add 1 to some v variable we use to keep track of thre cats we find
                # continue searchiong the stirng for thew next index after the cat we just found 
                # update the starting index by 1
                if cat_index == -1:
                        break
                else:
                        number_of_cats += 1
                        start_index = cat_index + 1

                # do this until we dont find any more cats: when find() returns -1
        print(f"There are {number_of_cats} {search_word}s in the sentence")
main() 
