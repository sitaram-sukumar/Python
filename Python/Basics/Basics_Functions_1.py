def mean(lst):
    if isinstance(lst, list) or isinstance(lst, tuple):
        mean = sum(lst)/ len(lst)
        return mean
    elif isinstance(lst, dict):
        mean = sum(lst.values())/ len(lst)
        return mean
    else:
        return "No Mean"

def sq_area(side):
    return str(side*side)

print("The mean = ", mean(list(range(1,10))))
print(type(mean), ":: ", type(sum) )
print("The mean = ", mean({"James":10, "Lily":15, "Serverus":20}))
print("The mean = ", mean( (12, 13, 14) ))
print("The mean = ", mean( "James" ))

print("The Area = ", sq_area(20) )

def foo(x, array):
    if x in array:
        return True
    else:
        return False
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

def Check_temp(temp):
    if temp>25:
        return "Very Hot"
    elif temp>=15 and temp<=25:
        return "Moderate"
    else:
        return "Cold"
print(Check_temp(10))
print(Check_temp(16))
print(Check_temp(27))