class Person:

    def __init__(self, surname, name):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'

class Student(Person):

    def __init__(self, surname, name, date_of_birth):
        super().__init__(surname, name)
        self.date_of_birth = date_of_birth


class Group:

    def __init__(self, title, max_limit=10):
        self.title = title
        self.max_limit = max_limit
        self.__students = []

    def add_student(self, student: Student):
        if len(self.__students) >= self.max_limit:
            return None
        for item in self.__students:
            if (item.surname, item.name, item.date_of_birth) == (student.surname, student.name, student.date_of_birth):
                return None
        self.__students.append(student)

    def remove_student(self, student: Student):
        if student in self.__students:
            self.__students.remove(student)

    def search_by_surname(self, surname: str):
        res = []
        for item in self.__students:
            if item.surname == surname:
                res.append(item)

        return res

    def __str__(self):
        return f'{self.title}\nStudents:\n' + '\n'.join(map(str, self.__students))

    def __getitem__(self, item):
        if isinstance(item, int):
            if item >= 0 and item < len(self.__students):
                return self.__students[item]
            raise IndexError


        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or self.__students
            step = item.step or 1
            if step == 0:
                raise IndexError
            if start < 0 and stop >= len(self.cars_list):
                raise IndexError
            res = []
            for item in range(start, stop, step):
                res.append(self.__students[item])
            return res

    def __len__(self):
        return len(self.__students)



x_1 = Student('Ivanov 1', 'Ivan', '01.01.2000')
x_2 = Student('Ivanov 2', 'Ivan', '01.01.2000')
x_3 = Student('Ivanov 3', 'Ivan', '01.01.2000')
x_4 = Student('Ivanov 4', 'Ivan', '01.01.2000')
x_5 = Student('Ivanov 5', 'Ivan', '01.01.2000')
x_6 = Student('Ivanov 6', 'Ivan', '01.01.2000')
x_7 = Student('Ivanov 7', 'Ivan', '01.01.2000')
x_8 = Student('Ivanov 8', 'Ivan', '01.01.2000')
x_9 = Student('Ivanov 9', 'Ivan', '01.01.2000')
x_10 = Student('Ivanov 10', 'Ivan', '01.01.2000')
x_11 = Student('Ivanov 11', 'Ivan', '01.01.2000')
x_12 = Student('Ivanov 12', 'Ivan', '01.01.2000')
x_13 = Student('Ivanov 3', 'Ivan', '01.01.2000')

gr_1 = Group('Python Start', max_limit=2)
gr_2 = Group('Python Pro')

gr_1.add_student(x_1)
gr_1.add_student(x_3)
gr_1.add_student(x_4)

gr_2.add_student(x_2)
gr_2.add_student(x_5)
gr_2.add_student(x_6)
gr_2.add_student(x_7)
gr_2.remove_student(x_6)
# print(gr_1)
# print(gr_2)

# st_surname = input('surname=')
# res = gr_2.search_by_surname(st_surname)
# print('*'.join(map(str, res)))

print(gr_1[0:2])
for student in gr_1:
    print(student)
print('**********')
for student in gr_2:
    print(student)