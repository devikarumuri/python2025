#oops concepts
#polymorphism
class laptop():
    def details(self,a):
        print("this is laptop",a)
class computer(laptop):
    def details(self,a):
        print("this is computer",a)
        super().details(a)
obj = computer()
obj.details("$500")

#encapsulation
#protected variable(_)
class atm():
    def __init__(self,a):
     self._a=a
     print("hello",a)
class atm_2(atm):
    def display (self):
     print(self._a)
obj = atm_2("kotak bank atm")
obj.display()

#private  variable (__)
class Car:
    def __init__(self,a):
        self.__a=a
        print("benz",a)
class BMW(Car):
    def display(self):
        print(self._Car__a)
obj = BMW("this is luxury car")
obj.display()
