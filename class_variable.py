class Employee:
    
    raise_amount = 1.1
    
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + '.' + surname + '@company.com'
        
    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)
    
    def apply_raise(self):
        #self.salary = int(self.salary) * raise_amount 
        #in this case raise_amount is not defined, because it is class variable not instance
        #so we have to change code such as below     
        self.salary = int(self.salary) * self.raise_amount
        #self.salary = int(self.salary) * Employee.raise_amount
        
emp3 = Employee('John', 'Wich', 10000)
emp4 = Employee('Jennifer', 'Aniston', 12000)

print(emp3.salary)
emp3.apply_raise()
print(emp3.salary)

emp4.raise_amount=1.5
print(emp4.raise_amount)        #It will give us 1.5
print(emp3.raise_amount)        #It will return us 1.1
print(Employee.raise_amount)

#to define difference lets deep into dive

print(Employee.__dict__)
print(emp3.__dict__)
print(emp4.__dict__)


#if we override class variable such as below, it will affect all instance of class, lets test it
Employee.raise_amount=2

print(Employee.raise_amount)
print(emp3.raise_amount)
print(emp4.raise_amount)