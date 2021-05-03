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
        return super().__repr__() + ' ' + str(self.university) + ' ' + str(self.faculty) + ' ' + str(self.course) + ', Score: ' + str(self.middle_score)

p = Person('Armine', 'Hovhannisyan', 27, 'Female')
s = Student('Armine', 'Hovhannisyan', 27, 'Female', 'YSU', 'IAM', 'Discrete Math', '16')
print(p)
print(s)
