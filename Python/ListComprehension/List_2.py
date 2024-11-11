def foo(lst):
    sum = 0;
    lst1 = [float(x) for x in lst]
    for y in lst1:
        sum+=y; 
    return sum;

print(foo(['1.2', '2.6', '3.3']))
