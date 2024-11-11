class InsCount(object):
    count=0;
    def __init__(self, value):
        self.m_val = self.filterInt(value);
        InsCount.count+=1;

    @staticmethod
    def filterInt(value):
        if isinstance(value, int):
            return value;
        else:
            return 0;

    def setVal(self, val):
        self.m_val = val;

    def getVal(self):
        return self.m_val;
    
    @classmethod
    def getInstCount(cls):
        return cls.count;

a = InsCount(10); 
b = InsCount(15); 
c = InsCount(20);

for obj in (a,b,c):
    print("Value of obj: ", obj.getVal());
print("Using Class: ", InsCount.getInstCount(), " : Using ClassAttribute: ", InsCount.count);


d = InsCount('Helpp');
for obj in (c, d):
    print("Value of obj: ", obj.getVal());

print("Using Class: ", InsCount.getInstCount(), " : Using ClassAttribute: ", InsCount.count);