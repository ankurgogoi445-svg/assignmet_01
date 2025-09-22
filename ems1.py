# Employee Management System (EMS)

# Step 1: Data Storage
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Ankur", "age": 30, "department": "Engineering", "salary": 60000},
    103: {"name": "Riya", "age": 25, "department": "Finance", "salary": 45000}
}

# Step 3: Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please try with a new ID.")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }
        print("Employee added successfully!\n")

    except ValueError:
        print("Invalid input. Please enter correct data.\n")


# Step 4: View All Employees
def view_employees():
    if not employees:
        print("No employees available.\n")
    else:
        print("\n--- Employee List ---")
        print("{:<10} {:<15} {:<5} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
        print("-" * 60)
        for emp_id, details in employees.items():
            print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(
                emp_id, details['name'], details['age'], details['department'], details['salary']
            ))
        print()


# Step 5: Search Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print("\n--- Employee Found ---")
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid input. Please enter a valid Employee ID.\n")


# Step 2 & 6: Menu System
def main_menu():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the Program
if __name__ == "__main__":
    main_menu()
 