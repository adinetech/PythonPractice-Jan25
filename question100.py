## Multiple Inheritance: Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.

class A:
    def method1(self):
        print("Method 1 of class A")

class B:
    def method2(self):
        print("Method 2 of class B")

class C(A, B):
    def method3(self):
        print("Method 3 of class C")

obj = C()
obj.method1()
obj.method2()
obj.method3()