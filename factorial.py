def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print(fact)
factorial(5)

def decToBin(num):#string
    str1=""
    r=0
    while num>0:
        r=num%2
        str1=str(r)+str1
        num=num//2
    print(str1)

decToBin(10)

def decToBin(num):#integer
    binary=0
    r=0
    place=1
    while num>0:
        r=num%2
        binary=binary+r*place
        num=num//2
        place*=10
    print(binary)

decToBin(10)







