import array
a=array.array('i',[1,2,3,4,5,6])
print(a)
print(type(a))
print(a.typecode)
for i in range(len(a)):
    print("element",i+1,":",a[i])
#b=array.array('i',['a',12,23.4])
#print(a)#error
print(a.buffer_info)#object
print(a.buffer_info())#(address,length)
a[0]=34
print(a)
a.append(24)
print(a)
a.extend([1,2,3,4])
print(a)
a.insert(3,68)#insert(i,value)
print(a)
print(a.itemsize)#bytesize
print(len(a))
print(len(a)*a.itemsize)
print(a.buffer_info()[1]*a.itemsize)



#1
import array
a=array.array('i',[1,2,3,4,5])
'''print("enter array elements: ")
for i in range(5):
    a[i]=input()'''
for i in range(len(a)):
    print("element",i+1,":",a[i])
print("first three elements are: ")
print(a[0])
print(a[1])
print(a[2])
a.append(11)
print(a)
a.reverse()
print(a)
print(a.itemsize)
print(a.buffer_info())
print(a.buffer_info()[1]*a.itemsize)
b=array.array('i',[1,2,30,20,30,4,5,30])
c=int(input("enter item to be checked for occurence:"))
count=0
for i in range(len(b)):
    if b[i]==c:
        count+=1
print("number of occurence of ",c,"is ",count)
l1=[1,2,3,4]
b.fromlist(l1)
print(b)
new=int(input("enter new element: "))
b.insert(1,new)
print(b)

