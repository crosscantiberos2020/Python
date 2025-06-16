import random

print("Welcome to Guess the Number Game 🎮")

c_number = random.randint(1,10)
print("Computer Number is X. Now, You Have To Guess The Number.")

user_number = int(input("Enter Your Number[3] Chances Left]: "))

chances = 5

while True :
    user_number = int(input(f"Try Again! {chances} Chance Left. Enter Your Number: "))
    chances = chances - 1

    if c_number > user_number :
        print("Try Higher Number.")
    elif c_number < user_number:
        print("Try Lower Number.")

    if chances == 0:
        print("Sorry! You Lost.")
        break

    if user_number == c_number:
      print("Hurray! You Won the Game 🏆")
      break
    else:
        continue


