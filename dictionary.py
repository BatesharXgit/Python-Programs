cars = {'Lamborghini': "250k", 'BMW': '200k', "Mercedes": "200k", "Land Rover": "200k"}
print(cars)

employees = dict({1: "A", 2: "B", 3: "C", 4: "D", '5': "E"})
print(employees)
employees[2] = "XD"
employees.update({3: "XYZ"})
employees[6] = input("Enter value: ")
print(employees)
del employees[5]
# employees.pop({})
print(employees)