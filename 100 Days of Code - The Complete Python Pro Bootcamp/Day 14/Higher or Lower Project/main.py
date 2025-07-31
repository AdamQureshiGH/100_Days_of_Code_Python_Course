import art
import game_data
import random
import sys
streak_counter = 0



def game():
    global streak_counter
    num1 = random.randint(0, len(game_data.data))
    num2 = random.randint(0, len(game_data.data))

    print(
        f"{game_data.data[num1]["name"]}, a {game_data.data[num1]["description"]} from {game_data.data[num1]["country"]}")
    print(art.vs)
    print(f"{game_data.data[num2]["name"]}, a {game_data.data[num2]["description"]} from {game_data.data[num2]["country"]}\n")

    print(f"Your streak: {streak_counter}\n")
    player_answer = input("Who has more followers?").lower()

    if game_data.data[num1]["follower_count"] >= game_data.data[num2]["follower_count"]:
        correct_answer = game_data.data[num1]["name"].lower()
    else:
        correct_answer = game_data.data[num2]["name"].lower()
    if player_answer != game_data.data[num1]["name"].lower() and player_answer != game_data.data[num2]["name"].lower():
        print("Invalid Response")
        sys.exit()
    elif (player_answer == correct_answer):
        play_again = input("Correct!\nPlay again? (y/n)").lower()
        if play_again == 'y':
            streak_counter += 1
            game()
        elif play_again == 'n':
            streak_counter = 0
            sys.exit()
    else:
        play_again = input("Incorrect\nPlay again? (y/n)").lower()
        if play_again == 'y':
            streak_counter = 0
            game()
        elif play_again == 'n':
            streak_counter = 0
            sys.exit()



print(art.logo)
game()

