def recur_fact(num):
    fact=1
    if num==0 or num==1:#base condition is really imp bcuz it terminates the loop
        return 1
    return num*recur_fact(num-1)
n =int(input("enter a number"))
print(recur_fact(n))


#dec to bin
def toBin(num):
    if num==0:
        return 0
    return num%2+10*toBin(num//2)
n=int(input("enter a number"))
print(toBin(n))


#return 0 if num=0 else return sum of the numbers 
def sumex(num):
    if num==0:
        return 0
    return num+sumex(num-1)
n1=int(input("enter a number"))
print(sumex(n1))
  
def add(a,b):
    return a+b,a-b
a1=int(input("enter a number"))
b1=int(input("enter a number"))
print("the sum of two numbers is ",add(a1,b1))


#find number of upper and lower case
def countCase(st):
    size=len(st)
    uc=0
    lc=0
    if size<0:
        return 0


def cnt_case(str1):
    d={"lower":0,"upper":0}
    for char in str1:
        if char.islower():
            d["lower"]+=1
        elif char.isupper():
            d["upper"]+=1
        else:
            pass
    
    print("lowercase--->:",d["lower"])
    print("uppercase--->:",d["upper"])

str2=input("enter string: ")
cnt_case(str2)


            





    