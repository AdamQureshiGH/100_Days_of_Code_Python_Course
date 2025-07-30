import random
import hangman_words

word_list = hangman_words.words

secret_word = random.choice(word_list)
solved_characters = []

lives_left = 6
game_finish = False
correct_guess = False
repeated_guess = True

#To display solved characters
for i in secret_word:
    solved_characters.append("_")

while not game_finish:
    correct_guess = False
    print(secret_word)
    print("Current Guess:" + "".join(solved_characters))
    guess = input("Guess a character:\n").lower()
    for i in range(len(secret_word)):
        if guess in "".join(solved_characters):
            repeated_guess = True
        elif guess == secret_word[i]:
            correct_guess = True
            solved_characters[i] = secret_word[i]
    if correct_guess:
        print("Correct Guess!")
        if "".join(solved_characters) == secret_word:
            game_finish = True
            print("******YOU WIN!************")
    elif repeated_guess:
        print("You already guessed that!")
        repeated_guess = False
    else:
        lives_left -= 1
        print("Incorrect Guess :(\n")
        print(f"You have {lives_left} lives left")
        if lives_left == 0:
            game_finish = True
            print(f"*********IT WAS {secret_word}!! You LOSE*******")
    print(hangman_words.HANGMANPICS[6 - lives_left])

#for i in chosen_word:

#flow through all the letters, they guess a letter then you iterate through a loop of the secret word,
#if the char they entered is the same as the current iterated char, then set the string you have at that number to that char
#    squares = [x**2 for x in range(10)]  # squares will be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#have a boolean that ticks true once you go into setting a letter scope so it knows you did not lose a life that round
#compare the lists to see if equal at the end or man is hanged, if not then ask for another letter

#The other way was appending either a _ or letter depending on the condition d: Then when youre checking for guesses, check whether guess is in secret word or the letter iteration that youre on is in the secret word