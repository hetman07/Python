# Класс Person

# Создайте класс Person, представляющий человека.
# Каждый человек должен иметь имя.
# Добавьте метод introduce(), который выводит приветствие с именем.

class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Hello, my name is {self.name}"

u1 = Person("Alice")
# print(u1.introduce())

# Класс Student

# На основе класса Person создайте класс Student.
# Студент должен иметь имя и номер курса.
# Метод introduce() должен сначала выводить базовое приветствие, 
# а затем строку: I'm on course <номер_курса>.

class Student(Person):
    def __init__(self, name, n_course):
        super().__init__(name)
        self.n_course = n_course
        
        
    def introduce(self):
        base = super().introduce()
        return f"{base}\nI'm on course {self.n_course}"
   
std1 = Student('Alice', 2)   
# print(std1.introduce())     

# Класс Teacher и список людей

# На основе класса Person создайте класс Teacher.
# У преподавателя есть имя и предмет.
# Метод introduce() должен выводить строку: 
#     Hello, I am professor <имя>. My subject is <предмет>.

# Создайте список, в котором будут Student и Teacher, 
# и вызовите у всех метод introduce().


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def introduce(self):
        return f"Hello, I'm professor {self.name}.\nMy subject is {self.subject}"
   
tchr1 = Teacher('Bob', 'Math')   
# print(tchr1.introduce())  

for item in [Person("Alice"), Student('Alla', 2), Teacher('Bob', 'Math')]:
    print(item.introduce()) 
