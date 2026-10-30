employees = ["John Stevenson", "Jane Smith", "Tim Wilson", "Kate Stevenson", "Kate Palmer", "Tom Eastman", "Laura Green", "Mike Watson", "Sally Black", "Mark Ramsey"]
quit = False
while not quit:
    for employee in employees:
        print(employee)
    if input('if you would like to add another employee type 1 anything else will quit') == '1':
        for employee in employees:
            print(employee)
        add = input("name of employee")
        employees.append(add)
    else:
        quit = True




#
# new_employee = input("would you like to add a new employee?")
#
# while new_employee.lower()[0] == "y":
#     new_name = input("please enter a new employee name")
#     employees.append(new_name)
#     for names in employees:
#         print (names)
#     new_employee = input("would you like to add a new employee?")
