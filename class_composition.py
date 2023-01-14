class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_salary(self):
        result =self.pay * 12 + self.bonus
        return result
    
class Employee:
    def __init__(self, name, surname, pay, bonus):
        self.name = name
        self.surname = name
        self.obj_salary = Salary(pay, bonus)
        
    def total_salary(self):
        return self.obj_salary.annual_salary