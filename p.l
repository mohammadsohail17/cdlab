%{
    #include "y.tab.h"
%}
%%

[0-9]+(\.[0-9]*)? return num;
[+/*] return op;
. return yytext[0];
\n return 0;
%%
int yywrap(){
    return 1;
}