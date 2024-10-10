student = {}

print('----Grade book----')
print('Enter 1-5:\n1. Add student and grade\n2. View grade book\n3. Update a student\'s grade\n4. Delete a student\n5. Exit')

def add():
    a = input('Enter the student name: ').lower()
    b = input('Enter the student grade: ')
    student.update({a:b})
    print('Successfully added')

def view():
    for i, j in student.items():
        print(i, '\t: ', j)

def update():
    a = input('Enter the name of the student: ').lower()
    if a in student.keys():
        b = input('Enter grade: ')
        student.update({a:b})
        print('Successfully updated')
    else:
        print('Student name not found')

def delete():
    a = input('Enter the name of the student: ').lower()
    if a in student.keys():
        del student[a]
        print('Successfully deleted')
    else:
        print('Student name not found')

while True:
    try:
        n = int(input('Enter: '))
    except ValueError:
        print("Oops! That wasn't a number. Please enter a valid number.")
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
        print('Exiting the program.\nThank you for using this program')
        break
    else:
        print('Invalid input')
