student = {
    
}

print('----Grade book----')

print('Enter 1-5:\n1. Add student and grade')

print('2. View grade book')

print('3. Upate a students grade')

print('4. Delete a student')

print('5. Exit')


def add():
    a = input('Enter the student name :').lower()
    b = input('Enter the student grade :')
    student.update({a:b})
    print('Succesfully added')
    
    
def view():
    for i,j in student.items():
        print(i,'\t: ',j)    


def update():
    a = input('Enter the name of the student: ').lower()
    
    if a in student.keys():
        b = input('Enter grade : ')
        student.update({a:b})
        print('Successfully updated')
    else:
        print('student name not found')
 
 
def delete():
    a = input('Enter the name of the student: ').lower()
    
    if a in student.keys():
        del student[a]
        print('Succesfully deleted')
            
    else:
        print('student name not found')
        
                   
while True:
    n = int(input('Enter :'))

    if n == 1:
        add()
        
    elif n == 2:
        view()

    elif n == 3:
        update() 
    
    elif n == 4:
        delete()
        
    elif n == 5:
        print('Exiting the program.\n Thank you for using this program')
        break
        
    else:
        print('Invalid input')