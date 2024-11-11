class MyNum(object):
    m_val = -13;

    def __init__(self, value):
        self.m_val = value;

    def getVal(self):
        return self.m_val;

    def setVal(self, value):
        self.m_val = value;

    def getVar(self):
        return m_val;

n1 = MyNum(10);
print(n1.getVal(), " -- ", n1.m_val, " -- ", MyNum.m_val );

n1.m_val = 'James';
print(n1.m_val);
del n1.m_val;
print(n1.m_val);