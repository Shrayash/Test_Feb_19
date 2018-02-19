#Q3. Create a Employee class and initialize it with first_name, last_name and salary. Also, it has a derived attribute called email, which is self generated when instance is created. Now, make methods to :
      #a. Display - It should display all information of the employee instance.

class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary= salary
