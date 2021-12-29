from Products import Products
import os.path
import platform
# Stores the value in balance.txt in current_balance (also rounds it to 2)
def Get_Current_Balance():
    get_current_balance = open('balance.txt')
    current_balance = round(float(get_current_balance.read()), 2)
    get_current_balance.close()
    return current_balance

# adds to or substracts a value from the value stored in balance.txt
def Set_Current_Balance(balance, add_to_balance):
    balance += add_to_balance
    set_current_balance = open('balance.txt', 'w')
    set_current_balance.write(str(balance))
    set_current_balance.close()

def Clear_Console():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        os.system('cls')

# Main Program
def main():
    # Checks if the file exists and create a new one if it doesn't exist
    if os.path.exists('balance.txt') is False:
        Set_Current_Balance(0, 0)
        main()
    else:
        # Checks if the file is empty to prevent any possible errors
        size_checking = os.path.getsize('balance.txt')
        if size_checking == 0:
            Set_Current_Balance(0,0)
            Clear_Console()
            main()
        print(f"Your current balance is: £{Get_Current_Balance()}")
        pay_or_choose = input("press 0 to input money, or 1 to select and buy product\n")

        if pay_or_choose == '0':
            amount_inputted = input("Enter the amount you'd like to input:\n £")
            # Input sanitization - not sure if this is the best and most efficient way or not?
            try:
                amount_inputted = float(amount_inputted)
            except ValueError:
                Clear_Console()
                print("input a number, not a letter")
                main()
            Set_Current_Balance(Get_Current_Balance(), amount_inputted)
            main()
        elif pay_or_choose == '1':
            # List containing products values, all stored as an object of the Product class
            product_list = [
                Products("Logan", 1, 0),
                Products("Snickers", 1, 1, ),
                Products("Mars Bar", 1.50, 2),
                Products("Galaxy Bar", 1.75, 3)
            ]
            # Loops through the list and prints the objects
            for product in product_list:
                print(f"{product.product_name} : £{product.displayed_price} :  {product.product_number}")
            user_input = input("input a number: ")
            try:
                user_input = int(user_input)
            except ValueError:
                Clear_Console()
                print("input a number, not a letter")
                main()
            # Checks if inputted value is too big or too small
            if user_input > len(product_list) - 1 or user_input < 0:
                Clear_Console()
                print("don't input an invalid number - try again")
                main()
            selected_product = product_list[user_input]
            if Get_Current_Balance() >= selected_product.displayed_price:
                Set_Current_Balance(Get_Current_Balance() - selected_product.displayed_price, 0)
                Clear_Console()
                print(f"Successful Purchase, your new balance is £{Get_Current_Balance()}")
                main()

            else:
                Clear_Console()
                print("insufficient funds.")
                main()
        else:
            Clear_Console()
            main()

if __name__ == "__main__":
    main()
else:
    raise Exception("You must not import this standalone application")