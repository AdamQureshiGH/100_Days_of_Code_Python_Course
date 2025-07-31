import sys
import random
import art

class BlackjackGame:
    def __init__(self):
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        self.start_new_round()

    def start_new_round(self):
        self.player_cards = [random.choice(self.deck)]
        self.dealer_cards = [random.choice(self.deck)]
        self.play_round()

    @property
    def player_total(self):
        return sum(self.player_cards)

    @property
    def dealer_total(self):
        return sum(self.dealer_cards)

    def show_cards(self):
        """Clear screen and show both hands."""
        print("\n" * 100)
        print(art.logo)
        print(f"Dealer cards: {self.dealer_cards} (total: {self.dealer_total})")
        print(f"Your cards:   {self.player_cards} (total: {self.player_total})")

    def player_hit(self):
        self.player_cards.append(random.choice(self.deck))

    def dealer_play(self):
        while self.dealer_total <= 16:
            self.dealer_cards.append(random.choice(self.deck))
            if self.dealer_total > 21:
                self.show_cards()
                print("Dealer busts! You win! 🎉")
                self.ask_replay()

    def final_tally(self):
        self.show_cards()
        if   self.player_total  > 21: print("You busted! You lose. 💥")
        elif self.dealer_total  > 21: print("Dealer busted! You win! 🎉")
        elif self.player_total  > self.dealer_total: print("YOU WIN! 🎉")
        elif self.player_total  < self.dealer_total: print("YOU LOSE! 💔")
        else:                                 print("DRAW! 🤝")
        self.ask_replay()

    def ask_replay(self):
        ans = input("Play again? (y/n) ").strip().lower()
        if ans == "y":
            self.start_new_round()
        elif ans == "n":
            sys.exit()
        else:
            print("Come on, just 'y' or 'n'…")
            self.ask_replay()

    def play_round(self):
        while True:
            self.show_cards()
            choice = input("Hit or Stand? (h/s) ").strip().lower()
            if choice == "h":
                self.player_hit()
                if self.player_total > 21:
                    self.show_cards()
                    print("BUST! 💥")
                    self.ask_replay()
            elif choice == "s":
                self.dealer_play()
                self.final_tally()
            else:
                print("Invalid input — please type 'h' or 's'.")

if __name__ == "__main__":
    BlackjackGame()
