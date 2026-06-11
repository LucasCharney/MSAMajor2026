#create a decision structure to determine the season 
# Winter, Spring, Summer, Fall
#Ask the User to enter the number of the month. month must be 1-12
# Output the season
# Enter month number
def main():
    while True:
        try:
            month = int(input("Enter the month of the year"))
            if month == 12 or (month <= 2 and month >= 1):
                print(f"\nThe Season is winter \n")
                break
            elif month >= 9 and month <= 11:
                print(f"\nThe Season is fall \n")
                break
            elif month >= 6 and month <= 8:
                print(f"\nThe Season is summer \n")
                break
            elif month >= 3 and month <= 5:
                print(f"\nThe Season is spring \n")
                break
            else:
                print(f"Please enter a valid input")
                continue
        except:
            print(f"Please enter a valid input")
            continue
main()





































































