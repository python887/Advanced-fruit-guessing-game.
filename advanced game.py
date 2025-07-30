import random
import os
import time

animation = [
    "W",
    "WE",
    "WEL",
    "WELC",
    "WELCO",
    "WELCOM",
    "WELCOME",
]
for frame in animation:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame)
    time.sleep(0.5)

while True:
    print("Welcome to fruit guessing game!" )
    while True:
        response = input("Do you want to play? (yes/no): ").strip().lower()
        if response =="yes":
           print("Great! Let's start the game!")
           break
        if response == "no":
            print("Thank you for visiting! Goodbye!")
            exit()
        else:
           print("Hey, type 'yes' or 'no'.")

    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    random_fruit = random.choice(fruits)
    while True:
        guess = input(f"Guess the fruit from the fruits list: {fruits}: ").strip().lower()
        if guess == random_fruit:
            time.sleep(0.5)
            print(f"Congratulations! You guessed it right. The fruit was {random_fruit}.")
            break
        elif guess in fruits:
            time.sleep(0.5)
            print(f"Sorry, you guessed it wrong. The fruit was {random_fruit}.")
            break
        else:
            time.sleep(1)
            print("Hey Hey! you gave wrong input. ")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("Great! Let's play again!")
        
    elif play_again == "no":
        print("Thank you for playing! Goodbye!")
        exit() 
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue       
