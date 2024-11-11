def MatchChar(MatchChar, fileName):
    content="";
    with open(fileName) as _File:
        content = _File.read();
        
    iCount = 0;
    lst = [x for x in content if x==MatchChar]
    return len(lst);
    

def Disp90Chars(fileName):
    content = "";
    with open(fileName) as _File:
        content = _File.read();

#    return content[:90];
        
    lst = [x for x in content];
    str ="";
    iCount = 0;
    
    for x in lst:
        iCount = iCount+1;
        if iCount > 90:
            break;
        str+= x;
        
    return str;

print(MatchChar('N', f"..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\FileIO\\bear.txt"));
#print(Disp90Chars(f"..\\2.ExploratoryDataAnalysis\\Udemy-Course\\Python\\FileIO\\bear.txt"));