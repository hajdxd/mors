#morse code translator, both ways

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

REV_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "
    return cipher


def decrypt(message):
    decipher = ""
    for code in message.split(' '):
        if code == "":
            decipher += " "
        else:
            decipher += REV_MORSE_CODE_DICT.get(code, " ")
    return decipher


mode_selected = False

while not mode_selected:
    mode = input("\033[33mwelcome to morse code translator\033[0m\n[\033[31m1\033[0m]encrypt\n[\033[34m2\033[0m]decrypt\n")
    if mode == "1":
        mode_selected = True
        message = input("\033[36menter your message:\033[0m ").upper()
        result = encrypt(message).lower()
        print(f"\033[92m{result}\033[0m")

    elif mode == "2":
        mode_selected = True
        message = input("\033[35menter your message:\033[0m ").upper()
        result = decrypt(message).lower()
        print(f"\033[92m{result}\033[0m")

    else:
        print("wrong input")



