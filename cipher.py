def encode_message(text, shift):
    encoded_message = []
    for letter in text:
        if letter not in alphabet:
            encoded_message.append(letter)
        else:
            new_letter_index = alphabet.index(letter) + shift
            if new_letter_index > 25:
                new_letter_index = new_letter_index - 26
            encoded_message.append(alphabet[new_letter_index])
    print("The encoded message is: " + "".join(encoded_message))


def decode_message(text, shift):
    decoded_message = []
    for letter in text:
        if letter not in alphabet:
            decoded_message.append(letter)
        else:
            new_letter_index = alphabet.index(letter) - shift
            if new_letter_index < 0:
                new_letter_index = 26 + new_letter_index
            decoded_message.append(alphabet[new_letter_index])
    print("The decoded message is: " + "".join(decoded_message))



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
another = True

while another:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode_message(text, shift)
    else:
        decode_message(text, shift)

    another_message = input("Type y to enter another message or any other key to exit: ")
    if another_message != "y":
        another = False
    else:
        encoded_message.clear()
        decoded_message.clear()
