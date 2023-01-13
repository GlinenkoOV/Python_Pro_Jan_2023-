class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.type = 'student'

    def __str__(self):
        return f'{self.type} - {self.surname} {self.name[0]}.'


class Instructor:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.type = 'instructor'

    def __str__(self):
        return f'{self.type} - {self.surname} {self.name[0]}.'


class Group:

    def __init__(self, instructor, title):
        self.instructor = instructor
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f'{self.title}; {self.instructor}\n' + '\n'.join(map(str, self.students))

    def __len__(self):
        return len(self.students)

teacher = Instructor('Tymchuk', 'Oleh')
x_1 = Student('Ivanov1', 'Ivan')
x_2 = Student('Ivanov2', 'Ivan')
x_3 = Student('Ivanov3', 'Ivan')
x_4 = Student('Ivanov4', 'Ivan')
x_5 = Student('Ivanov5', 'Ivan')
x_6 = Student('Ivanov6', 'Ivan')
x_7 = Student('Ivanov7', 'Ivan')

group = Group(teacher, 'Python Pro')
group.add_student(x_1)
group.add_student(x_2)
group.add_student(x_3)
group.add_student(x_4)
group.add_student(x_5)
group.add_student(x_6)
group.add_student(x_7)

print(group)
print(len(group))


print('The End')
print()

