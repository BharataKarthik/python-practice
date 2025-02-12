import random

choices = ["Rock","Paper","Scissors"]

user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice not in [0,1,2]:
    print("Invalid Entry, you lose! 😢")
    exit()

computer_choice = random.randint(0,2)

print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

if user_choice == computer_choice:
    print("Its a Tie! 🤝")

elif (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
    print("You win! 🎉")

else:
    print("You Lose! 😢")
