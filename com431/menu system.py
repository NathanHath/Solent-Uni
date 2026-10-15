employees = ["John Stevenson", "Jane Smith", "Tim Wilson", "Kate Stevenson", "Kate Palmer", "Tom Eastman", "Laura Green", "Mike Watson", "Sally Black", "Mark Ramsey"]
user_quit = True
def option_1():
    add = input ("new employee name: ")#
    employees.append(add)
    for names in employees:
        print (names)
def option_2():
    for names in employees:
        print (names)
def option_3():
    global user_quit
    user_quit = False
while user_quit:
    menu = int(input("1. add new employee\n2. display all employees\n3. quit\n "))
    if menu == 1:
        option_1()
    elif menu == 2:
        option_2()
    elif menu == 3:
        option_3()
    else:
        break