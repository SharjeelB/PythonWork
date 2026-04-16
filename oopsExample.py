#Inheritance in Python allows a new class (called a child class or subclass) to inherit

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
emp1 = Employee(101, "Alice", 60000)
emp2 = Employee(102, "Bob", 70000)
print(emp1.emp_id, emp1.name, emp1.salary)


#child class inheriting from Employee class
class EmployeeDetails(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department
emp_details = EmployeeDetails(103, "Charlie", 80000, "HR")
print(emp_details.emp_id, emp_details.name, emp_details.salary, emp_details.department)


#Child redefines parent method.
emp = EmployeeDetails(104, "Alice", 70000, "IT")
emp.department = "Finance"
print(emp.department)
