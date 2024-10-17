# random password generator

print(f"\n{'Random':<{8}} {'Password':<{10}} {'Generator':<{10}}")

print('-'*30)

import random

list1 = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

list2 = [33, 35, 36, 37, 38, 42, 43, 47,60, 61, 62, 63, 64, 92, 94, 95, 126]

while True:
    x = input('\nDo you want to generate a password? (type yes or no) :- ').lower()
    if x not in ['yes','no']:
        print('\nOops invalid input. Please enter yes or no')
        continue
    else:
        break
            
def another():
    while True:
        y = input('\nDo you want to generate another password? (type yes or no) :- ').lower()
        if y not in ['yes', 'no']:
            print('\nOops invalid input. Please enter yes or no')
            continue
        else:
            return y
            break

while True:

    if x == 'yes':
        a = random.choices(list1,k = 5)

        b = random.choices(list2,k = 3)

        m = a + b
        random.shuffle(m)
        n = ''
        for i in m:
            n += chr(i)

        print(f'\nRandom password is :- {n}')

        y = another()
                
        if y == 'yes':
            continue

        else:
            print("\nThank you for using this program.")
            break
    else:
        print("\nThank you for using this program")
        break
