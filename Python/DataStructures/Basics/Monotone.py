def monotonic_array(array):
    #write code here
    iLen = len(array);
    bIsMonotone = True;
    
    # check for monotone Increasing
    for k in range(1, iLen):
        if array[k-1]>=array[k]:
            bIsMonotone = False;
            break;
    
    if bIsMonotone == False:
        bIsMonotone = True;
        for k in range(1, iLen):
            if array[k-1]<=array[k]:
                bIsMonotone = False;
                break;
    
    return bIsMonotone;

print( monotonic_array([89,75,0,-2,-3,]) )