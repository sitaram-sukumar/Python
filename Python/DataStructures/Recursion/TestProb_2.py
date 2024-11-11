def NotOf(iVal):
    if iVal==0:
        return 1;
    elif iVal ==1:
        return 0;
    return 0;

def kthsymbol(n, k):
    if n==1: 
        return 0;
    else:
        length = 2**(n-1);
        hfLen = length/2;
        if(k<=hfLen):
            return kthsymbol(n-1, k);
        else:
            return NotOf(kthsymbol(n-1, k-hfLen));

print(kthsymbol(5,15))