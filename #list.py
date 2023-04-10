#list
l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
print(type(l1))#type

#append
l1.append(7)
print(l1)

#len() function ---->return length of list
print(len(l1))

#insert(ind,value)---->insert element at specified index
l1.insert(2,"shivee")

#extend()---->add multiple element or add element 
k=0
s1=""
s2=""
l2=[]
string="is2 Thi1s Tes4t 3a"
for i in string:
    if(i.isalpha):
        s1=s1+i
    elif(i.isdigit):
        k=i
    else:
        l2.insert(k,s1)
        
print(l2)
