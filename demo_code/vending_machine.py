# use while command and prompt user to input a coin amount in command, convert coins to float and restart if not convertable through an except in the if command
# use if and elif commands to check if coins are in the denominations 1, 5, 10, 25
# use else command to restart code if coins dont follow correct denominations
# use number and subtract comman to subtract a number from pay variable depending on type of coin, then print variable number in coins due
# repeat code until coins owed <=  0 then multiply number by -1 and print that as change owed with:.0f to remove .0 decimal and break loop 
def main():
    amount_due = 50
    while True:
        try: 
            print(f"Amount Due: {amount_due}")
            coin = float(input("Insert coin:"))
            if coin == 1:
                amount_due -= 1
                if amount_due <= 0:
                    amount_owed = amount_due*-1
                    print(f"change owed: {amount_owed}")
                    break
                else:
                    continue
            elif coin == 5:
                amount_due -= 5
                if amount_due <= 0:
                    amount_owed = amount_due*-1
                    print(f"change owed: {amount_owed}")
                    break
                else:
                    continue
            elif coin == 10:
                amount_due -= 10
                if amount_due <= 0:
                    amount_owed = amount_due*-1
                    print(f"change owed: {amount_owed}")
                    break
                else:
                    continue
            elif coin == 25:
                amount_due -= 25
                if amount_due <= 0:
                    amount_owed = amount_due*-1
                    print(f"change owed: {amount_owed}")
                    break
                else:
                    continue
            else:
                continue
        except:
            continue
            
main()

                

