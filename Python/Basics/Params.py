import datetime as dt;

def KeyWordArgs(**kwargs):
    print("____");
    print(kwargs.values());
    for x in kwargs.values():
        print("Values = ", x);
        print("Sum = ",sum(x));
    print("____");
    #print( sum( kwargs.values() ));
    #print("____");
    return kwargs;

#print(KeyWordArgs(a=[1,dt.date(2020,2,3),"James"], b=(2,3,"Arnab"), c={1: "James", 2:dt.date(2018,1,2), 3:1234.3 } ))
print(KeyWordArgs(a=[2,3, 4]));