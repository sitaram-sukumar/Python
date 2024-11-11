class RecursiveClass(object):
    sVal = "";
    bInReverse = False;

    def __init__(self):
        return;    
    
    def GenValues(self, iVal):
        if iVal!= 0:
            self.sVal += f"{iVal} "; # str(iVal);
            iVal-=1;
            self.GenValues(iVal);
        else:
            return self.sVal;
    
oRecur = RecursiveClass();
print(oRecur.GenValues(5));
