#dictionary is an unordered collection of time
#each item has a key/ value pair
#empty dictionary
dict1={}
print(dict1)

print(type(dict1))

#dict with integer
dict2={1:'abc',2:'xyz',3:'pqr'}
print(dict2)

dict3={'address':'civil lines',2:456}
print(dict3)

#using dict()
dict4=dict({'name':'sameer','add':'xyz','mobile':'xxxxxx'})
print(dict4)

dict5=dict([(1,'ria'),(2,'sonali'),(3,'akash')])
print(dict5)
print(type(dict5))
#access data member /dictionary items
dict6={'name':('sonali','ria','seema'),'roll no':(101,102,103),'age':(11,12,13)}
print(dict6['age'])
print(dict6['name'])
print(dict6['roll no'])
print(dict6['name'][0])
print(dict6['name'][1])
print(dict6['name'][2])
print(dict6['roll no'][0])
print(dict6['roll no'][1])
print(dict6['roll no'][2])
print(dict6['age'][0])
print(dict6['age'][1])
print(dict6['age'][2])
print(dict6)
#changing and adding items
dict6['name']=('a','b')
print(dict6)

dict6['add']=('abc','xyz','stu')
print(dict6)

#removing items from dictionary pop(key),popitems(),del
print(dict6.pop('name'))
print(dict6)
print(dict6.popitem())
print(dict6)

del dict6
#error print(dict6)

#dictionary methods
#copy() ----> return a copy of dictionary
data={1:'a',2:'b',3:'c'}
copdata=data.copy()
print(data)
print(copdata)

#from keys (key value) ----> create dictionary from given sequence(string,list,tuple)
key=(1,2,3)
data=dict.fromkeys(key)
print(data)
value="xyz"
data=dict.fromkeys(key,value)
print(data)


#item(),key(),values(),update()
#item()-->return pair
print(dict2.items())
#keys()-->return keys
print(dict2.keys())
#values()--->return values
print(dict2.values())

#update
print("\n")
print(dict3)
print(dict4)
dict3.update(dict4)
print(dict3)

def solve(nums):
        n=len(nums)
        n=len(nums)
        k=0
        maxx=0
        if n>=0 and n<=100000:
            for i in range(n):
                for j in range(i,n):
                    if nums[i]==nums[j]:
                        k+=1
                if k>maxx:
                    maxx=k
                k=0
            return maxx
        maxx=0

def dictt(nums):
    d={}
    for num in nums:
        if num in d:
            d[num]+=1
        else:
            d[num]=1
    m=0
    for key,value in d.items():
        if value>m:
            m=value
    return m

def dictt2(nums):
    d={}
    for num in nums:
        if num in d:
            d[num]+=1
        else:
            d[num]=1
    m=0
    for key,value in d.items():
        if value>m:
            m=value
    return m



 

