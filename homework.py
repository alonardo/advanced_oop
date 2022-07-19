from datetime import datetime as dt
import time

class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.created_on = dt.utcnow()

    # Option to change first and last name is shared between Employee and Customer - need to keep this in User class.
    def change_first(self):
        self.first_name = input('What would you like to change your first name to?\n').title()
    
    def change_last(self):
        self.last_name = input('What would you like to change your last name to?\n').title()
    
    def print_name(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name},  Email: { self.email}")

    def __str__(self):
        return f'<User | {self.email} >'

    def __repr__(self):
        return f'<User | {self.email} {self.created_on.strftime("%c")}>'

    def __hash__(self):
        return hash(self.email + self.created_on.strftime("%c"))

class Employee(User):
    def __init__(self, first_name, last_name, email, home_address, security_level, department):
        super().__init__(first_name, last_name, email)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department.title()

    @property    
    def id(self):
        return self.first_name.title() + ' ' + self.last_name.title() + ' ' + self.department.title()
    
    def describe_employee(self):
        self.print_name()
        print(f"Address: {self.home_address}, Security Clearance: {self.security_level}, Department: {self.department}")
        print(f"ID: {self.id}")
        
    def change_department(self):
        self.department = input('What would you like to change your department to?\n')
     

class Customer(User):
    def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history):
        super().__init__(first_name, last_name, email)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history

    @property
    def id(self):
        return self.email + ' ' + self.shipping_address
    
    def describe_customer(self):
        self.print_name()
        print(f"Home Address: {self.shipping_address}, Billing Address: {self.billing_address}, Purchase History: {self.purchase_history}")
        print(f"ID: {self.id}")
    
    def change_billing_address(self):
        self.billing_address = input('What would you like to change your billing address to?\n')
    
    def change_shipping_address(self):
        self.shipping_address = input('What would you like to change your shipping address to?\n')
      
# Employees
andre = Employee(first_name='andre', last_name='lonardo', email='aalonardo@gmail.com', home_address='123 Fake Street', security_level=5, department= 'software')
time.sleep(.5)

nick = Employee(first_name='nick', last_name='james', email='nick123@gmail.com', home_address='945 westminster', security_level=10, department= 'security')
time.sleep(.5)

marcus = Employee(first_name='marcus', last_name='bond', email='mbond@gmail.com', home_address='4988 sparrow lane', security_level=1, department= 'finance')
time.sleep(.5)

# Customers
peanut = Customer(first_name='peanut', last_name='lonardo', email='moretreatsplz@dogs.com', shipping_address='789 Good Boy Ave', billing_address='3456 Main Street', purchase_history=['beef', 'chicken', 'toys'])
time.sleep(.5)

furiosa = Customer(first_name='furiosa', last_name='tuminez', email='playwithme@gmail.com', shipping_address='128 Blair Way', billing_address='128 Blair Way', purchase_history=['fish', 'rice', 'water'])
time.sleep(.5)

luigi = Customer(first_name='luigi', last_name='hildebrand', email='yourfavorite@yahoo.com', shipping_address='6300 Ramona Lane', billing_address='1550 Robin Circle', purchase_history=['beans', 'pork', 'tortillas'])
time.sleep(.5)


employees = [andre, nick, marcus]
print(employees.sort())

# Not currently functional, here's my debuggin thought process
# What is the data type of employees? - list
print(type(employees))
#What is the data type of the individual employees inside the list of employees?
print(type(employees[0]))



# print(sorted(employees))

print('********************************')

customers = [peanut, furiosa, luigi]
print(sorted(customers))
# Not currently functional
# print(sorted(employees))

