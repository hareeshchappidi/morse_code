MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.'
}


def encrypt(text):
    encrypted_text = ""
    for letter in text:
        if letter != " ":
            encrypted_text = encrypted_text + MORSE_CODE_DICT.get(letter) + " "
        else:
            encrypted_text += " "
    print(f'Encrypted text : {encrypted_text}')


def decrypt(text):
    text += " "
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    morse_coded_text = ""
    decrypted_text = ""
    space_found = 0
    for letter in text:
        if letter != " ":
            morse_coded_text += letter
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                decrypted_text += " "
            else:
                decrypted_text = decrypted_text + key_list[val_list.index(morse_coded_text)]
                morse_coded_text = ""
    print(f'Decrypted text : {decrypted_text}')


choice = input('Enter E to Encrypt or D to Decrypt: ')
if choice.upper() == 'E':
    text_to_encrypt = input("Enter some Text To Encrypt : ").upper()
    encrypt(text_to_encrypt)
elif choice.upper() == 'D':
    text_to_decrypt = input("Enter morse code to Decrypt : ")
    decrypt(text_to_decrypt)
else:
    print('Invalid option!')
