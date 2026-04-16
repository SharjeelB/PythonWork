class Employee:
    company = "TechCorp"   # Class variable

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id     # Instance variable
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"{self.emp_id} - {self.name} - {self.salary}"

emp1 = Employee(101, "Alice", 60000)
emp2 = Employee(102, "Bob", 70000)
print(emp1.get_details())
print(emp2.get_details())
