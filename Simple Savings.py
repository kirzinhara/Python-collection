
money = 0
def add():
    global money
    try:
        add_money = input("Deposit Balance Here:")
        add_money = int(add_money)
        if add_money < 0:
            print("Sorry we can't proceed to your transaction")
        else:
            money += add_money
    except ValueError:
        print("Invalid input")
    

def sub():
    global money
    sub_money = input("withdraw balance here:")
    sub_money = int(sub_money)
    if money < sub_money:
        print("Sorry we can't proceed to your transaction")
    else:
        money -= sub_money

while True:
    print("========================================")
    print("|Welcome to Online Transaction Savings...")
    print(f"|Your Balance:{money}"                    )
    print("| 1. Deposit Balance                    |")
    print("| 2. Withdraw Balance                   |")
    print("========================================")
    pick_transact = input("What would you like to do ?")
    if pick_transact == '1':
        add()
    if pick_transact == '2':
        sub()
    else:
        print("Press the appropriate number")



    print("Remaining Balance : ",money)
    choice = input("Do you want to transact again? y/n :")
    if choice != 'y':
        print("bye")
        break



