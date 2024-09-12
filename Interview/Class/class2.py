class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f"name is {self.name}\nID is {self.id}\nsalary is {self.salary}"


class Manager(Employee):
    def __init__(self, name, id, salary, pid):
        super().__init__(name, id, salary)
        self.pid = pid

    def get_details(self):
        super().get_details()
        return f"complete manager details is name is {self.name}\nID is {self.id}\nsalary is {self.salary}\nManager id is {self.pid}"


class Developer(Employee):
    def __init__(self, name, id, salary, skill):
        super().__init__(name, id, salary)
        self.skill = skill

    def get_details(self):
        super().get_details()
        return f"Developer Details name is {self.name}\nID is {self.id}\nsalary is {self.salary}\nSkill is {self.skill}"


employees = [
    Employee("Vasanth", 420, 10000000000),
    Manager("Arun", 421, 2938848, 115),
    Developer("Amar", 422, 384444848, "python")

]
try:
    for emp in employees:
        print(emp.get_details())
except Exception as e:
    print(f"error occurred:{e}")
finally:
    print(f"Employee name: {emp.name}")
