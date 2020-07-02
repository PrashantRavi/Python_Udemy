class Student:

    def __init__(self):
        self.__id =123
        self.__name="raj"

    def display(self):
        print(self.__id)
        print(self.__name)

s1 = Student()
s1.display()

print(s1._Student__id)