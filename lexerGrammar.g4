lexer grammar lexerGrammar;

// Palavras reservadas
PROGRAM : 'PROGRAM' ;
INTEGER : 'INTEGER' ;
BOOLEAN : 'BOOLEAN' ;
STRING  : 'STRING' ;
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

// Operadores aritméticos
OPAD    : '+' | '-' ; 
OPMULT  : '*' | '/' ;
OPLOG   : 'OR' | 'AND' ; 
OPNEG   : '~' | 'NOT' ;

// Operadores relacionais
OPREL   : '<' | '<=' | '>' | '>=' | '==' | '<>' ;

// Símbolos
PVIG    : ';' ;
PONTO   : '.' ;
DPONTOS : ':' ;
VIG     : ',' ;
ABPAR   : '(' ;
FPAR    : ')' ;
ATRIB   : ':=' ;


IDENTIFIER : [a-zA-Z0-9]{1,16} ;

CTE : [0-9]+ {
value = int(self.text)
if value > 65535:
    raise Exception(f"Constante fora do intervalo de 2 bytes: {self.text}")
};

STRING_LITERAL : '"' (~["\r\n] | '""')* '"' ;

// Comentários de linha
COMMENT : '//' ~[\r\n]* -> skip ;

// Descartar espaços em branco
WS : [ \t\r\n]+ -> skip ;