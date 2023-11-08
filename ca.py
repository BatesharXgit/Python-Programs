#write a python program that store information about employees, including their names,
#salary and departments, the program should allow user to add employees, find employees and update employees information.

employees = []
def add_employee(name, salary, department):
    employee = {"name": name, "salary": salary, "department": department}
    employees.append(employee)

add_employee("Akshat", 50000, "HR")
add_employee("Vimarsh", 60000, "Finance")
add_employee("Rahul", 70000, "Marketing")

def find_employee(name):
    for employee in employees:
        if employee["name"] == name:
            return employee
    return None

def update_employee(name, new_salary, new_department):
    for employee in employees:
        if employee["name"] == name:
            employee["Salary"] = new_salary
            employee["department"] = new_department

print("List of employees are: ",employees)

employee_to_find = input("Enter name of employee you are looking for: ")

found_employee = find_employee(employee_to_find)
if found_employee:
    print(f"Found employee {employee_to_find}: {found_employee}")
else:
    print(f"Employee {employee_to_find} not found.")

employee_to_update = 'Rahul'
new_salary = 80000
new_department = 'Sales'
update_employee(employee_to_update, new_salary, new_department)

print("Updated employees list are: ", employees)
