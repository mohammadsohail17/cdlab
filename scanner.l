%{
    /*hello there*/
%}

digit [A-Za-z0-9]+

%%
if|while {printf("valid keyword : %s",yytext);}
{digit} {printf("valid identifier:%s",yytext);}
%%
int main()
{
yylex();
}
int  yywrap()
{
 printf("not");
 return 1;
}