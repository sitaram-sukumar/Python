import datetime as dt

class Example(object):
    print("Example - Class Begins");
    classVar = "test";
    print(f"<<<{classVar=}>>>"); #print(f"<<<{classVar}>>>");

    def __new__(cls, *args, **kwargs):
        print(f"<<<Example - Entering new>>>");
        print(f"<<<{cls=}, {args=}, {kwargs=}>>>");
        return super().__new__(cls);

    def __init__(self, **kwargs):
        print("<<<Example - Entering init>>>");
        self.__dict__.update(kwargs);
        print(f"<<<{self.__dict__=}>>>");
        print(f"<<<{type(self.__dict__)=}>>>");

    print("<<<Example - Middle of the class decl>>>");

    def example_func(self):
        print(f"<<<{self.classVar=}>>>");

    def AppendToDict(self, newDict):
        print("type of ", type(newDict));
        (self.__dict__).update(newDict);
        
    def PrintDictVals(self):
        print(self.__dict__, " :: Type :: ", type(self.__dict__));
        for ky in (self.__dict__):
            print("Key= ", ky, " :: Val=", (self.__dict__)[ky]);

    print("<<<Example - End of Class Defn>>>")

ex = Example(a=1, b=10);
ex.AppendToDict({'d':[1,2,3], 'f':dt.date(2002, 1, 2) });
ex.PrintDictVals();
print(f"{Example.__dict__=}");
print(f"{type(ex)=}")
print(f"________________________________________________");
#print(f"{type(type)=}")
#print(f"{type(type(type))=}")

''' ========== method ============ '''
class_body = ''' 
print("Example2 -- Class Begins");
classVar = "test";
print(f"<<<{classVar=}>>>");

def __new__(cls, *args, **kwargs):
    print(f"<<<Example2 - Entering new>>>");
    print(f"<<<{cls=}, {args=}, {kwargs=}>>>");
    return super(Example2, cls).__new__(cls);

def __init__(self, **kwargs):
    print("<<<Example2 - Entering init>>>");
    self.__dict__.update(kwargs);
    print(f"<<<{self.__dict__=}>>>");
    print(f"<<<{type(self.__dict__)=}>>>");

print("<<<Example2 - Middle of the class decl>>>");

def example_func(self):
    print(f"<<<{self.classVar=}>>>");

def AppendToDict(self, newDict):
    print("type of ", type(newDict));
    (self.__dict__).update(newDict);
    
def PrintDictVals(self):
    print(self.__dict__, " :: Type :: ", type(self.__dict__));
    for ky in (self.__dict__):
        print("Key= ", ky, " :: Val=", (self.__dict__)[ky]);

print("<<<Example2 - End of Class Defn>>>") ''';

namespace = type.__prepare__();
exec(class_body, globals(), namespace);
Example2 = type("Example2", (), namespace);
ex2 = Example2(a=1, b=10);
