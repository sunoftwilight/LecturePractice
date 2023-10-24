# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'  # class입장에서 blood_color는 속성

    # 메서드
    def __init__(self, name):   # 개발자가 직접 호출하는 메서드 아님 (내부적으로 인스턴스 생성 시 자동으로 호출됨 - 생성자 메서드 : 해당 메서드 있어야 인스턴스 생성 가능)
        self.name = name            

    def singing(self):
        return f'{self.name}가 노래합니다.'
    

# 인스턴스 생성
singer1 = Person('IU')   # 생성자 함수에서 name이라는 위치 인자를 설정해뒀기 때문에 Person 사용시 'IU'와 같이 인자 꼭 넣어줘야함
singer2 = Person('BTS')  # 동일한 클래스로 만든 다른 인스턴스


# 메서드 호출
print(singer1.singing())         # IU가 노래합니다.
print(singer2.singing())         # BTS가 노래합니다.
# 동일한 클래스에서 생성된 메서드를 이용하지만, 변수가 다르므로 다른 결과 출력
# self.name은 결국 인스턴스가 가지는 독립적인 변수임 (인스턴스 변수)
# name은 class 내부에서 정의되지 않음


# 속성(변수) 사용
print(singer1.blood_color)       # red
print(singer2.blood_color)       # red
# 클래스 내에서 정의된 blood_color(클래스 변수)를 동일하게 참조하므로 동일한 결과 출력