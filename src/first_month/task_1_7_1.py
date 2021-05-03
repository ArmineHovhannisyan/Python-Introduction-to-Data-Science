from task_1_5_2 import Money

class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return str(self.name) + ' ' + str(self.surname) + ' - ' + str(self.gender) + ', ' + str(self.age) + ' years old'


class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.university = university
        self.faculty = faculty
        self.course = course
        self.middle_score = middle_score

    def __repr__(self):
        return super().__repr__() + ' - Info: ' + str(self.university) + ' ' + str(self.faculty) + ' ' \
               + str(self.course) + ', Score: ' + str(self.middle_score)


class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.university = university
        self.faculty = faculty
        self.discipline = discipline
        self.experience = experience
        self.salary = salary

    def __repr__(self):
        return super().__repr__() + ' - Info: ' + str(self.university) + ' ' + str(self.faculty) + ' ' \
               + str(self.discipline) + ', Years at university: ' + str(self.experience) \
               + ', Salary: ' + str(print(self.salary))  # why should I use str(). print() is already returning string


p = Person('Armine', 'Hovhannisyan', 27, 'Female')
s = Student('Armine', 'Hovhannisyan', 27, 'Female', 'YSU', 'IAM', 'Discrete Math', 16)
t = Teacher('Gegham', 'Jivanyan', 30, 'Male', 'Beyond Hub', 'Python', 'Data Science', '?', Money(10000000, 'usd'))
print(p)
print(s)
print(t)
