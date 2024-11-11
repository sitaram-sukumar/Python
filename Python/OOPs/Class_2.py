class MyInteger:
    def getVal(self):
        return self._val;

    def setVal(self, value):
        try:
            self._val = int(value);
        except ValueError:
            return;

    def increment(self):
        self._val = self._val+1;
        
obj1 = MyInteger();
obj1.setVal(10);
obj1._val = 'Hi'
print("Current value: ", obj1.getVal());
obj1.increment();
print("Current value: ", obj1.getVal());
