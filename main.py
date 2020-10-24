import random

import pyperclip


def password_generator(pcharacters="default", plength=16):
    if pcharacters == "default":
        print("An error has occurred")
    else:
        pswd = "".join(random.sample(pcharacters, plength))
        return pswd


lower = "abcdefghijklmnoprstuvwxyz"
upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
numbers = "123456789"
symbols = str("[]{}!$()-")

pswd_char = lower + upper + numbers + symbols
pswd_length = int(input("How long do you want the password to be? "))

selection = ' '

password = password_generator(pcharacters=pswd_char, plength=pswd_length)
print('Password: ', password, end="\n\n")

while selection != 'E':

    print('Please select from the following choices: ')
    print("\033[1m" + '(C)' + "\033[0m" + 'opy password to clipboard')
    print("\033[1m" + '(G)' + "\033[0m" + 'enerate a new password')
    print("\033[1m" + '(E)' + "\033[0m" + 'xit \n\n')
    selection = input('What do you want to do? ')

    if selection == "C":
        pyperclip.copy(password)
        print('Password copied to clipboard \n\n')
    elif selection == "G":
        print('Generating a new password \n\n')
        password = password_generator(pcharacters=pswd_char, plength=pswd_length)
        print('Password: ', password, end="\n\n")
    else:
        break

