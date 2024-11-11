class ProbSolver(object):
    def __init__(self):
        self.iCounter = 1;  self.arr = [0]*1;
        return;
    def kth_symbol(self, n, k):
        if self.iCounter != n:
            if self.iCounter==1:
                self.arr[0]=0;

            self.iCounter+=1;                           iNumCountPerLine = 2**(self.iCounter-1);
            arrCurr = [0]*iNumCountPerLine;             iCurrArrIdx = 0;
            for i in range(0, len(self.arr)):
                if self.arr[i]==0:
                    arrCurr[iCurrArrIdx] = 0;   iCurrArrIdx+=1;
                    arrCurr[iCurrArrIdx] = 1;   iCurrArrIdx+=1;
                elif self.arr[i]==1:
                    arrCurr[iCurrArrIdx] = 1;   iCurrArrIdx+=1;
                    arrCurr[iCurrArrIdx] = 0;   iCurrArrIdx+=1;
            
            self.arr = arrCurr;
            self.kth_symbol(n, k);
        return self.arr[k-1];
oProb = ProbSolver();
kthVal = oProb.kth_symbol(5,8);
print(kthVal);



def arrTest(self):
    arr = [0]*5;
    arr1 = [0]*10;
    iCount =0;
    for x in range(100, 110):
        arr1[iCount] = x;
        iCount+=1;
    arr = arr1;

    ilen = len(arr);
    for i in range(0, ilen):
        print(f"{i=} >> {arr[i]=}");