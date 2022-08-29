print(globals())

def foo(x):
    print(locals())
    def bar(x):
        print(x)
        print(y)
    print(locals())
    y = "y"
    print(locals())
    return bar

print(globals())
fun = foo(3)
print(globals())
fun(4)

# scope 변수명 충돌을 방지하는 등의 목적으로 중복 변수명을 허용하지 않는 범위를 정한 것
# namespace와 동의어
# 이는 곧 파이썬 인터프리터가 관리하는 identifier-memory address table을 의미
# 하나의 table은 하나의 namespace
# table 현재 등록 내용을 보기 위해서는 globals() / locals() 


class Foo():

    def __init__ (self, xx, yy):

        print(xx)
        print(yy)

    def foobar(self):
        print(self.z)

    def barfoo(self, x):
        print(x)

    def foofoo():
        print("no self")

    foofoo()
    z = "z"
    print(z)


f = Foo(33, 44)
print(f.z)


f.foobar()
f.barfoo(3)



Foo(44, 766)


class Bar(Foo):



    def __init__(self, z):

        print(z)
        self.barfoo(3)
        super().__init__(555, 666)

Bar(6667877)

# test