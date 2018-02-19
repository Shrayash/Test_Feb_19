#Q3. Create a Employee class and initialize it with first_name, last_name and salary. Also, it has a derived attribute called email, which is self generated when instance is created. Now, make methods to :
      #a. Display - It should display all information of the employee instance.

class Employee():
    def __init__(self,first_name,last_name,Salary):
        self.first_name = first_name
        self.last_name = last_name
        self.Salary= Salary

    def emailGenerator(self):
        self.email = self.first_name.lower() + '.' + self.last_name.lower() + '@deerwalk.edu.np'

    def displayInfo(self):
        print("First name: {}\nLast name: {}\nEmail: {}\nSalary: {}".format(self.first_name, self.last_name, self.email,self.Salary))

emp1 = Employee(input('Enter first name: '), input('Enter last name: '),input('Salary: '))
emp1.emailGenerator()
emp1.displayInfo()

