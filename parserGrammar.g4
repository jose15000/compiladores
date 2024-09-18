parser grammar parserGrammar;

options { tokenVocab=lexerGrammar; }

// Produção principal
prog        : PROGRAM ID PVIG decls? cmdComp PONTO ;

// Declaração de variáveis
decls       : VAR listDecl ;
listDecl    : declTip (PVIG declTip)* ;
declTip     : listId DPONTOS tip ;
listId      : ID (VIG ID)* ;
tip         : INTEGER | BOOLEAN ;

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

cmdIf       : IF expr THEN cmd (ELSE cmd)? ;
cmdWhile    : WHILE expr DO cmd ;
cmdRead     : READ ABPAR listId FPAR ;
cmdWrite    : WRITE ABPAR listW FPAR ;
cmdAtrib    : ID ATRIB expr ;

// Expressões com precedência e associatividade
expr        : relExpr ;

relExpr     : addExpr (OPREL addExpr)* ;
addExpr     : multExpr (OPAD multExpr)* ;
multExpr    : unaryExpr (OPMULT unaryExpr)* ;
unaryExpr   : OPNEG unaryExpr
            | ABPAR expr FPAR
            | ID
            | CTE
            | TRUE
            | FALSE ;

// Lista de expressões para o comando WRITE
listW       : expr (VIG expr)* ;
