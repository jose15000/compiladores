lexer grammar lexerGrammar;

options { caseInsensitive = true; }

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
ATRIB   : ':=';

// Identificadores (máx 16 caracteres)
ID : [a-zA-Z] [a-zA-Z_0-9]* ;

// Constante numérica (0 a 65535)
CTE : '0' | [1-9] [0-9]{0,4} ;

// Constante de cadeia de texto
CADEIA : '"' .*? '"' ;

// Comentários
COMENTARIOS_LINHA : '//' .*? '\n' -> skip ;

// Descartar espaços em branco
WS : [ \t\r\n]+ -> skip ;
