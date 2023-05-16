%{
    #include<stdio.h>

%}

oct [o][0-7]+
hex [x|X][0-9A-F]+

%%
{oct} printf("Number entered is octal");
{hex} printf("Number entered is hex");
%%

int main(){
    yylex();
}

int yywrap(){
    return 1;
}