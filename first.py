n=int(input("Enter no of productions:  "))
print("enter grammar: ")
s=[]
for x in range(n):
    s.append(input())
def FIRST(i,arr):
    for k in range(n):
        if s[k][0]==s[i][3]:
            if(s[k][3].isupper()):
                return FIRST(k)
            else:
                arr.append(s[k][3])
first={}
for i in range(n):
    f=s[i][0]
    if f not in first:
        first[f]=[]
    if(s[i][3].isupper()):
        FIRST(i,first[f])
    else:
        first[f].append(s[i][3])
print(first)