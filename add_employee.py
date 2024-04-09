def add_employee(employees_data: list, employees_ID: int):
    # Input employee details
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    dob = input("Enter employee's date of birth (YYYY-MM-DD): ")
    department = input("Enter employee's department: ")
    
    # Validate and process salary input
    while True:
        try:
            salary = float(input("Enter employee's salary: "))
            break
        except ValueError:
            print("Invalid salary input. Please enter a valid number.")
    
    # Create new employee dictionary
    new_employee = {
        'ID': employees_ID,
        'first_name': first_name,
        'last_name': last_name,
        'dob': dob,
        'department': department,
        'salary': salary
    }
    
    # Append new employee to the list
    employees_data.append(new_employee)
    print("Employee added successfully.")

# Example usage:
if __name__ == "__main__":
    # Sample usage within main function
    employees = []  # List to hold employee data
    employee_id_counter = 1  # Counter for assigning unique employee IDs
    
    # Call the add_employee function
    add_employee(employees, employee_id_counter)
