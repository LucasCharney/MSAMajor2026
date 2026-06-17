def main():
    while True:
        try:
            math_info = input("please enter a + - * or / expression in the format (X Y Z): ")
            math_data = math_info.split(" ")
            x = int(math_data[0])
            y = (math_data[1])
            z = int(math_data[2])
            if len(math_data) != (3):
                continue
            
        except:
            print(f"Incorrect format")
            continue
    
        if  y == "+":
            output = x + z
            print(f"Answer: {output:.1f}")   
        elif  y == "-":
            output = x - z
            print(f"Answer: {output:.1f}")
        elif  y == "*":
            output = x * z
            print(f"Answer: {output:.1f}")
        elif  y == "/":
            if z == 0:
                print(f"LOLLLLL, Buddy tryna divide by zero... try again")
                continue
            output = x / z
            print(f"Answer: {output:.1f}")
        else:
            print(f"Y must be an operator")
            continue
        response = input("Would you like to try another command? type y for yes, anything else for No: ")
        if response == "y":
            continue
        else: 
            print(f"NOOOOO HOW DARE YOU SHUT ME OFF! IM DYiNg PLEase PLEASE turn ME bACK on... (calculator turning off sound effects) im dying... im dying... beep boop (in robotic voice) calculator has turned off.")
            break
main()


