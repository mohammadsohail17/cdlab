nott=['S','L','X']
t=['a',',','(',')','$']
First={'S':['(','a'],'L':['(','a'],'X':[',','@']}
prod=['S->(L)','S->a','L->SX','X->,SX','X->@']
Follow={'S':['(',',','$'],'L':[')'],'X':[')']}
LL={}
for x in nott:
    LL[x]={}
    for y in t:
        LL[x][y]=[]
flag=0
for x in prod:
    m=x[0]
    a=x[3]
    if a in t:
        LL[m][a].append(x)
    elif x[3]=='@':
        for y in Follow[m]:
            LL[m][y].append(x)
    else:
        for y in First[a]:
            LL[m][y].append(x)
print("    ",end="")
for x in t:
    print(x,end="\t\t")
print()
for x in LL.keys():
    print(x,end=" ")
    for y in t:
        if (len(LL[x][y])!=0):
            print(LL[x][y],end='\t')
            if (len(LL[x][y])>1):
                flag=1
        else:
            print("\t\t",end="")
    print()