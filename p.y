%{
    #include<stdio.h>
    int valid=0;


%}
%token num op
%%

s:  num x s{printf("end");}
   | num {printf("hello\n");}
   ;
x:  op '-' {printf("op\n");}
   | 
   ;
%%
int yyerror(){
    valid=0;
    printf("\nInvalid\n");
    return 0;
}
int main(){
    printf("\nenter:\n");
    yyparse();
    if(valid){
        printf("\ninvalid \n");
    }
}
