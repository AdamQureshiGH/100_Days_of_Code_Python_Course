import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to rock paper scissors.\n")
user_hand_input = input("Type 'rock' 'paper' or 'scissors'\n")
user_hand_ascii = ""
if user_hand_input == "rock":
    user_hand_ascii = rock
elif user_hand_input == "paper":
    user_hand_ascii = paper
elif user_hand_input == "scissors":
    user_hand_ascii = scissors
else:
    print("Invalid Input")

enemy_hand = ""
enemy_hand_ascii = ""
enemy_hand_number = random.randint(0,2)
if enemy_hand_number == 0:
    enemy_hand = "rock"
    enemy_hand_ascii = rock
elif enemy_hand_number == 1:
    enemy_hand = "paper"
    enemy_hand_ascii = paper
else:
    enemy_hand = "scissors"
    enemy_hand_ascii = scissors
print("You played:\n" + user_hand_input + user_hand_ascii)
print("Enemy played:\n" + enemy_hand  + enemy_hand_ascii)
if user_hand_input == "scissors":
    if enemy_hand == "scissors":
        print("Tie!")
    elif enemy_hand == "rock":
        print("You lose!")
    elif enemy_hand == "paper":
        print("You win!")
elif user_hand_input == "paper":
    if enemy_hand == "scissors":
        print("You lose!")
    elif enemy_hand == "rock":
        print("You win!")
    elif enemy_hand == "paper":
        print("Tie!")
elif user_hand_input == "rock":
    if enemy_hand == "scissors":
        print("You win!")
    elif enemy_hand == "rock":
        print("Tie!")
    elif enemy_hand == "paper":
        print("You lose!")