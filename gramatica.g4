grammar gramatica;

// palavras reservadas

PROGRAM : 'PROGRAM' ;
INTEGER : 'INTEGER' ;
BOOLEAN : 'BOOLEAN' ;
BEGIN   : 'BEGIN' ;
END     : 'END' ;
WHILE   : 'WHILE' ; 
DO      : 'DO' ;
READ    : 'READ' ;
VAR     : 'VAR' ;
FALSE   : 'FALSE' ;
TRUE    : 'TRUE' ;
WRITE   : 'WRITE' ;

// operadores aritméticos

OPAD    : '+' | '-' ; 
OPMULT  : '*' | '/' ;
OPLOG   : 'OR' | 'AND' ;
OPNEG   : '~' ;

// operadores relacionais

OPREL   : '<' | '<=' | '>' | '>=' | '==' | '<>' ;

// símbolos

PVIG    : ';' ;
PONTO   : '.' ;
DPONTOS : ':' ;
VIG     : ',' ;
ABPAR   : '(' ;
FPAR    : ')' ;
ATRIB   : ':=' ;

// descartar espaços em branco
WS : [ \t\r\n ]+ -> skip ;

// identificadores (maíusculas, minúsculas e números)

ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// comentários

COMENTARIOS_LINHA : '//' ~[\r\n]* -> skip ;

programa : PROGRAM ID PVIG ; 