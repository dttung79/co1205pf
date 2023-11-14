employees = {}

def print_employees():
    for id, name in employees.items():
        print(f"ID: {id}, Name: {name}")

def add_employee():
    id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    if id in employees:
        print("Employee already exists")
    else:
        employees[id] = name
        print("Employee added")

def edit_employee():
    id = input('Enter employee ID to edit: ')
    name = input('Enter new name: ')
    if id not in employees:
        print('Employee does not exist')
    else:
        employees[id] = name
        print('Employee updated')

def del_employee():
    id = input('Enter employee ID to delete: ')
    if id not in employees:
        print('Employee does not exist')
    else:
        del employees[id]
        print('Employee deleted')

### Main ###
running = True
while running:
    print('1. Print employees')
    print('2. Add employee')
    print('3. Edit employee')
    print('4. Delete employee')
    print('5. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print_employees()
    elif choice == '2':
        add_employee()
    elif choice == '3':
        edit_employee()
    elif choice == '4':
        del_employee()
    elif choice == '5':
        running = False
    else:
        print('Invalid choice')
    print()
