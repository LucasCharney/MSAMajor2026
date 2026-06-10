# program to get hourly wage and give pay advice

def get_hours_input():
    #loop
    while (True):
    # get inputs and validate as working types
    #convert inputs to float 
        try: 
             # prompt user to enter hourly wage and hours worked
            hours_worked = float(input("Enter the hours worked: "))
             # if input is negative ouytput error message and break
            
            if (hours_worked > 24) or (hours_worked <= 0):
                print("ERROR: Invalid Input. Please Try Again \n")
                continue
            break
        except:
            print("ERROR: Invalid Input. Please Try Again \n")
            continue
    return hours_worked
def get_wage_input():
    #loop
    while (True):
    # get inputs and validate as working types
    #convert inputs to float 
        try: 
             # prompt user to enter hourly wage and hours worked
            hourly_wage = float(input("Enter the hourly wage: "))
             # if input is negative ouytput error message and break
            
            if (hourly_wage > 200) or (hourly_wage <= 0):
                print("ERROR: Invalid Input. Please Try Again \n")
                continue
            break
        except:
            print("ERROR: Invalid Input. Please Try Again \n")
            continue
    return hourly_wage
    
def main():
    hours_worked= get_hours_input()
    hourly_wage = get_wage_input()
    wages_before_taxes = hourly_wage*hours_worked*350 
    taxes = 0.12
    tax_multiplier = (1-taxes) 
    annual_wage_after_taxes = wages_before_taxes*tax_multiplier
    tax_amount = wages_before_taxes - annual_wage_after_taxes
    print(f"\nPAY ADVICE: \n------------- \nHours_worked: {hours_worked:.2f} \nHourly Wage: ${hourly_wage:.2f} \nWages Before Taxes ${wages_before_taxes:.2f}\nTax Amount ${tax_amount:.2f} \nAnnual Wage After Taxes ${annual_wage_after_taxes:.2f}")
main()
