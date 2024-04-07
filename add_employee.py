def add_employee(employees_data: list, employees_ID: int):
    first_name_of_employee =input("Enter your first name:")
    last_name_of_employee =input("Enter your last name:")
    dob=input("Enter your date of birth:")
    your_department=input("Enter the department:")
    salary= float(input("Enter the salary:"))

    new_employee={
        'ID': employees_ID,
        'first_name_of_employee':first_name_of_employee,
        'last_name_of_employee':last_name_of_employee,   
        'dob':dob,
        'department':your_department,
        'salary' : salary
    }
    
    employees_data.append(new_employee)
    print("Successfully added.")