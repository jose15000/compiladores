parser grammar parserGrammar;

options {
    tokenVocab=lexerGrammar;
}

prog: PROGRAM ID PVIG decls cmdComp PONTO;

decls: (VAR listDecl)? ;

listDecl: declTip (PVIG declTip)* ;

declTip: listId DPONTOS tip ;

listId: ID (VIG ID)* ;

tip: INTEGER | BOOLEAN | STRING;

cmdComp: BEGIN listCmd END ;

listCmd: cmd (PVIG cmd)* ;

cmd: cmdIf
    | cmdWhile
    | cmdRead
    | cmdWrite
    | cmdAtrib
    | cmdComp ;

cmdIf: IF expr THEN cmd elseOpt ;

elseOpt: ELSE cmd | ;

cmdWhile: WHILE expr DO cmd ;

cmdRead: READ ABPAR listId FPAR ;

cmdWrite: WRITE ABPAR listW FPAR ;

listW: elemW (VIG elemW)* ;

elemW: expr | CADEIA ;

cmdAtrib: ID ATRIB expr ;

expr: expr OR expr1
    | expr1 ;

expr1: expr1 AND expr2
    | expr2 ;

expr2: expr3 OPREL expr3
    | expr3 ;

expr3: expr3 OPAD expr4
    | expr4 ;

expr4: expr4 OPMULT expr5
    | expr5 ;

expr5: OPNEG expr5
     | ABPAR expr FPAR
     | ID
     | CTE
     | TRUE
     | FALSE ;
