parser grammar parserGrammar;

options { tokenVocab=lexerGrammar; } // Liga o parser ao lexer

// Regras de produção

prog        : PROGRAM ID PVIG decls cmdComp ;
decls       : ( VAR listDecl )? ;
listDecl    : declTip ( PVIG declTip )* ;
declTip     : listId DPONTOS tip ;
listId      : ID ( VIG ID )* ;
tip         : INTEGER | BOOLEAN ;

cmdComp     : BEGIN listCmd END ;
listCmd     : cmd ( PVIG cmd )* ;
cmd         : cmdIf
            | cmdWhile
            | cmdRead
            | cmdWrite
            | cmdAtrib
            | cmdComp ;

cmdIf       : IF expr THEN cmd ( ELSE cmd )? ;
cmdWhile    : WHILE expr DO cmd ;
cmdRead     : READ ABPAR listId FPAR ;
cmdWrite    : WRITE ABPAR listW FPAR ;
cmdAtrib    : ID ATRIB expr ;

expr        : expr OPREL expr
            | expr OPAD expr
            | expr OPMULT expr
            | OPNEG expr
            | ABPAR expr FPAR
            | ID
            | CTE
            | TRUE
            | FALSE ;

listW       : expr ABPAR VIG expr FPAR* ;
  