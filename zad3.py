alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(message, key, alphabet=alphabet):
    message = message.lower()
    letters_only = ''.join(filter(str.isalpha, message))


    if key > len(alphabet):
        key = key % len(alphabet)
    #print(key)
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    shifted_letters = ''
    for letter in letters_only:
        if letter.isupper():
            shifted_letters += shifted_alphabet[alphabet.index(letter.lower())].upper()
        else:
            shifted_letters += shifted_alphabet[alphabet.index(letter)]

    output = ''
    index = 0
    for char in message:
        if char.isalpha():
            output += shifted_letters[index]
            index += 1
        else:
            output += char

    return output


data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
enc = caesar_cipher(data, 50)
print(enc)


