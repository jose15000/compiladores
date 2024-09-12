lexer grammar lexerGrammar;

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
IF      : 'IF' ;       
THEN    : 'THEN' ;      
ELSE    : 'ELSE' ;     

// operadores aritméticos
OPAD    : '+' | '-' ; 
OPMULT  : '*' | '/' ;
OPLOG   : 'OR' | 'AND' ; // Corrigido para OPLOG
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
ATRIB   : ':=';

// identificadores (maíusculas, minúsculas e números)
ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// constante numérica
CTE: [0-9]+ ;

// constante string
CADEIA: '"' .*? '"' ;

// comentários
COMENTARIOS_LINHA : '//' .*? '\n' -> skip ;

// descartar espaços em branco
WS : [ \t\r\n]+ -> skip ;
