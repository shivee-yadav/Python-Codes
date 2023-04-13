#set()-->multiple elements can be stored in a single variable
#unordered,unchangeable,unindexed
#also use{curly braces}

#set1={}-->wrong bc it'll be considered as a dictionary by the compiler
set1=set()#empty set
print(set1,type(set1))

set2=set((1,2,3,4,5,6))#-->tuple has been passed in the args
print(set2)

#set2=set(0,9,8,(1,2,3))---->can't pass multiple sequences 

set3={29,"esha",78.79}
print(set3)
#print(set3[0])--->doesn't support indexing
#set3[1]=299--->doesnt supportitem assignment

set3.add(23)#adding an item
print(set3)

set3.update([1,2,3,4,5],('a','aa'),(21.5,87.6))
print(set3)

#accessing items
for i in set3:
    print(i)

#remove(),discard(),pop(),clear()del
print(set3)
print(len(set3))
set3.remove(2)
print(set3)
set3.discard(78.79)
print(set3)
#set3.remove(500)--->generates error
set3.discard(500)#doesnt gives error even if the item is absent
print(set3)
set3.pop()
print(set3)

set3.clear()
print(set3)

del set3


#set() methods--->union(),interection()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9,10}
print(a.union(b))
print(a|b)
#intersection()
print(a.intersection(b))
print(a&b)
#difference()
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

#symmetric difference
print(a.symmetric_difference(b))#--->discards common values and prints the items together as whole
print(a^b)
a.difference_update(b)#--->discards common elements from the main set
print(a)
print(b)
b.difference_update(a)
print(a)
print(b)