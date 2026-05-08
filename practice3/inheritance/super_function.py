class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

student1 = Student("Ali", "A")

print(student1.name)
print(student1.grade)