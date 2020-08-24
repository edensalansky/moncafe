from persistence import *


def printActivities():
    print('Activities')
    activities = repo.Activities.find_all()
    for a in activities:
        print("(" + str(a.product_id) + ", " + str(a.quantity) + ", " + str(a.activator_id) + ", " + str(a.date) + ")")


def printEmployees():
    print('Employees')
    employees = repo.Employees.find_all()
    for e in employees:
        print("(" + str(e.id) + ", '" + e.name + "', " + str(e.salary) + ", " + str(e.coffee_stand) + ")")


def printSuppliers():
    print('Suppliers')
    suppliers = repo.Suppliers.find_all()
    for s in suppliers:
        print("(" + str(s.id) + ", '" + s.name + "', " + s.contact_information + ")")


def printProducts():
    print('Products')
    products = repo.Products.find_all()
    for p in products:
        print("(" + str(p.id) + ", '" + p.description + "', " + str(p.price) + ", " + str(p.quantity) + ")")


def printCoffeeStands():
    print('Coffee stands')
    coffeestands = repo.Coffee_stands.find_all()
    for c in coffeestands:
        print("(" + str(c.id) + ", '" + c.location + "', " + str(c.number_of_employees) + ")")


def printEmployeesReport():
    print('Employees report')
    employees = repo.Employees.find_all()
    for e in employees:
        sum = 0
        empActivity = repo.Activities.find_all()
        for emp in empActivity:
            if emp.quantity < 0:
                if emp.activator_id == e.id:
                    sum = sum + abs(emp.quantity) * repo.Products.find(emp.product_id).price
        print(e.name + " " + str(e.salary) + " " + str(e.coffee_stand) + " " + str(sum))


def printActivitiesReport():
    print('Activities')
    activities = repo.Activities.find_all()
    for a in activities:
        p = repo.Products.find(a.product_id)
        sName = "None"
        eName = "None"
        if (a.quantity < 0):
            eName = str(repo.Employees.find(a.activator_id).name)
            eName = "'" + eName + "'"
        else:
            sName = str(repo.Suppliers.find(a.activator_id).name)
            sName = "'" + sName + "'"
        print("("+str(a.date) + ", '" + p.description + "', " + str(a.quantity) + ", " + eName + ", " + sName + ")")


def printAll():
    printActivities()
    printCoffeeStands()
    printEmployees()
    printProducts()
    printSuppliers()
    printEmployeesReport()
    printActivitiesReport()
