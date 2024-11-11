'''
myFile = open(f"..\\Udemy-Course\\Python\\NewFile\\Data\\bear.txt");
contents = myFile.read();
print(contents);

ct = "";
with open(f"..\\Udemy-Course\\Python\\NewFile\\Data\\fruits.txt") as _file1:
    ct = _file1.read();
print(ct);
'''

class FileHelper(object):
    def __init__(self, FileName):
        self.m_FileName = FileName;
        #self.m_File="";

    def DispChars(self, iCount):
        with open(self.m_FileName) as _File:
            content = _File.read();
        return content[:iCount];

    def MatchChar(self, MatchChar):
        with open(self.m_FileName) as _File:
            content = _File.read();
        []

ex = FileHelper(f"..\\Udemy-Course\\Python\\NewFile\\Data\\bear.txt");
print(ex.DispChars(90));