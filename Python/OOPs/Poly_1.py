class Animal(object):
    def __init__(self, name):
        self.m_name = name;

    def eat(self, food):
        print("{0} eats {1}".format(self.m_name, food));

class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the {1}".format(self.m_name, thing));

    def showAff(self):
        print("{0} wags tail, of type: {1}".format(self.m_name, type(self)));

class Cat(Animal):
    def swatString(self):
        print("{0} shreads string".format(self.m_name));

    def showAff(self):
        print("{0} purrs, of type: {1}".format(self.m_name, type(self)));

for a in ( Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout'), Animal('Animal') ):
    a.showAff();