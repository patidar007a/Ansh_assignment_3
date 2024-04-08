def update_employee(employees):
    employee_id = input("Enter the ID of the employee to update: ")

    for employee in employees:
        if employee.get('ID') == employee_id:
            print("Employee found. Enter new details:")
            employee['first_name_of_employee'] = input("Enter new first name (leave empty to skip): ")
            employee['last_name_of_employee'] = input("Enter new last name (leave empty to skip): ")
            employee['dob'] = input("Enter new date of birth (YYYY-MM-DD) (leave empty to skip): ")
            employee['department'] = input("Enter new department (leave empty to skip): ")
            salary = input("Enter new salary (leave empty to skip): ")
            if salary:
                employee['salary'] = float(salary)
            print("Employee details updated successfully.")
            return

    print("Employee with ID '{}' not found.".format(employee_id))