


def spellCheck(s1,s2,k1):
    if s1==s2:
        return 1
    elif len(s1)==len(s2):
        length=len(s1)
        count=0
        for i in range(0,length):
            if s1[i]==s2[i]:
                count+=1
        diff=length-count
        if diff<k1:
            return 2
        elif diff>k1:
            return 4
        else :
            return 3
    else:
        return "unmatched strings"

str1=input("enter string 1: ")
str2=input("enter string 2: ")
k=int(input("enter number of characters mismatched: "))
print(spellCheck(str1,str2,k))


#ques2
str1=input("enter string: ")
word=""
str2=""
str1=str1+" "
for i in str1:
    word=i+word
    if i==" ":
        str2=str2+word 
        word=""      
  
print(str2)

#tea
#ate
str1=input("enter string 1: ")
str2=input("enter string 2: ")
temp=True
if len(str1)!=len(str2):
    print("not same")
else:
    for i in str1:
        if i in str2:
            continue
        else:
            temp=False
    if temp==True:
        print("same")


#palindrome in the string
str1=input("enter string: ")
word=""
word1=""
str2=""
palin=[]
str1=str1+" "
print(str1)

for i in str1:
    word=word+i
    #print(word)
    word1=i+word1
    
    if i==" ":
        print(word,word1)
        str2=str2+word1
        if word==word[::-1]:
            print(word)
            palin.append(word)
        word="" 
        word1=""
              
palin.append("mom")  
print(str2)
print(palin)