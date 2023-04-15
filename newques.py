rangeLeft=int(input("enter left range: "))
rangeRight=int(input("enter right range: "))
flag=True
sum=0
if rangeLeft>=-1e9 and rangeRight<=1e9:
    for i in range(rangeLeft,rangeRight+1):
        if i<0:
            for j in range(2,-i):
                if i%j==0:
                    break
            else:
                #print(i)
                sum=sum+i
        else:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
               #print(i)
                sum=sum+i
    print("sum of all the prime numbers between ",rangeLeft,"and ",rangeRight," is ",sum)
else:
    print("invalid input")

#oops
#class Student:


           