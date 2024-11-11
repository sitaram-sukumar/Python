'''
content = "";
with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\data.txt", "a+") as File:
    content = File.read();
    iCount = 3;
    
    while iCount>0:
        iCount = iCount -1;
        File.write(content);


content = "";
str1="";
with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\data.txt", "r") as File:
    content = File.read();
    iCount = 2;
    
    while iCount>0:
        iCount = iCount -1;
        str1 = str1+ content;
        

with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\data.txt", "a+") as File:
    File.write(str1);
'''

content = "";
str1="";
with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\data1.txt", "r") as _File:
    content = _File.read();

with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\Modules\\data1.txt", "a+") as _File:
    iCount = 2;
    while iCount>0:
        iCount = iCount -1;
        _File.write(content);
        _File.seek(0);