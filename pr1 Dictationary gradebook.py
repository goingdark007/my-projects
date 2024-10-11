student = {

}

print(f"{'Grade Book':>{15}}")

print('-'*20,'\n')

print('Enter 1-5:\n\n1. Add a student and grade.\n\n2. View grade book.\n\n3. Update a student\'s grade.\n\n4. Delete a student.\n\n5. Exit.')

def add():
    a = input('\nEnter the student\'s name: ').upper()
    b = input('\nEnter the student\'s grade: ').upper()
    student.update({a:b})
    print('\nThe student is successfully added to grade book')

def view():
    print(f"\n{'Key':<{15}} {'Value':<{15}}")
    print('-'*30)
    for i, j in student.items():
        print(f'\n{i:<{15}} {j:<{15}}')

def update():
    a = input('\nEnter the name of the student: ').upper()
    if a in student.keys():
        b = input('\nEnter the student\'s grade: ').upper()
        student.update({a:b})
        print('\nThe student\'s grade is successfully updated to grade book')
    else:
        print('\nSorry, student name not found in the grade book')

def delete():
    a = input('\nEnter the name of the student: ').upper()
    if a in student.keys():
        del student[a]
        print('\nThe student is successfully deleted from grade book')
    else:
        print('\nSorry, student name not found in the grade book')

while True:
    try:
        n = int(input('\nEnter the operation you want to perform: '))
    except ValueError:
        print("\nOops! That wasn't a number. Please enter a valid number.")
        continue

    if n == 1:
        add()
    elif n == 2:
        view()
    elif n == 3:
        update()
    elif n == 4:
        delete()
    elif n == 5:
        print('\n\nExiting the program.Thank you for using this program.')
        break
    else:
        print('Sorry, invalid input. Please enter between number 1-5.\n')
