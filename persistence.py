import os
import sqlite3
import atexit


# -------------------DTO-------------------------------------------
class Employees:
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Suppliers:
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Products:
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


class Coffee_stands:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activities:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# -------------------DAO-------------------------------------------
# Data Access Objects:
# All of these are meant to be singletons
class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employees):
        self._conn.execute("""
               INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
           """, [employees.id, employees.name, employees.salary, employees.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, salary, coffee_stand FROM Employees WHERE id = ?
        """, [employee_id])

        return Employees(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, salary, coffee_stand FROM Employees
        """).fetchall()

        return [Employees(*row) for row in all]


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, name, contact_information FROM Suppliers WHERE id = ?
            """, [id])

        return Suppliers(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, contact_information FROM Suppliers
        """).fetchall()

        return [Suppliers(*row) for row in all]


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, description, price, quantity FROM Products WHERE id = ?
            """, [id])

        return Products(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, description, price, quantity FROM Products
        """).fetchall()

        return [Products(*row) for row in all]

    def update_table(self, quantity, id):
        c = self._conn.cursor()
        sql = "UPDATE   Products    SET quantity    =   ?  WHERE   id  =   ?"
        val = (quantity, id)
        c.execute(sql, val)




class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
                INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, location, number_of_employees FROM Coffee_stands WHERE id = ?
            """, [id])

        return Coffee_stands(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, number_of_employees FROM Coffee_stands
        """).fetchall()

        return [Coffee_stands(*row) for row in all]


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Activity):
        self._conn.execute("""
                INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [Activity.product_id, Activity.quantity, Activity.activator_id, Activity.date])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT product_id, quantity, activator_id, date FROM Activities WHERE product_id = ? ORDER BY date 
            """, [id])

        return Activities(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT product_id, quantity, activator_id, date FROM Activities ORDER BY date 
        """).fetchall()

        return [Activities(*row) for row in all]


# -------------------Repository-------------------------------------------

class _Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = _Employees(self._conn)
        self.Suppliers = _Suppliers(self._conn)
        self.Products = _Products(self._conn)
        self.Coffee_stands = _Coffee_stands(self._conn)
        self.Activities = _Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):

        cur = self._conn.cursor()
        self._conn.executescript("""
            CREATE TABLE Employees (
                  id    INT PRIMARY KEY,
                  name  TEXT  NOT NULL,
                  salary    REAL    NOT NULL,
                  coffee_stand  INT,
                  FOREIGN KEY(coffee_stand) REFERENCES Coffee_stands(id)
              );
    
            CREATE TABLE Suppliers (
                  id    INT PRIMARY KEY,
                  name  TEXT    NOT NULL,
                  contact_information   TEXT
              );
    
            CREATE TABLE Products (
                  id    INT   PRIMARY KEY,
                  description   TEXT    NOT NULL,
                  price REAL    NOT NULL,
                  quantity  INT NOT NULL
              );
              
            CREATE TABLE Coffee_stands (
                  id    INT PRIMARY KEY,
                  location  TEXT    NOT NULL,
                  number_of_employees   INT
              );
            CREATE TABLE Activities (
                  product_id    INT REFERENCES  Product(id),
                  quantity  INT NOT NULL,
                  activator_id  INT NOT NULL,
                  date  DATE    NOT NULL,
                   
                  FOREIGN KEY(product_id) REFERENCES Products(id)
              );
    """)



# the repository singleton
repo = _Repository()
atexit.register(repo._close)
