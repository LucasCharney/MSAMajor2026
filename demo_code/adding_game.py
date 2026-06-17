import random
def get_level():
    while True:
        try: 
            difficulty = int(input("Enter Level 1, 2, 3:"))
            if not (0 < difficulty < 4):
                print(f"invalid input!")
                continue
            while True:
                try:
                    questions = int(input("\nEnter number of questions to ask: 3 to 10: "))
                    if not (2 < questions < 11):
                        print(f"Please enter an integer value from 3 to 10!")
                        continue
                    break
                except:
                    print(f"Please enter an integer value from 3 to 10!")
                    continue
        except:
             print(f"invalid input!")
             continue
        return difficulty, questions
    
def main():
    difficulty, questions = get_level()
    random_generator = random.Random()
    incorrect_answers = 0
    correct_answers = 0

    while True:
        incorrect_attempts = 0
        if difficulty == 1:
            random_number_1 = random_generator.randint(0,9)
            random_number_2 = random_generator.randint(0,9)
        elif difficulty == 2:
            random_number_1 = random_generator.randint(10,99)
            random_number_2 = random_generator.randint(10,99)
        elif difficulty == 3:
            random_number_1 = random_generator.randint(100,999)
            random_number_2 = random_generator.randint(100,999)
        answer = random_number_1 + random_number_2
        
        
        while True:
            try:
                response = int(input(f"{random_number_1} + {random_number_2} = "))
            except:
                print( f"WRONG!!!")
                incorrect_attempts += 1
                if incorrect_attempts == 3:
                    print(f"\nCorrect Answer = {random_number_1} + {random_number_2} = {answer}\n")
                    incorrect_answers += 1
                    break
                continue
            if answer != response:
                print( f"WRONG!!!")
                incorrect_attempts += 1
                if incorrect_attempts == 3:
                    print(f"\nCorrect Answer = {random_number_1} + {random_number_2} = {answer}\n")
                    incorrect_answers += 1
                    break
                continue
            print(f"CORRECT!!!")
            correct_answers += 1
            break
        questions -= 1
        if questions == 0:
            percentage = (correct_answers / (correct_answers + incorrect_answers))*100
            print(f"You got {correct_answers} out of {correct_answers + incorrect_answers} correct: {percentage:.2f}%")
            break
        else: 
            continue
main()