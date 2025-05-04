# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
other_bidders = ""
print("\n" * 100)
print(art.logo)
dict = {}
def auction(dict):
    highest_bidder = ""
    highest_value = 0
    while (True):
        if (input("Are there any other bidders? (yes/no)\n").lower() == "no"):
            break
        Key = input("Name:\n")
        Value = input("Amount to bid:\n")
        dict[Key] = Value

    for key in dict:
        if (float(dict[key]) > highest_value):
            highest_value = float(dict[key])
            highest_bidder = key

    print(f"The winner is {highest_bidder}, with a bid of ${highest_value}")

auction(dict)