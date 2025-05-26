import sys

import art
import random


def final_tally(player_total, dealer_total, player_cards, dealer_cards):
    if player_total < dealer_total:
        show_cards(player_cards, dealer_cards)
        print("YOU LOSE!\n")
        end_game()

    elif (player_total == dealer_total):
        show_cards(player_cards, dealer_cards)
        print("DRAW!\n")
        end_game()

    else:
        show_cards(player_cards, dealer_cards)
        print("YOU WIN!\n")
        end_game()

def player_hit(player_cards, dealer_cards, cards):
    player_cards.append(random.choice(cards))
def dealer_hit(dealer_cards, cards):
    dealer_cards.append(random.choice(cards))
def dealer_final(player_total, dealer_total, dealer_cards, cards, player_cards):
    while (dealer_total <= 16):
        dealer_hit(dealer_cards, cards)
        player_total, dealer_total = check_totals(player_cards, dealer_cards, player_total, dealer_total,)
        if (dealer_total > 21):
            show_cards(player_cards, dealer_cards)
            print("Dealer Busts! You Win!")
            sys.exit(0)
def end_game():
    play_again = input("Would you like to play again? ( y / n )?\n")
    if play_again.lower() == "y":
        sys.exit()
    elif play_again.lower() == "n":
        sys.exit()
    else:
        end_game()
def show_cards(player_cards, dealer_cards):
    print("\n" * 100)
    print(art.logo)
    print(f"Dealer cards: {dealer_cards}")
    print(f"Your cards: {player_cards}")
def check_totals(player_cards, dealer_cards, player_total, dealer_total):
    player_total = 0
    dealer_total = 0
    for num in player_cards:
        player_total += num
    for num in dealer_cards:
        dealer_total += num
    return player_total, dealer_total
def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    player_total = 0
    dealer_total = 0


    while (True):
        show_cards(player_cards, dealer_cards)
        choice = input("Hit or Stand? ( h / s )\n")
        if (choice.lower() == "h"):
            player_hit(player_cards, dealer_cards, cards)
            player_total, dealer_total = check_totals(player_cards, dealer_cards, player_total, dealer_total)
            if player_total > 21:
                show_cards(player_cards, dealer_cards)
                print("BUST")
                end_game()
        elif (choice.lower() == "s"):
            dealer_final(player_total, dealer_total, dealer_cards, cards, player_cards)
            player_total, dealer_total = check_totals(player_cards, dealer_cards, player_total, dealer_total)

            final_tally(player_total, dealer_total, player_cards, dealer_cards)
        else:
            print("Invalid input bro")


play_game()

