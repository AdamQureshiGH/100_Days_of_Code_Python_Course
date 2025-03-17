import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
s = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_characters = nr_numbers + nr_letters + nr_symbols
nr_used_letters = 0
nr_used_symbols = 0
nr_used_numbers = 0
# for i in range(total_characters):
while(len(s) < total_characters):
    num = random.randint(0,2)
    if(num == 0 and nr_used_letters < nr_letters):
        s+= random.choice(letters)
        nr_used_letters += 1
    if (num == 1 and nr_used_symbols < nr_symbols):
        s+= random.choice(symbols)
        nr_used_symbols += 1
    if (num == 2 and nr_used_numbers < nr_numbers):
        s+= random.choice(numbers)
        nr_used_numbers += 1
print(s)
