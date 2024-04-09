"""
Employee Management System Module

This module provides various functionalities for managing employee data, 
including adding, deleting, updating, and generating reports.
"""
import src.menu as menu

def main():
    """
    Main function to start the Employee Management System.
    
    This function calls the main_menu() function to display the main menu
    of the Employee Management System to the user.
    """
    menu.main_menu()

if __name__ == "__main__":
    main()
    
def add_employee(employees):
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")

    new_employee = {
        'name': name,
        'age': age,
        'position': position
    }

    employees.append(new_employee)
    print("Employee added successfully.")

# Example usage:
# Initialize an empty list to store employees
employees_list = []

# Call the function to add an employee
add_employee(employees_list)

# Print the updated list of employees
print("Updated List of Employees:")
print(employees_list)