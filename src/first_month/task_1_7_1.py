from task_1_5_2 import Money

class Person:
    def __init__(self, name, surname, age, gender):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return str(self.__name) + ' ' + str(self.__surname) + ' - ' + str(self.__gender) + ', ' + str(self.__age) + ' years old'



class Student(Person):
    def __init__(self, name, surname, age, gender, university, faculty, course, middle_score):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__middle_score = middle_score

    def __repr__(self):
        return super().__repr__() + ' - Info: ' + str(self.__university) + ' ' + str(self.__faculty) + ' ' \
               + str(self.__course) + ', Score: ' + str(self.__middle_score)

    def get_score(self):
        return self.__middle_score

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university


class Teacher(Person):
    def __init__(self, name, surname, age, gender, university, faculty, discipline, experience, salary):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__discipline = discipline
        self.__experience = experience
        self.__salary = salary

    def __repr__(self):
        return super().__repr__() + ' - Info: ' + str(self.__university) + ' ' + str(self.__faculty) + ' ' \
               + str(self.__discipline) + ', Years at university: ' + str(self.__experience) \
               + ', Salary: ' + str(print(self.__salary))  # why should I use str(). print() is already returning string

    def get_discipline(self):
        return self.__discipline

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university

    def get_experience(self):
        return self.__experience

    def get_salary(self):
        return self.__salary


p = Person('Armine', 'Hovhannisyan', 27, 'Female')
s = Student('Armine', 'Hovhannisyan', 27, 'Female', 'YSU', 'IAM', 'Discrete Math', 16)
t = Teacher('Gegham', 'Jivanyan', 30, 'Male', 'Beyond Hub', 'Python', 'Data Science', '?', Money(10000000, 'usd'))
print(p)
print(s)
print(t)
print(s.get_score())
print(s.get_faculty())
print(s.get_university())

print(t.get_discipline())
print(t.get_faculty())
print(t.get_university())
print(t.get_experience())
print(t.get_salary())

#print(p.__name)
