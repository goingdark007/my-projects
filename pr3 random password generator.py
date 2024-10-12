# random password generator

print(f'\n{'Random':<{8}} {'Password':<{10}} {'Generator':<{10}}')

print('-'*30)

import random

list1 = ['apple', 'banana', 'cherry','sugar','master','coder','project']

list2 = ['$', '@', '#','!']

while True:
    x = input('\nDo you want to generate a password? :- ').lower()
    if x not in ['yes','no']:
        print('\nOops invalid input. Please enter yes or no')
        continue
    else:
        break

while True:

    if x == 'yes':
        a = random.choice(list1).capitalize()

        b = str(random.randint(1,20))

        c = random.choice(list2)

        d = a + b + c

        print(f'\nRandom password is :- {d}')

        while True:
            y = input('\nDo you want to generate another password? :- ').lower()
            if y not in ['yes', 'no']:
                print('\nOops invalid input. Please enter yes or no')
                continue
            else:
                break

        if y == 'yes':
            continue

        else:
            print("\nThank you for using this program.")
            break
    else:
        print("\nThank you for using this program")
        break