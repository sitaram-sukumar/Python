'''myFile = open(f"..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\FileIO\\fruits.txt");
print(myFile.read());
print("+++++++++++++")
myFile.close();
'''
content="NULL";
with open('..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\FileIO\\fruits.txt') as myFile1:
    content = myFile1.read();

print(content);