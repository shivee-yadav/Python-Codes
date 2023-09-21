'''day=int(input("enter number of hours in a day: "))
part=int(input("enter number of parts the hours is divided into: "))
hrs=day/part
count=0
k=0
j=1
while(j<hrs):
    
        for  i in range(1,j+1):
            if j%i==0 :
                k+=1
        if k==2:
            for()'''



import math
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


d, p = map(int, (input().split()))
n = int(d / p)
count = 0
# as 0, 1 not prime so starting from 2
for i in range(2, n):
    prime_time = True
    for j in range(p):
        num = i + j*n
        if not prime(num):
            prime_time = False
            break

    if prime_time:
        count += 1

print(count)
            

            

    
