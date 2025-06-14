Teriyaki_Chicken = 10
Cheeseburger = 7
Pizza = 5
Fries = 3
Soda = 1

Bill = 0

while True:
    print("Welcome to Cross's Food Zone")
    choice = input("1.Teriyaki Chicken(10)\n2.Cheeseburger(7)\n3.Pizza(5)\n4.Fries(3)\n5.Soda(1)Please Choose your Order: ")
    if choice == "1" :
        print("Your Order - Teriyaki Chicken")
        Bill = Bill+10
        next = input("Would you like to add more to your order?(Yes-1/No-0)")
        if next == "1":
            continue
        elif next == "0":
            break
    elif choice == "2" :
        print("Your Order - Cheeseburger")
        Bill = Bill+7
        next = input("Would you like to add more to your order?(Yes-1/No-0)")
        if next == "1":
            continue
        elif next == "0":
            break
    elif choice == "3" :
        print("Your Order - Pizza")
        Bill = Bill+5
        next = input("Would you like to add more to your order?(Yes-1/No-0)")
        if next == "1":
            continue
        elif next == "0":
            break
    elif choice == "4" :
        print("Your Order - Fries")
        Bill = Bill+3
        next = input("Would you like to add more to your order?(Yes-1/No-0)")
        if next == "1":
            continue
        elif next == "0":
            break
    elif choice == "5" :
        print("Your Order - Soda")
        Bill = Bill+1
        next = input("Would you like to add more to your order?(Yes-1/No-0)")
        if next == "1":
            continue
        elif next == "0":
            break

    else:
        print("Invalid Entry")
        continue

print("Thank You! Your Total Bill - ",Bill)
        