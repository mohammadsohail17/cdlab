from collections import defaultdict

s= {
    'S': ['E'],
    'E': ['E + T', 'T'],
    'T': ['T * F', 'F'],
    'F': ['( E )', 'id']
}
clo=defaultdict(list)
for i,j in s.items():
    z=i
    k=0
    while(k<len(s[z])):
        clo[i].append("."+str(s[z][k]))
        k=k+1
l=[]

#closure for a given grammer
print("closure for a given grammer")  
for i,j in clo.items():
    z=i
    k=0
    while(k<len(clo[z])):        
        print(i,'-->',clo[z][k])
        l.append(clo[z][k])
        k=k+1
#goto for a given grammer
gt=defaultdict(list)
for i,j in s.items():
    z=i
    k=0
    while(k<len(s[z])):
        ch=s[z][k].split()
        j=len(ch)    
        c=0
        while((j>=0) and (c<=len(ch))):        
            strg=(ch[:c]+[str(".")]+ch[c:]) 
            strh=""
            for b in strg:  
                 strh+=b 
            gt[i].append(strh)         
            strh=""       
            c=c+1      
            j=j-1
        k=k+1
print("Goto statements")   
st=0
print(gt)
for i,j in gt.items():
    z=i
    k=0    
    print("state is "+str(st)) 
    st=st+1
    while(k<len(gt[z])):        
        print(i,'  -->  ',gt[z][k])
        l.append(gt[z][k])
        k=k+1