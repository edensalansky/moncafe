from persistence import *
import os
import sys

if os.path.isfile("moncafe.db"):
    os.remove("moncafe.db")
file = open("config.txt", "r")
repo.__init__()
repo.create_tables()
file =open(sys.argv[1],"r")
for line in file:

    line = line.replace('\n', "")
    input = line.split(', ')
    if input[0] == 'E':
        employee=Employees(int(input[1]), input[2], float(input[3]), int(input[4]))
        repo.Employees.insert(employee)
    if input[0] == 'S':
        supplier=Suppliers(int(input[1]), input[2], input[3])
        repo.Suppliers.insert(supplier)
    if input[0] == 'P':
        product = Products(int(input[1]), input[2], float(input[3]), 0)
        repo.Products.insert(product)
    if input[0] == 'C':
        coffee_stands = Coffee_stands(int(input[1]), input[2], float(input[3]))
        repo.Coffee_stands.insert(coffee_stands)

