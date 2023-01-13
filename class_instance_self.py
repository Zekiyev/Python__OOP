##Let's create a class and explain line by line

class Test_Employee:
    
    def __init__(x, name, surname):
        x.name = name
        x.surname = surname
        x.email = name + '.' + surname + '@company.com'
        
    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)
#__init__ function is constructor method the first argument which it accepts is self instance 
#of object, shortly self. object. So it will be good name it by self

#in line 10, we creating another function which is class method
#Don't forget that every method or function of class must accept self argument, else 
#it will be return error 

emp1 = Test_Employee('John','Wich')
emp2 = Test_Employee('Jennifer', 'Aniston')

print(emp1.get_full_name())

#Don't forget that every method or function of class must accept self argument, else 
#it will be return error 

print(Test_Employee.get_full_name(emp2))

#because of emp1.get_full_name is equivalent for Test_Employee.get_full_name(emp1)


#now it our class looks like pretty good
class Employee:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.email = name + '.' + surname + '@company.com'
        
    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)