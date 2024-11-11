class A(object):
    def func(self):
        print("Executing A()");

class B(A):
    def funcNone(self):
        print("INside B::funcNone()");

class C(object):
    def func(self):
        print("Executing C()");

class D(B,C):
    def funcNone(self):
        print("INside D::funcNone()");

obj = D();
obj.func();
print(D.__mro__);