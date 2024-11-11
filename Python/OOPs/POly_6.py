import random;
class Animal(object):
    def __init__(self, value):
        self.m_name = value;

class Dog(Animal):
    def __init__(self, value):
        super(Dog, self).__init__(value);
        self.m_breed = random.choice(["Lab", "Gol Ret", "Chi"]);

    def fetch(self, thing):
        print('{0} goes by the name : {1} and get this {2}'.format(self.m_breed, self.m_name, thing));

d = Dog('Rover');
print(d.m_name, d.m_breed);
d.fetch('Fizbee');