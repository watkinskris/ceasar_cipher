from cipher_art import logo


def cipher(text, shift, direction):
    cipher_text = []
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            cipher_text.append(letter)
        else:
            new_letter_index = alphabet.index(letter) + shift
            cipher_text.append(alphabet[new_letter_index])
    print(f"The {direction}d message is: " + "".join(cipher_text))
    cipher_text.clear()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
another = True

print(logo)
while another:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    cipher(text, shift, direction)

    another_message = input("Type y to enter another message or any other key to exit: ")
    if another_message != "y":
        another = False
