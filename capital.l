%{
#include<stdio.h>
#include<ctype.h>
int k;
void display(char *);

%}
comm [//]
t [a-z]
new [\n]
%%
{comm} {k=1;}
{t} {if(k==1){display(yytext);}}
{new} {k=0;printf("\n");}

%%
int main(){
    yylex();
    return 0;
}


void display(char *s)
{
    int i;
    for(i=0;s[i]!='\0';i++){
        printf("%c",toupper(s[i]));
    }
}
int yywrap(){
    return 1;
}