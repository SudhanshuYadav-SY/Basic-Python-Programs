from abc import ABC, abstractmethod


#Class A is an Abstract class because it contains one or more abstract functions
class A(ABC):                               #ABC is a predefined class in Python Library
    @abstractmethod
    def method_1(self):                     #Abstract Method as no function body exists
        pass
    @abstractmethod
    def method_2(self):                     #Abstract Method as no function body exists
        pass

    def method_3(self):
        print("Inside Method 3")

class B(A):
    def method_1(self):
        print("Inside Method 1")

#We can not create objects for Abstract Classes
#To Access Abstract methods you can create a child class and implement the same
#obj = A()
obj = B()
obj.method_1()
obj.method_2()
obj.method_3()