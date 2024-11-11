class MyNum(object):
    def __init__(self):
        self._val = 15;
        print("Inside Ctor");

    '''' def __init__(self, newVal):
        self._val = newVal;
        print("Inseide new cotr")                   '''

    def increment(self):
        self._val = self._val+1

    def getVal(self):
        return self._val;

    def setVal(self, newVal):
        self._val = newVal;

n1 = MyNum();
n2 = MyNum();

n1.increment(); n1.increment();
print(n1.getVal())

n2.setVal(200); n2.increment();
print(n2.getVal());