gr=['S->AA','A->aA','A->b']
t=['S','A']
nt=['a','b','$']
follow={'S':['$'],'A':['a','b','$']}
items={'I0':['Sx->.S','S->.AA','A->.aA','A->.b'],'I1':['Sx->S.'],'I2':['S->A.A','A->.aA','A->.b'],'I3':['A->a.A','S->.AA','A->.b'],'I4':['A->b.'],
       'I5':['S->AA.'],'I6':['A->aA.']}
goto={}
for x in items.keys():
    goto[x]={}

    for y in items.keys():
       pass
