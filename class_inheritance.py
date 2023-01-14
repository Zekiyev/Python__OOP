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
        
class Developer_Test(Employee):
    pass

#print(help(Developer_Test))
#print(help(Employee))

dev1 = Developer_Test('Orxan', 'Zekiyev', 4000)
print(dev1.raise_amount)


#if you want to add bonus argument with parent class's arguments, u dont need repeat 
#parent class's argument, just use super method
class Developer(Employee):
    def __init__(self, name, surname, salary, prog_lang):
        super().__init__(name, surname, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, name, surname, salary, employees=None):
        super().__init__(name, surname, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_11 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_12 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_11])

print(mgr_1.email)

mgr_1.add_emp(dev_12)
mgr_1.remove_emp(dev_12)

mgr_1.print_emps()