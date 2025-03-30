import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'


stop_word = None
while stop_word not in ['no', 'n', 'nope', 'nah']:
    print()
    print('Welcome to the Password Generator!')
    print()
    print('==================================================')

    c1 = int(input('Enter the number of passwords to generate: '))
    c2 = int(input('Enter the password length (number of characters): '))
    c3 = input('Should the password contain the numbers 0123456789? ').lower().strip()
    c4 = input('Should the password contain uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? ').lower().strip()
    c5 = input('Should the password contain lowercase letters abcdefghijklmnopqrstuvwxyz? ').lower().strip()
    c6 = input('Should the password contain the characters !#$%&*+-=?@^_? ').lower().strip()
    c7 = input('Do you want to save passwords to a file? (Yes/No): ').lower().strip()

    l = []
    if c3 in ['yes', 'y', 'ye', 'yeah', 'yep', 'yup']:
        l.append(digits)
    if c4 in ['yes', 'y', 'ye', 'yeah', 'yep', 'yup']:
        l.append(uppercase_letters)
    if c5 in ['yes', 'y', 'ye', 'yeah', 'yep', 'yup']:
        l.append(lowercase_letters)
    if c6 in ['yes', 'y', 'ye', 'yeah', 'yep', 'yup']:
        l.append(symbols)

    if len(l) > 0:
        def generate_password(length: int) -> None:
            print()
            print('==================================================')
            print(f'Generated passwords: {c1}')
            passwords_list = []
            for i in range(c1):
                password = ''
                for j in range(length):
                    m = random.choice(l)
                    if m == '0123456789':
                        password += digits[random.randint(0, len(digits) - 1)]
                    elif m == 'abcdefghijklmnopqrstuvwxyz':
                        password += lowercase_letters[random.randint(0, len(lowercase_letters) - 1)]
                    elif m == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        password += uppercase_letters[random.randint(0, len(uppercase_letters) - 1)]
                    elif m == '!#$%&*+-=?@^_':
                        password += symbols[random.randint(0, len(symbols) - 1)]
                passwords_list.append(password)
                print(password)
            if c7 in ['yes', 'y', 'ye', 'yeah', 'yep', 'yup']:
                with open("passwords.txt", "w") as file:
                    file.write("\n".join(passwords_list))
                print()
                print("Passwords have been saved to passwords.txt")
                
        generate_password(c2)
        print()
        print('==================================================')
        stop_word = input('Generate passwords again? (Yes/No) ').lower().strip()
        print('==================================================')
    else:
        print()
        print('==================================================')
        print(f'A password must contain at least one type of character')
        stop_word = input('Generate passwords again? (Yes/No) ').lower().strip()
        print('==================================================')
print()
print(f'The program has successfully finished. See you next time!')