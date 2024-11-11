class MyClass(object):
    def getVal(self):
        return self._val;

    def setVal(self, value):
        self._val = value;

obj1 = MyClass();
obj2 = MyClass();

obj1.setVal(10);
obj2.setVal(100);

print("Obj1= ", obj1, ": obj1.Value", obj1.getVal());
print("Obj2= ", obj2, ": obj1.Value", obj2.getVal());

obj2._val = 'James';
print("Obj2= ", obj2, ": obj1.Value", obj2.getVal());