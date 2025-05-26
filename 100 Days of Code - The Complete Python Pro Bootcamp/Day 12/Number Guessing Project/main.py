import art
import random
print(art.logo)

secret_number = random.randint(0, 100)
print("Im thinking of an integer between 1 and 100\n")
def choose_difficulty():
    difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
       return 10
    elif difficulty == "hard":
       return 5
    else:
        choose_difficulty()

attempts = choose_difficulty()
for i in range(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > secret_number:
        print("Too high!")
        attempts -= 1
    elif guess < secret_number:
        print("Too low!")
        attempts -= 1
    else:
        print("You win!")
        break
