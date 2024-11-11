class MaxSizeCustomList(object):
    def __init__(self, maxSize):
        self.m_MaxSize = maxSize;
        self.m_lst = [];

    def push(self, val):
        if len(self.m_lst)>=self.m_MaxSize:
            self.m_lst.pop(0);
        
        self.m_lst.append(val);

    def get_lst(self):
        print(self.m_lst);
        