class UserError(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg


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
     try:
        if len(self.__students) < self.max_limit:
            self.__students.append(student)
        else:
            raise UserError("In group should be up to 10 students ")
     except UserError as err:
        print(err)


    def remove_student(self, surname):
        for item in self.__students:
            if item.surname == surname:
                self.__students.remove(item)
                return None


    def search_by_surname(self, surname: str):
        res = []
        for item in self.__students:
            if item.surname == surname:
                res.append(item)

        return res

    def __str__(self):
        return f'{self.title}\nStudents:\n' + '\n'.join(map(str, self.__students))


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


gr_1 = Group('Python Start', max_limit=2)
gr_2 = Group('Python Pro')

gr_1.add_student(x_1)
gr_1.add_student(x_3)
gr_1.add_student(x_4)

gr_2.add_student(x_2)
gr_2.add_student(x_5)


print(gr_1)
print(gr_2)

