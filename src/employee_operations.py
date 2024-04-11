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
class Employee:
    def __init__(self, id, first_name, last_name, dob, department, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.department = department
        self.salary = salary

def delete_employee(employees):
    employee_id = input("Enter the ID which you want to delete: ")
    found = False
    for employee in employees:
        if employee.id == int(employee_id): 
            employees.remove(employee)
            found = True
            print("You successfully delete the employee.")
            break
    if not found:
        print("Given employee ID is not found.")


    with open("employee_data.txt", "w") as file:
        for employee in employees:
            file.write(f"{employee.id},{employee.first_name},{employee.last_name},{employee.dob},{employee.department},{employee.salary}\n")

#nnnnnnnnnnnnnnnnnnnnnnnnnn
if __name__ == "__main__":
    employees = [] 

    while True:
        print("\n1. Delete Employee")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            delete_employee(employees)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def delete_employee(id):
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """
    employee_id = input("Enter the ID which you want to delete: ")
    found = False
    for employee in employees:
        if employee.id == int(employee_id): 
            employees.remove(employee)
            found = True
            print("You successfully delete the employee.")
            break
    if not found:
        print("Given employee ID is not found.")


def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
