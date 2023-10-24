# Person 정의
class Person:
    name = 'unknown'

    # 인스턴스 메서드 (메서드 사용 주체가 인스턴스이므로)
    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown
"""
p1은 인스턴스 변수가 정의되어 있지 않아
클래스 변수(unknown)가 출력됨
"""

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim
"""
p2는 인스턴스 변수가 정의되어
인스턴스 변수(Kim)가 출력됨
"""

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
"""
Person 클래스의 값이 Kim으로 변경된 것이 아닌
p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
"""