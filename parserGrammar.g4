parser grammar parserGrammar;

options { tokenVocab=lexerGrammar; }

// Produção principal
prog        : PROGRAM IDENTIFIER PVIG decls? cmdComp PONTO ;

// Declaração de variáveis
decls       : VAR listDecl+ ;
listDecl    : declTip PVIG ;
declTip     : listId DPONTOS tip ;
listId      : IDENTIFIER (VIG IDENTIFIER)* ;
tip         : INTEGER | BOOLEAN | STRING ;

// Comandos compostos
cmdComp     : BEGIN listCmd END ;
listCmd     : cmd (PVIG cmd)* ;

// Comandos básicos
cmd         : cmdIf
            | cmdWhile
            | cmdRead
            | cmdWrite
            | cmdAtrib
            | cmdComp ;

// Comando IF
cmdIf       : IF expr THEN cmd (ELSE cmd)? ;

// Comando WHILE
cmdWhile    : WHILE expr DO cmd ;

// Comando READ
cmdRead     : READ ABPAR listId FPAR ;

// Comando WRITE
cmdWrite    : WRITE ABPAR listW FPAR ;

// Atribuição
cmdAtrib    : IDENTIFIER ATRIB expr ;

// Expressões
expr        : relExpr ;
relExpr     : addExpr (OPREL addExpr)? ;
addExpr     : multExpr (OPAD multExpr)* ;
multExpr    : unaryExpr (OPMULT unaryExpr)* ;
unaryExpr   : OPNEG unaryExpr
            | ABPAR expr FPAR
            | IDENTIFIER
            | CTE
            | TRUE
            | FALSE
            | STRING_LITERAL ;

// Lista de expressões para o comando WRITE
listW       : expr (VIG expr)* ;