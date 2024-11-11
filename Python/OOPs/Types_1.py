#import MyTestModule as MTM;
#print(MTM._TestVariable, "-- ", type(MTM._TestVariable), " -- ", type(MTM));

from MyTestModule  import _TestFunc, _TestVariable;
print(_TestVariable, "-- ", type(_TestVariable), " -- ", type(_TestVariable));
print(_TestFunc());

lst = [1,2,3,4];
_MyBool = True;
_MyNone = None;
def func():
    print("Func()");
    return 1;

print(type(lst));
print(type(_MyBool));
print(type(_MyNone));
print(type(func));
lstType = type(lst);
print(type(lstType));
print(type(type(lstType)));


