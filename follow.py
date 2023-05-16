n=int(input("Enter no of prod: "))
print("ENter gr")
prod=[]
follow={}
for x in range(n):
    prod.append(input())
def Follow(i,j):
    for k in range(n):
        if prod[k][0]==prod[i][j+1]:
            if prod[k][3]=='@':
                return f"follow({prod[i][0]})"
            if (not prod[k][3].isupper()):
                return prod[k][3]
            else:
                return Follow(k,2)
for i in range(n):
    if i==0:
         print(f"follow({prod[0][0]})=$")
    for j in range(3,len(prod[i])):
        if(prod[i][j].isupper()):
            if(len(prod[i])-1==j):
                print(f"follow({prod[i][j]})=follow({prod[i][0]})")
            f=prod[i][j]
            if(j+1<len(prod[i]) and not prod[i][j+1].isupper()):
                print(f"follow({f})={prod[i][j+1]}")
            if(j+1<len(prod[i]) and prod[i][j+1].isupper()):
                print(f"Follow({f})={Follow(i,j)}")
                

