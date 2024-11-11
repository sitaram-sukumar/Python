class InsCount(object):
    count=0;
    def __init__(self, val):
        self.m_value = val;
        InsCount.count+=1;

    def getVal(self):
        return self.m_value;

    def setVal(self, value):
        self.m_value = value;

    @classmethod
    def getCounter(cls):
        return count;

a = InsCount(10);
b= InsCount(20);
c = InsCount(30);

for obj in (a,b,c):
    print("Val of obj: {0}".format(obj.getVal()));

print("Instance counter: {0}".format(obj.count));
print("Instance counter: {0}".format(InsCount.count));
#print("Instance counter: {0}".format(obj.getCounter())); # will not work
print("Instance counter: {0}".format( InsCount.getCounter() )); # will not work

