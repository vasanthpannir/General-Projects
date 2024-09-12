class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        try:
            return sum(self.grades)/len(self.grades)
        except ZeroDivisionError:
            return "No grades available"


students = [
               Student("Alice",[85,92,78]),
               Student("Bob",[76,87,45]),
               Student("Charlie",[])
               ]
for student in students:
    print(f"{student.name}'s average grade:{student.average_grades()}")









