'''class Student:
    def __init__(self, name, surname, data_birth):
        self.name = name # name - це те що передали
        self.surname = surname
        self.data_birth = data_birth
        print(self)

st_1 = Student('Ivan','Ivanov','10.10.2000')  # викликаємо метод init
print(hex(id(st_1)))
#print(st_1.name,st_1.surname,st_1.data_birth)
#st_2 = Student('Petro','Ivanov','10.10.2000')
#print(st_2.name, st_2.surname, st_2.data_birth)'''

'''class Student:
    def __init__(self, name, surname, data_birth):
        self.name = name # name - це те що передали
        self.surname = surname
        self.data_birth = data_birth
        
    def __str__(self): # Повернути стрічкове представлення обєкту 
        return f'{self.surname} {self.name[0]}.'

st_1 = Student('Ivan','Ivanov','10.10.2000')  # викликаємо метод init
print(st_1)
st_1.breed = 'good student' # додаємо до словника 

st_2 = Student('Petro','Ivanov','10.10.2000')
print(st_2)

#x = st_1.__str__()  #  або print(st_1)
#print(x)

print(st_1.__dict__)
print(Student.__dict__)
print(st_2.__dict__)
print(Student.__dict__)'''

'''# Виводимо на екран  st_1.breed = 'good student
class Student:
    def __init__(self, name, surname, data_birth):
        self.name = name  # name - це те що передали
        self.surname = surname
        self.data_birth = data_birth

# Виводимо на екран  st_1.breed = 'good student
    def __str__(self):  # Повернути стрічкове представлення обєкту
        res = ''
        for key, value in self.__dict__.items():
            res += f'{key}: {value}\n'
        return res


st_1 = Student('Ivan', 'Ivanov', '10.10.2000')  # викликаємо метод init
st_1.breed = 'good student' # додаємо до словника

st_2 = Student('Petro', 'Ivanov', '10.10.2000')

print(st_1)
print(st_2)'''

# Якщо треба розширити
'''class Student:
    def __init__(self, name, surname, data_birth, *args,**kwargs):
        self.name = name  # name - це те що передали
        self.surname = surname
        self.__data_birth = data_birth

# Виводимо на екран  st_1.breed = 'good student
    def __str__(self):  # Повернути стрічкове представлення обєкту
        res = ''
        for key, value in self.__dict__.items():
            res += f'{key}: {value}\n'
        return res
    #def __method(self):
    #    pass

st_1 = Student('Ivan', 'Ivanov', '10.10.2000')  # викликаємо метод init
st_1.breed = 'good student' # додаємо до словника

st_2 = Student('Petro', 'Ivanov', '10.10.2000')
print(st_1.__dict__)  # Словник
st_1._Student__data_birth = 'Hello' # Зі словником можемо робити все що завгодно
print(st_1)
#print(st_1.__data_birth)'''

# Треба створити групу студентів
class Student:
    def __init__(self, name, surname, data_birth):
        self.name = name  # name - це те що передали
        self.surname = surname
        self.__data_birth = data_birth

#
    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Group:
    def __init__(self, title): # Треба передати назву групу
        self.title = title
        self.__students = [] # Заводиться атрибут і це буде пустий список

# У групи буде поведінка. Група дозволяє додавати студента до списку

    def add_student(self, student:Student): # student буде посилатись на  екземпляр класу(инстанс )класу  students
        if isinstance(student, Student) and  student not in self.__students:  #Перевіряємо якщо наш студетн є інстансом класу Student and ще відсутній у групі Перевірка щоб не додавались слова Привіт замість st_5....
         # Якщо не має такого студента то тоді його додати, а якщо такий студент вже є  ми нічого не робимо. student:Student - Анотація
            self.__students.append(student)

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.__students))
        # Ми знаємо що в списку students зберігаються інстанси
        # класу student. В класі student є метод str тому для кожного студента буде викликати метод str
        # в класі student. Хочу кожного студента з нової стрічки прописати'\n'.join(map
        #  з великої букви


st_1 = Student('Ivan 1', 'Ivanov 1', '10.10.2000')
st_2 = Student('Ivan 2', 'Ivanov 2', '10.10.2000')
st_3 = Student('Ivan 3 ', 'Ivanov 3', '10.10.2000')
st_4 = Student('Ivan 4', 'Ivanov 4', '10.10.2000')
st_5 = Student('Ivan 5', 'Ivanov 5', '10.10.2000')
# Створюю інстанс класу Group
python_pro = Group('Python Pro')
python_pro.add_student(st_1)
python_pro.add_student(st_2)
python_pro.add_student(st_3)
python_pro.add_student(st_4)
python_pro.add_student(st_5)
python_pro.add_student('Hello') # Однакові студенти
python_pro.add_student(st_5) # Однакові студенти
print(python_pro)

