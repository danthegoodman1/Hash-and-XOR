# define alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# asks for input
encrypted_message = input("What is the encrypted message?\n> ")

#decrypt the input
new_message = ''

for i in range(1, 26):
    new_message = ''
    for character in encrypted_message:
        if character in alphabet:
            position = alphabet.find(character)
            new_position = (position - i) % 26
            new_character = alphabet[new_position]
            new_message += new_character
        else:
            new_message += character
    print("\nThe letters have been shifted by {}, and The encrypted contents might be:\n".format(i), new_message)