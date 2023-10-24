class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

# def __init__을 생략하는 것은 권장하지 않음.
# 따라서 가장 상위의 class에서 init 후 super로 참조해오는 것이 가장 정석임
class Mom(Person):
    gene = 'XX'

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom): 
    mom_gene = Mom.gene  # gene이 공통 인자이므로 Person에서 정의하고, 만약 엄마의 유전자를 받아오고 싶다면  (***강의 다시 보기***)
    def __init__(self, name):
        super().__init__(name)
        # Dad.__init__(self, name, age)   # 만약 Dad와 Mom의 init이 다른데 Dad의 init을 쓰고싶다면 이처럼 명시적으로 작성을 해야함 (super로는 Dad에 접근 불가)

    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())    # 첫째가 응애 -> 본인의 인스턴스 메서드
print(baby1.swim())   # 첫째가 수영 -> 본인의 인스턴스 메서드
print(baby1.walk())   # 아빠가 걷기 -> 본인 클래스에 없으니 부모 클래스로 찾아 올라감 -> Dad에 walk() 있으니 그걸 받아옴
print(baby1.gene)     # XY -> 본인 클래스에 없으니 부모 클래스로 찾아 올라감 
                      # -> Dad와 Mom에 둘 다 있음 -> Dad가 우선 상속 -> Dad 정보 우선으로 받아옴

print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]