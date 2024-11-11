def Good_Sorted_squared(array):
    iLen = len(array);
    i=0; j = iLen-1;
    newArray = [0]*iLen;

    for k in reversed(range(iLen)):
        iSq = array[i]**2;      jSq = array[j]**2;
        if(iSq>=jSq):
            newArray[k]= iSq;
            i+=1;
        else:
            newArray[k]=jSq;
            j-=1;

    return newArray;

print(Good_Sorted_squared([-10,-4,-2,0,1,5]));
print(Good_Sorted_squared([0,1,5,6,7,8,9]));