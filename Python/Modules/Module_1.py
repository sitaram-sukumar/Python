import time as t;
iCount = 5;

while iCount >0:
    with open("..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\FileIO\\bear.txt") as _File:
        print(_File.read());
        t.sleep(3);
        print("_____________________")
        iCount=iCount-1;