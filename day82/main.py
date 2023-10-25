morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

input = input("What do you want to say in Morse Code?\n")
input = input.upper()
def encrypt(text):
    result = ''
    for letter in text:
        result += morse_code[letter] + ' '
    return result
print(encrypt(input))
cipher_text = encrypt(input)
def decrypt(text):
    result = ''
    for letter in text:
        for key, value in morse_code.items():
            if letter == value:
                result += key
    return result
print(decrypt(cipher_text))