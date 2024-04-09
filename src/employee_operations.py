"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""
from file_operations import read_employees, write_employees


def add_employee(first_name, last_name, dob, department):
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
        'salary': "salary"
    }
    list_emp.append(new_employee)
    write_employees(list_emp)


def delete_employee():
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
