import datetime


#Class methods affects all instances by calling from a instances
#It acceps firstly cls argument instead of self

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
        self.salary = int(self.salary) * self.raise_amount
        
    @classmethod
    #it will be generate objects by parcing from given str, this is say that we can
    #create another constructer method method by cls
    def create_from_string(cls, my_str):
        name, surname, salary = my_str.split('-')
        return cls(name, surname, salary)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @staticmethod
    #withoud any required argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
     
emp3 = Employee('John', 'Wich', 10000)
emp4 = Employee('Jennifer', 'Aniston', 12000)


emp3.set_raise_amount(3.5)
print(Employee.raise_amount)
print(emp3.raise_amount)
print(emp4.raise_amount)


my_str1 = 'Jonathan-Smith-8000'
my_str2 = 'Aaron-Dyche-11000'

print(Employee.create_from_string(my_str1).surname)
print(Employee.create_from_string(my_str2).name)


my_date = datetime.date(2021, 7, 11)

print(Employee.is_workday(my_date))