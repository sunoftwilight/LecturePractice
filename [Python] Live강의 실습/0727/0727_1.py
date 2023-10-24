class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        # self.name = name
        # self.age = age
        Person.__init__(self, name, age)
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        # self.name = name
        # self.age = age
        # Person.__init__(self,name, age)
        super().__init__(name, age)         # self도 사용X
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 클래스인 Person의 talk 메서드 활용
p1.talk()    # 반갑습니다. 박교수입니다.
s1.talk()    # 반갑습니다. 김학생입니다.