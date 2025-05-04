import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
game_over = True


def caesar(original_text, shift_amount, direction):

    cipher_text = ""
    if (direction == "encode"):
        shift_amount * 1
    elif (direction == "decode"):
        shift_amount *= -1
    else:
        print("Choose encode or decode")

    for letter in original_text:
        if(not letter.isalpha()):
            cipher_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Text: {cipher_text}")

while(game_over == True):
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, type 'stop' to terminate the program:\n").lower()
    if (direction == "stop"):
        game_over = False
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(not shift.is_integer()):
        print("Invalid Input")
        break
    caesar(text, shift, direction)


