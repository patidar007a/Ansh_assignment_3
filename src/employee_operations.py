"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""
from file_operations import read_employees, write_employees


def add_employee(first_name, last_name, dob, department, salary):
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """

    list_emp = read_employees()
    last_emp = list_emp[len(list_emp)-1]
    last_id =last_emp['ID']
    new_employee = {
        'ID': last_id,
        'first_name': first_name,
        'last_name': last_name,
        'dob': dob,
        'department': department,
        'salary': salary
    }
    list_emp.append(new_employee)
    write_employees(list_emp)


def delete_employee(id):
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
    def update_employee(employees):
    employee_id = input("Enter the ID of the employee to update: ")

    for employee in employees:
        if employee.get('ID') == employee_id:
            print("Employee found. Enter new details:")
            employee['first_name'] = input("Enter new first name (leave empty to skip): ")
            employee['last_name'] = input("Enter new last name (leave empty to skip): ")
            employee['dob'] = input("Enter new date of birth (YYYY-MM-DD) (leave empty to skip): ")
            employee['department'] = input("Enter new department (leave empty to skip): ")
            employee['salary'] = input("Enter new salary (leave empty to skip): ")
            if salary:
                employee['salary'] = float(salary)
            print("Employee details updated successfully.")
            return

    print("Employee with ID '{}' not found.".format(employee_id))
