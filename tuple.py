#tuple is similar of list,difference is we cannot change element

#empty tuple
tup=()
print(type(tup))

#single element
tup1=(23,)
print(type(tup))

tup2=(10,20,"sonali")
print(tup2)

#unpacking
a,b,c=tup2
print(a)
print(b)
print(c)


#access tuple element
tup3=(1,2,3,4,5,6,7,8,[9,10,11])
print(tup3)
print(tup3[1])
print(tup3[::-1])
print(tup3[1:7])
print(tup3[8])
print(tup3[8][1])

tup3[8][0]=100
print(tup3)

#concatenation-->
print(tup2+tup3)

# *--->repeat
print(tup2*3)

#methods
#count(),index()
print(tup3.count(2))
print(tup3.index(2))


#remove(),pop(),del() --->do not work

tup4=2,3,4,5,6,7,8
if tup4.count(5)!=0:
    print("5 is present")

name=("ria","shivee","anu","rashi")

for i in name:
    print("hey",i)
