no_lines=0
no_words=0
no_char=0
with open('hello.txt','r') as f:
    for x in f:
        #print(x)
        no_lines+=1
        for w in x:
            if w.isspace():
                no_words+=1
            elif w.isalpha():
                no_char+=1
    print(no_lines,no_char,no_words)