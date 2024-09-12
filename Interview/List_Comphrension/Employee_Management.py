class Employee:
    def __init__(self,salary,designation):
        self.salary = salary
        self.designation = designation

    def average(self,percentage):
        self.salary += self.salary*(percentage/100)

employee = [
    Employee(10000,"Engineer"),
    Employee(20000,"Driver")
    ]
for emp in employee:
    emp.average(10)

print([emp.salary for emp in employee])