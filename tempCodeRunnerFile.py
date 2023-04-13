k=0
s1=""
l2=[]
string="is2 Thi1s Tes4t 3a"
for i in string:
    if(i.isalpha):
        s1=s1+i
    elif(i.isdigit):
        k=i
        
    else:
       
        l2.insert(k,s1)
        s1=""
print(l2)
