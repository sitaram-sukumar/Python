import random;

class Animal(object):
    def __init__(self, name):
        self._name = name;

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name); 
        self.m_breed = random.choice(['Lab', 'Gold Retr', 'Rott', 'chi']);

    def fetch(self, thing):
        print( "{0} goes after {1}".format(self._name, self.m_breed) );

d = Dog('dogname');
print(d._name);
print(d.m_breed);
d.fetch('Frizbee');