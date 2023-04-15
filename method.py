class Student:
    clg='jec'#class variable


    def __init__(self,m1,m2,m3,m4):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4

    def display(self):
        print("student marks:")
        print(self.m1,self.m2,self.m3,self.m4)

    def per(self):
        return (self.m1+self.m2+self.m3+self.m4)/4
    
    @classmethod#decorator---->
    def show_cls_info(cls):
        print(cls.clg)#class method
    

s1=Student(34,36,37,38)
s1.display()
print(s1.per())

Student.show_cls_info()





##################


def setVal(func):
    def swap(a,b):
        if a>b:
            a,b=b,a
        return func(a,b)
    return swap

@setVal
def avgoftwo(a,b):
    print(a/b)

avgoftwo(20,2)#10.0
avgoftwo(2,20)#0.1
#we want that if denominator is greater than numerator still it returns greater/smaller
#avgoftwo=setVal(avgoftwo)
avgoftwo(20,2000)
