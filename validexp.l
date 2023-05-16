%{
    #include<stdio.h>
    int operator=0;
    int operand=0;
%}

opr[=+*-/%]
opp[a-zA-Z0-9]+

%%
{opr} {operator--;}
{opp} {operator++;}
%%
int main(){
    yylex();
    if(operator==1){
        printf("valid exp");
    }
    else{
        printf("invalid");
    }
}
int yywrap(){
    return 1;
}
