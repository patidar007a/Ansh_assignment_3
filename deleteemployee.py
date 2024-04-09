def delete_employee(employees_data: list, employees_id: int):
    for employee in employees_data:
        if employee['ID']==employees_id:
            employees_data.remove(employee)
            print(f"employee having employee ID {employees_id} is deleted successfully")
            return
        print(f"Employee having employee id{employees_id} is not available" )

